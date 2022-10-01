# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

import os
os.environ['BOARD'] = 'RFSoC4x2'

from time import time, sleep
from datetime import datetime
import subprocess as sp
import logging
import netifaces
import pandas as pd
import numpy as np
from pynq import get_rails, DataRecorder, allocate
from pynq import GPIO
from pynq.lib.pmod import pmod_cable
from pynq.overlays.base import BaseOverlay
from rfsoc4x2 import oled
from rfsystem.spectrum_sweep import ToneGenerator
from rfsystem.spectrum_sweep import FrequencySelector
from rfsystem.spectrum_sweep import SpectrumProcessor
from rfsystem.cmac import CMAC

lmk_reset = GPIO(341, 'out')
lmk_reset.write(0x0)

# Test constants
V_ERR = 10
MIN_V_ERR = (100 - V_ERR) / 100
MAX_V_ERR = (100 + V_ERR) / 100

RAIL_RANGES = {
    'VCCp0V85': {'voltage': (0.85 * MIN_V_ERR, 0.85 * MAX_V_ERR),
             'current': (0, 20)},
    'VCCp3V3': {'voltage': (3.3 * MIN_V_ERR, 3.3 * MAX_V_ERR),
               'current': (0, 2)},
    'VCCp1V8': {'voltage': (1.8 * MIN_V_ERR, 1.8 * MAX_V_ERR),
               'current': (-3, 3)},
    'VDAC_AVCC': {'voltage': (0.925 * MIN_V_ERR, 0.925 * MAX_V_ERR),
               'current': (-3, 3)},
    'VADC_AVCC': {'voltage': (0.925 * MIN_V_ERR, 0.925 * MAX_V_ERR),
            'current': (0, 6)},
    'VADC_AVCCAUX': {'voltage': (1.8 * MIN_V_ERR, 1.8 * MAX_V_ERR),
               'current': (0, 2)},
    'VDAC_AVCCAUX': {'voltage': (1.8 * MIN_V_ERR, 1.8 * MAX_V_ERR),
            'current': (0, 2)},
    'VDAC_AVTT': {'voltage': (2.5 * MIN_V_ERR, 2.5 * MAX_V_ERR),
               'current': (0, 6)},
}

FREQUENCIES = [200, 600, 1000, 1600, 2600, 3200, 3600, 4200, 4400, 4800]
BITSTREAM_PATH = 'base.bit'


class SelfTestOverlay(BaseOverlay):

    def __init__(self, bitfile_name=BITSTREAM_PATH, autoconfig=False,
                 **kwargs):

        super().__init__(bitfile_name, **kwargs)
        addrs = netifaces.ifaddresses('eth0')
        self.oled_display = oled.oled_display()
        self.mac = addrs[netifaces.AF_LINK][0]['addr'].upper()
        self.pmbus_rails = None
        self.pmbus_recorder = None
        self.pmbus_sensors = None
        self.sweep = []
        self.sweep_results = []
        self.syzygy_pin_pairs = [
            (1, 3),
            (5, 7),
            (8, 10),
            (9, 11),
            (12, 14),
            (13, 15),
            (16, 18),
            (17, 19),
            (20, 22),
            (21, 23),
            (24, 26),
            (25, 27),
            (28, 30),
            (29, 31),
        ]
        
        if autoconfig:
            self.configure_all()

    def configure_all(self):
        """The main call to configure all the components.

        This step can generate some exceptions for bad boards so we have to
        be careful. By default, this `configure()` will not be called.
        A formal test should follow the steps in this method.

        """
        self.init_i2c()
        self.config_leds()
        self.config_pmbus()
        self.init_rf_clks()
        self.config_tile_clock(btype='dac', tile=0)
        self.config_tile_clock(btype='dac', tile=2)
        self.config_tile_clock(btype='adc', tile=0)
        self.config_tile_clock(btype='adc', tile=2)
        self.config_sweep()

    def config_leds(self):
        """ Configure all the LEDs.
        
        LEDs are off by default after configuration.

        """
        delay = 0.3
        for led in [0, 1]:
            self.rgbleds[led].write(1)
            sleep(delay)
            self.rgbleds[led].write(0)
        for led in self.leds:
            led.on()
            sleep(delay)
            led.off()

        for i in range(0, 3):
            self.leds.write(15, 0xF)
            sleep(delay)
            self.leds.write(0, 0xF)
            sleep(delay)

    def test_syzygy_loop_back(self, pin_pair):
        input_pin, output_pin = pin_pair
        write_value = 0x1 << input_pin
        self.syzygy_std0.write(0, write_value)
        read_value = self.syzygy_std0.read(0)
        assert (
            read_value & (0x1 << output_pin)
        ) >> output_pin == 0x1, "Read value is {}.".format(read_value)
        write_value = 0x0
        self.syzygy_std0.write(0, write_value)
        read_value = self.syzygy_std0.read(0)
        assert (
            read_value & (0x1 << output_pin)
        ) >> output_pin == 0x0, "Read value is {}.".format(read_value)
            
    def config_pmbus(self):
        """Configure pmbus related attributes.

        This includes the pmbus rails and sensors.

        """
        self.pmbus_rails = get_rails()
        sensors = []
        for rail in list(self.pmbus_rails.values()):
            sensors.append(rail.voltage)
            sensors.append(rail.current)
            sensors.append(rail.power)
        self.pmbus_sensors = sensors
        self.pmbus_recorder = DataRecorder(*sensors)

    def config_sweep(self):
        """Configure the spectrum sweep.

        Use a default setting.

        """
        frequencies = [200, 600, 1000, 1600, 2600, 3200, 3600, 4200, 4400, 4800]
        number_samples = 12288
        for i in range(0, 4):
            #if i < 2:
                #j = 0
            #else:
                #j = 1
            self.sweep.append(SpectrumSweepApplication(
                dac_channel=self.radio.transmitter.channel,
                adc_channel=self.radio.receiver.channel[i],
                frequencies=frequencies,
                number_samples=number_samples))

    def config_tile_clock(self, btype='adc', tile=0):
        """Simple method to check that a tile's PLL clock has a valid input.

        """
        tile = getattr(self.radio.rfdc, ''.join([btype, '_tiles']))[tile]
        tile.DynamicPLLConfig(1, 491.52, 4915.2)

    def test_pll_clocks(self):
        """Test all pll tile config using config_tile_clock().

        """
        self.config_tile_clock(btype='dac', tile=0)
        self.config_tile_clock(btype='dac', tile=2)
        self.config_tile_clock(btype='adc', tile=0)
        self.config_tile_clock(btype='adc', tile=2)
    
    def test_cmac(self):
        self.cmac.internal_loopback = 0
        self.cmac.start()
        raw_str = ' /$$$$$$$  /$$     /$$ /$$   /$$  /$$$$$$ \n| $$__  $$|  $$   /$$/| $$$ | $$ /$$__  $$\n| $$  \\ $$ \\  $$ /$$/ | $$$$| $$| $$  \\ $$\n| $$$$$$$/  \\  $$$$/  | $$ $$ $$| $$  | $$\n| $$____/    \\  $$/   | $$  $$$$| $$  | $$\n| $$          | $$    | $$\\  $$$| $$/$$ $$\n| $$          | $$    | $$ \\  $$|  $$$$$$/\n|__/          |__/    |__/  \\__/ \\____ $$$\n                                      \\__/\n\n                                          \n                                         '
        packets_in = np.array(list(raw_str.encode()))
        dma_buf_in = allocate(packets_in.shape[0])
        dma_buf_out = allocate(packets_in.shape[0])
        dma_buf_in[:]=packets_in
        self.dma.sendchannel.transfer(dma_buf_in)
        self.dma.recvchannel.transfer(dma_buf_out)
        self.dma.sendchannel.wait()
        self.dma.recvchannel.wait()
        packets_out = bytes(dma_buf_out)
        logprint('CMAC packets out: \n{}'.format(packets_out.decode()))
        return np.array_equal(dma_buf_in,dma_buf_out)
    
    def test_pmods(self):
        """ Tests PMODs 
        
        Transmit a simple bit pattern over a loopback cable from PMODA to PMODB. If all bits correct -> pass.
        
        """
        self.pmod_outputs = [pmod_cable.Pmod_Cable(test_overlay.PMODA, i, 'out', 'straight') for i in range(8)]
        self.pmod_inputs = [pmod_cable.Pmod_Cable(test_overlay.PMODB, i, 'in', 'straight') for i in range(8)]
        bits = [0,1,0,1,0,1,0,1]
        for pmod_out, bit in zip(self.pmod_outputs, bits):
            pmod_out.write(bit)
        received_bits = [pmod_in.read() for pmod_in in self.pmod_inputs]
        assert bits == received_bits

    def test_power_rail(self):
        """Check pmbus for non nominal values.
        SYZYGY power rail will not be tested since it is module dependent.
        Returns
        -------
        dict
            A dictionary storing the power rail test results, each being
            a bool value, indicating pass or fail.
        """
        pmbus_flags = {}
        for rail, rail_sensors in RAIL_RANGES.items():
            for sensor in rail_sensors:
                key = '{}_{}'.format(rail, sensor)
                pmbus_flags[key] = 'OK'
                for m in self.pmbus_recorder.frame[key]:
                    if not rail_sensors[sensor][0] <= m <= \
                           rail_sensors[sensor][1]:
                        pmbus_flags[key] = 'Error: Under Voltage'
        return pmbus_flags

    def test_sweep(self):
        """Runs spectrum sweep whilst recording pmbus sensors.

        Returns
        -------
        dict
            A dictionary storing the power rail test results, each being
            a bool value, indicating pass or fail.

        """
        rfdc_results = []

        with self.pmbus_recorder.record(1):
            for i in range(0, 4):
                self.sweep[i].run()
        
        for i in range(0, 4):
            array_results = self.sweep[i].results
            fundamental_result = not all(array_results[0] - array_results[1])
            if fundamental_result == True:
                fundamental_result = 'Pass'
            else:
                fundamental_result = 'Fail'
            sfdr_result = all(array_results[2] > 40)
            if sfdr_result == True:
                sfdr_result = 'Pass'
                logprint('Spectrum Sweep Pass: DAC -> ADC channel {}: SFDR is above the lower limit of 40dB'.format(i))
            else:
                sfdr_result = 'Fail'
                logprint('Spectrum Sweep Error: DAC -> ADC channel {}: SFDR is below the lower limit of 40dB'.format(i))
                logprint('** Did you connect the SMA cables to the correct DAC and ADC?**')
            channel_result = fundamental_result and sfdr_result
            rfdc_results.append(channel_result)

        dc_channel_flags = {}
        for i in range(0, 4):
            dc_channel_flags['RFSoC Data Converters_ch_{}'.format(i)] = rfdc_results[i]
        return dc_channel_flags


class SpectrumSweepApplication:
    """A Spectrum Sweep Application.

    """
    def __init__(self, dac_channel, adc_channel,
                 frequencies=FREQUENCIES, number_samples=12288):
        """Class constructor for the Spectrum Sweep Application.

        Create a new spectrum sweep application by assigning a DacChannel and
        ADCChannel object. Optionally set the frequencies to be tested between
        0 to 4915.2MHz. The number of samples defines the FFT size for calculating
        the fundamental receive frequency and simple SFDR.

        Attributes
        ----------
        results : Read-only, returns a pandas data frame with the results of
        the previous spectrum sweep run. If no run has executed, returns None.

        """
        self._results = None
        self._frequencies = frequencies

        self._sample_frequency = \
            adc_channel.adc_block.BlockStatus['SamplingFreq']*1e9 / \
            adc_channel.adc_block.DecimationFactor

        self._number_samples = number_samples

        self._rbw = self._sample_frequency/self._number_samples

        self._spectrum_processor = SpectrumProcessor(
            channel=adc_channel,
            sample_frequency=self._sample_frequency,
            number_samples=self._number_samples)

        self._frequency_selector = FrequencySelector(
            block=adc_channel.adc_block)

        self.generators = []
        for i in range(0, len(dac_channel)):
            self.generators.append(
                ToneGenerator(channel=dac_channel[i]))
        
    @property
    def results(self):
        """ Returns the results of the previous run in a pandas dataframe.

        """
        return pd.DataFrame(data=self._results,
                            index=["TX Frequency (MHz)",
                                   "RX Fundamental (MHz)", "SFDR (dB)"])
    
    def _start_generator(self):
        """ Starts the tone generator

        """
        for generator in self.generators:
            generator.frequency_selector.centre_frequency = 600 # MHz
            generator.amplitude_controller.enable = True
            generator.amplitude_controller.gain = 0.5
        
    def _stop_generator(self):
        """ Stops the tone generator

        """
        for generator in self.generators:
            generator.amplitude_controller.enable = False
            generator.amplitude_controller.gain = 0

    def _calculate_simple_sfdr(self, spectrum):
        """ Calculates the SFDR for a given spectrum and channel properties

        """
        return np.max(spectrum) - np.average(spectrum)

    def _calculate_fundamental(self, spectrum):
        """ Calculated the fundamental signal in a spectrum given the channel
        properties

        """
        maxindex = np.argsort(spectrum)[-1:][0]
        return (maxindex * self._rbw +
                abs(self._frequency_selector.centre_frequency*1e6) -
                self._sample_frequency/2)*1e-6

    def _run_sweep(self):
        """ Runs the Spectrum Sweep Application

        """
        fundamental = []
        sfdr = []
        frequency_zones = \
            [self._sample_frequency/2*1e-6,
             (self._sample_frequency + self._sample_frequency/2)*1e-6]
        for frequency in self._frequencies:
            for generator in self.generators:
                generator.frequency_selector.centre_frequency = frequency
            sleep(1)
            if frequency*1e6 < self._sample_frequency:
                receive_frequency = frequency_zones[0]
            else:
                receive_frequency = frequency_zones[1]
            self._frequency_selector.centre_frequency = receive_frequency
            spectrum = self._spectrum_processor.get_spectrum()
            fundamental.append(self._calculate_fundamental(spectrum))
            sfdr.append(self._calculate_simple_sfdr(spectrum))
        self._results = np.array([self._frequencies, fundamental, sfdr])

    def run(self):
        """ Starts the tone generator and runs Spectrum Sweep
        Applications

        """
        self._start_generator()
        self._run_sweep()
        self._stop_generator()


start_time = time()
test_flags = {}

boot_log_dir = '/boot/BootLogs'
test_log_dir = '/boot/TestLogs'
if not os.path.exists(boot_log_dir):
    os.mkdir(boot_log_dir)
if not os.path.exists(test_log_dir):
    os.mkdir(test_log_dir)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

now = datetime.now()
time_str = now.strftime("%Y_%m_%d_%H_%M_%S")
testlog = os.path.join(test_log_dir, '{}_test.log'.format(time_str))
bootlog = os.path.join(boot_log_dir, '{}_boot.log'.format(time_str))
logger = logging.getLogger()
fhandler = logging.FileHandler(filename=testlog, mode='a')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)
tty_path = '/dev/ttyPS0'
tty = os.open(tty_path, os.O_RDWR)


def logprint(message):
    logging.debug(message)
    if terminal_ok:
        os.write(tty, bytes(message + '\n', 'utf-8'))
    print(message)


"""Section 0: Log the boot message, download overlay

This section is supposed to be free of errors. If it does not boot properly,
there is no way to test.

The serial needs some time to be stable, give it 10 second timeout period.

"""
command = 'dmesg > {}'.format(bootlog)
os.system(command)
test_overlay = SelfTestOverlay()

timeout, terminal_ok = 10, True
msg = '==== Self-test started ===='
while timeout > 0:
    try:
        ret = os.write(tty, bytes(msg + '\n', 'utf-8'))
        if ret > 0:
            break
    except:
        pass
    timeout -= 1
    sleep(1)
if timeout == 0:
    terminal_ok = False


"""Section 1: Test the basic components.

This section includes the basic tests for MAC, LEDs, I2C, and PMBUS.

"""
mac = test_overlay.mac
test_flags['mac_test'] = 'Pass'
try:
    i2c_mac = sp.getoutput('i2cdump -y -r 0x9A-0x9F 1 0x58')[149:166].upper().replace(' ',':')
    assert i2c_mac == test_overlay.mac
except:
    test_flags['mac_test'] = 'Fail'
logprint('MAC: {}'.format(test_flags['mac_test']))
logprint('MAC address: {}'.format(mac))
logprint('MAC address from eeprom: {}'.format(i2c_mac))

test_flags['config_leds'] = 'Pass'
try:
    test_overlay.config_leds()
except:
    test_flags['config_leds'] = 'Fail'
logprint('LED: {}'.format(test_flags['config_leds']))


test_flags['init_i2c'] = 'Pass'
try:
    test_overlay.init_i2c()
except:
    test_flags['init_i2c'] = 'Fail'
logprint('I2C: {}'.format(test_flags['init_i2c']))

test_flags['config_syzygy'] = 'Pass'
try:
    test_overlay.set_syzygy_vio(1.8)
    test_overlay.syzygy_std0.write(4, 0xCCCCCC9D)
    _ = [test_overlay.test_syzygy_loop_back(i) \
         for i in test_overlay.syzygy_pin_pairs]
except:
    test_flags['config_syzygy'] = 'Fail'
logprint('SYZYGY: {}'.format(test_flags['config_syzygy']))

test_flags['config_pmbus'] = 'Pass'
try:
    test_overlay.config_pmbus()
except:
    test_flags['config_pmbus'] = 'Fail'
logprint('Configure PMBUS: {}'.format(test_flags['config_pmbus']))

test_flags['test_cmac'] = 'Pass'
try:
    test_overlay.test_cmac()
except:
    test_flags['test_cmac'] = 'Fail'
logprint('CMAC: {}'.format(test_flags['test_cmac']))

test_flags['pmod_test'] = 'Pass'
try:
    test_overlay.test_pmods()
except:
    test_flags['pmod_test'] = 'Fail'
logprint('PMOD: {}'.format(test_flags['pmod_test']))

if 'Fail' in [test_flags['mac_test'], test_flags['config_leds'], \
        test_flags['init_i2c'], test_flags['config_syzygy'], \
        test_flags['config_pmbus'], test_flags['pmod_test']]:
    test_overlay.leds[0].off()
else:
    test_overlay.leds[0].on()

"""Section 2: Test Clocks

In this section we will reconfigure the RF clock chips, namely, LMK and LMX
chips.

"""
test_flags['set_ref_clks'] = 'Pass'
try:
    test_overlay.init_rf_clks()    
except RuntimeError as e:
    test_flags['set_ref_clks'] = 'Fail'
    logprint('Set RF Data Converter clocks failed: {}'.format(str(e)))
logprint('Set RF Data Converter clocks: {}'.format(test_flags['set_ref_clks']))


if test_flags['set_ref_clks']:
    test_overlay.leds[1].on()


"""Section 3: Test RF components.

We will configure the RF components, including ADC, DAC. After that, we 
sweep the frequency domain while checking power.

"""
test_flags['config_rf'] = 'Pass'
try:
    test_overlay.config_tile_clock(btype='dac', tile=0)
    test_overlay.config_tile_clock(btype='dac', tile=2)
    test_overlay.config_tile_clock(btype='adc', tile=0)
    test_overlay.config_tile_clock(btype='adc', tile=2)
    test_overlay.config_sweep()
except RuntimeError as e:
    test_flags['config_rf'] = 'Fail'
    logprint('Configure ADC/DAC failed: {}'.format(str(e)))
logprint('Configure ADC/DAC: {}'.format(test_flags['config_rf']))

test_flags['pmbus_rails'] = 'Pass'
try:
    rails = map(str, test_overlay.pmbus_rails.values())
    logprint('\n' + '\n'.join(rails))
except:
    test_flags['pmbus_rails'] = 'Fail'
logprint('PMBUS rails: {}'.format(test_flags['pmbus_rails']))

test_flags['RFSoC Data Converters_test'] = 'Pass'
try:
    dc_ch_flags = test_overlay.test_sweep()
except Exception as e:
    test_flags['RFSoC Data Converters_test'] = 'Fail'
    logprint('RFSoC Data Converter test failed: {}'.format(str(e)))
else:
    test_flags.update(dc_ch_flags)
    if list(dc_ch_flags.values()).count('Pass') < 4:
        test_flags['RFSoC Data Converters_test'] = 'Fail'
        
logprint('RFSoC Data Converters tests: {}'.format(test_flags['RFSoC Data Converters_test']))


test_flags['pmbus_test'] = 'Pass'
try:
    pmbus_ch_flags = test_overlay.test_power_rail()
except:
    test_flags['pmbus_test'] = 'Fail'
else:
    test_flags.update(pmbus_ch_flags)
    for pmbus_ch in pmbus_ch_flags.values():
        test_flags['pmbus_test'] = test_flags['pmbus_test'] and pmbus_ch
logprint('PMBUS tests: {}'.format(test_flags['pmbus_test']))


if test_flags['pmbus_rails'] and test_flags['pmbus_test']:
    test_overlay.leds[2].on()


if test_flags['config_rf'] and test_flags['RFSoC Data Converters_test']:
    test_overlay.leds[3].on()

try:
    df_ch0 = test_overlay.sweep[0].results
    logprint('ch0:\n' + str(df_ch0.round(2)))
except:
    logprint('ch0 data not available.')

try:
    df_ch1 = test_overlay.sweep[1].results
    logprint('ch1:\n' + str(df_ch1.round(2)))
except:
    logprint('ch1 data not available.')

try:
    df_ch2 = test_overlay.sweep[2].results
    logprint('ch2:\n' + str(df_ch2.round(2)))
except:
    logprint('ch2 data not available.')

try:
    df_ch3 = test_overlay.sweep[3].results
    logprint('ch3:\n' + str(df_ch3.round(2)))
except:
    logprint('ch3 data not available.')

try:
    dump = str(test_overlay.pmbus_recorder.frame)
    logprint('pmbus dump:\n' + dump)
except:
    logprint('PMBUS recorder data not available.')


""" Final check if all tests passed.

Light on green LEDs if all tests have passed. Otherwise light red.

"""
self_test_passed = True
for flag, flag_val in test_flags.items():
    logprint('{}: {}'.format(flag, flag_val))
    if flag_val == 'Pass' or flag_val == 'OK':
        passState = True
    else:
        passState = False
    self_test_passed = self_test_passed and passState

logprint('*******************************************')
if self_test_passed:
    test_overlay.rgbleds[0].on(2)
    test_overlay.rgbleds[1].on(2)
    test_overlay.oled_display.write('Test PASS.')
    logprint('Test PASS.')
    logprint('*******************************************')
else:
    test_overlay.rgbleds[0].on(4)
    test_overlay.rgbleds[1].on(4)
    test_overlay.oled_display.write('Test FAIL.')
    logprint('Test FAIL.')
logprint('*******************************************')

end_time = time()
logprint('Test took {0:.2f}s'.format(end_time - start_time))
logprint('Test logged to: {}'.format(testlog))
logprint('==== Self-test finished ====')
os.close(tty)
