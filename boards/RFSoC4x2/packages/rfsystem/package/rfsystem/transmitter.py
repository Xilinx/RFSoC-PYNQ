# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause



from pynq import DefaultIP


class AmplitudeController(DefaultIP):

    """Driver for the transmit control IP Core.
    
    The Amplitude Controller is a simple IP core written
    in VHDL. The core outputs a user defined value on the master
    AXI-Stream interface when the enable register is high.
    This core was purposely designed to communicate with the
    RF Digital-to-Analogue Converter (RF DAC). The user
    can set the amplitude of the signal written to the RF DAC
    and use the RF DAC's fine mixer to generate a tone for
    loopback purposes on their development board.
    
    Attributes
    ----------
    enable : a bool
        If high, enables the output of the gain register on to
        the master AXI-Stream interface.
        
    gain : a float
        A float in Volts, that describes the amplitude of the
        output master AXI-Stream signal. Must be in range 0 to 1.
    
    """
    
    def __init__(self, description):
        super().__init__(description=description)
        
    bindto = ['xilinx.com:ip:amplitude_controller:1.0']
    
    @property
    def enable(self):
        """The state of the output master AXI-Stream data signal.
        If high, the gain register is passed to the data signal, if
        low, a zero is passed to the data signal."""
        return self.read(0x00)
    
    @enable.setter
    def enable(self, enable):
        if enable:
            self.write(0x00, int(1))
        else:
            self.write(0x00, int(0))
    
    @property
    def gain(self):
        """The amplitude of the output master AXI-Stream data signal.
        Measured in volts and should be a float in range 0 to 1."""
        gain = self.read(0x04) & 0x0000FFFF
        if gain > 0:
            return gain/0x7FFF
        else:
            return 0.0
    
    @gain.setter
    def gain(self, gain):
        if 0 <= gain <= 1:
            int_gain = int(gain*0x7FFF*0x00000001) | int(gain*0x7FFF*0x00010000)
            self.write(0x04, int_gain)
        else:
            raise ValueError('Programmable Gain must be in range 0 to 1.')

