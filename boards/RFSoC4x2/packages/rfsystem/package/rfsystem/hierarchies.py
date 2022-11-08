# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause



from pynq import DefaultHierarchy
from pynq import allocate
from .transmitter import AmplitudeController
from .receiver import PacketGenerator
from .constants import *
import numpy as np
import xrfdc
from time import sleep

class Transmitter(DefaultHierarchy):
    """Wrapper for the transmit pipeline.

    This wrapper assumes the following pipeline structure and naming

    channel_xy -> rfdc
    where x is a number associated with the relevant dac tile,
    and y is a number associated with the relevant dac block.

    Attributes
    ----------
    channel : list
        A list of hierarchies.DacChannel. The DacChannels are listed in the
        alphanumeric order that they are found.
        Indexing channel retrieves the associated
        DacChannel. Use get_channel_description() to obtain
        information of the associated adc_block and adc_tile as a dict.

    """

    @staticmethod
    def checkhierarchy(description):
        """The hierarchy must contain channel hierarchies and be named
        transmitter.
        """
        return (any('channel_' in s for s in description['hierarchies']) and
                description['fullpath'].split('/')[-1] == 'transmitter')

    def __init__(self, description, dac_tiles=None):
        """Initialise the driver for the transmit pipeline
        """
        super().__init__(description)
        self.channel = []
        self._dac_list = []
        self._dac_tiles = dac_tiles
        for i in range(0, NO_DAC_TILES):
            for j in range(0, NO_DAC_BLOCKS_PTILE):
                if ''.join(['channel_', str(i), str(j)]) in \
                        description['hierarchies']:
                    self.channel.append(getattr(
                        self, ''.join(['channel_', str(i), str(j)])))
                    self._dac_list.append([i, j])

    def _initialise_dacs(self):
        """Configure all DACs in the design as indicated by the dac_list.
        """
        for i in range(0, len(self._dac_list)):
            self.channel[i].dac_tile = self._dac_tiles[self._dac_list[i][0]]
            self.channel[i].dac_block = self.channel[i].dac_tile.blocks[
                self._dac_list[i][1]]
            self._setup_dac(self.channel[i].dac_tile,
                            self.channel[i].dac_block)

    def _setup_dac(self, dac_tile, dac_block):
        """Configure the dac block with default parameters.
        
        The DACs operate at 4096MHz with interpolation factor of 2. Just
        set the mixer frequency to 1000 as default. The fc must be because
        the first nyquist zone is set for the RF-DAC block.
        """        
        dac_tile.DynamicPLLConfig(1, 491.52, 4915.2)
        sleep(0.6)
        dac_block.NyquistZone = 1
        dac_block.MixerSettings = {
            'CoarseMixFreq':  xrfdc.COARSE_MIX_BYPASS,
            'EventSource':    xrfdc.EVNT_SRC_IMMEDIATE,
            'FineMixerScale': xrfdc.MIXER_SCALE_1P0,
            'Freq':           1228.8,
            'MixerMode':      xrfdc.MIXER_MODE_C2R,
            'MixerType':      xrfdc.MIXER_TYPE_FINE,
            'PhaseOffset':    0.0
        }
        dac_block.UpdateEvent(xrfdc.EVENT_MIXER)
        dac_tile.SetupFIFO(True)
        
    def get_channel_description(self):
        """Obtains the channels and their tile and block for the user.
        """
        ch_dict = {}
        for i in range(0, len(self._dac_list)):
            tile = self._dac_list[i][0]
            block = self._dac_list[i][1]
            ch_dict.update({''.join(["Channel ", str(i)]): 
                            {"Tile": tile+228,
                             "Block": block}})
        return ch_dict
    
            
class Receiver(DefaultHierarchy):
    """Wrapper for the receiver pipeline.
    
    This wrapper assumes the following pipeline structure and naming
    
    rfdc => channel_xy
    where x is a number associated with the relevant adc tile,
    and y is a number associated with the relevant adc block.
    
    Attributes
    ----------
    channel : A list of hierarchies.AdcChannel
        The AdcChannels are listed in the alphanumeric order that
        they are found. Indexing channel retrieves the associated
        AdcChannel. Use get_channel_description() to obtain
        information of the associated adc_block and adc_tile as a dict.
    
    """
    
    @staticmethod
    def checkhierarchy(description):
        """The hierarchy must contain channel hierarchies and be named receiver.
        """
        return (any('channel_' in s for s in description['hierarchies']) and
                description['fullpath'].split('/')[-1] == 'receiver')
    
    def __init__(self, description, adc_tiles=None):
        """Initialise the driver for the reciever pipeline
        """
        super().__init__(description)
        self.channel = []
        self._adc_list = []
        self._adc_tiles = adc_tiles
        for i in range(0, NO_ADC_TILES):
            for j in range(0, NO_ADC_BLOCKS_PTILE):
                if ''.join(['channel_', str(i), str(j)]) in \
                        description['hierarchies']:
                    self.channel.append(getattr(
                        self, ''.join(['channel_', str(i), str(j)])))
                    self._adc_list.append([i, j])

    def _initialise_adcs(self):
        """Configure all ADCs in the design as indicated by the adc_list.
        """
        for i in range(0, len(self._adc_list)):
            self.channel[i].adc_tile = self._adc_tiles[self._adc_list[i][0]]
            self.channel[i].adc_block = self.channel[i].adc_tile.blocks[
                self._adc_list[i][1]]
            self._setup_adc(self.channel[i].adc_tile,
                            self.channel[i].adc_block)
                    
    def _setup_adc(self, adc_tile, adc_block):
        """Configure the adc block with default parameters.
        
        The ADCs operate at 4096MHz with decimation factor of 2. Just
        set the mixer frequency to 1024. Negative fc because first nyquist
        zone is set for RF-ADC.
        """     
        adc_tile.DynamicPLLConfig(1, 491.52, 4915.2)
        sleep(0.6)
        adc_block.NyquistZone = 1
        adc_block.MixerSettings = {
            'CoarseMixFreq':  xrfdc.COARSE_MIX_BYPASS,
            'EventSource':    xrfdc.EVNT_SRC_TILE,
            'FineMixerScale': xrfdc.MIXER_SCALE_1P0,
            'Freq':           -1228.8,
            'MixerMode':      xrfdc.MIXER_MODE_R2C,
            'MixerType':      xrfdc.MIXER_TYPE_FINE,
            'PhaseOffset':    0.0
        }
        adc_block.UpdateEvent(xrfdc.EVENT_MIXER)
        adc_tile.SetupFIFO(True)
            
    def get_channel_description(self):
        """Obtains the channels and their tile and block for the user.
        """
        ch_dict = {}
        for i in range(0, len(self._adc_list)):
            tile = self._adc_list[i][0]
            block = self._adc_list[i][1]
            ch_dict.update({''.join(["Channel ", str(i)]): 
                            {"Tile": tile+224,
                             "Block": block}})
        return ch_dict
    
        
class DacChannel(DefaultHierarchy):
    """Wrapper for the dac channel hierarchy.
    
    This wrapper assumes the following pipeline structure and naming
    
    amplitude_controller -> rfdc
    
    Attributes
    ----------
    dac_tile : xrfdc.dac_tile
        The channel's associated DAC Tile. Can be used by the user
        to directly control the tile.
        
    dac_block : xrfdc.dac_block
        The channel's associated DAC Block. Can be used by the user
        to directly control the block.
        
    control : transmitter.AmplitudeController
        The Amplitude Controller that enables/disables signal
        output gain.
    
    """
    @staticmethod
    def checkhierarchy(description):
        return ('amplitude_controller' in description['ip'] and
                description['fullpath'].split('/')[-2] == 'transmitter')
    
    def __init__(self, description, dac_tile=None, dac_block=None):
        """Initialise the driver for the dac channel hierarchy.
        
        """
        super().__init__(description)
        self.dac_tile = dac_tile
        self.dac_block = dac_block
        self.control = self.amplitude_controller
        
                    
class AdcChannel(DefaultHierarchy):
    """Wrapper for the adc channel hierarchy.
    
    This wrapper assumes the following pipeline structure and naming
    
    rfdc => packet_generator -> axi_dma_real
                             -> axi_dma_imag
    
    Attributes
    ----------
    adc_tile : xrfdc.adc_tile
        The channel's associated ADC Tile. Can be used by the user
        to directly control the tile.
        
    adc_block : xrfdc.adc_block
        The channel's associated ADC Block. Can be used by the user
        to directly control the block.
    
    """
    
    @staticmethod
    def checkhierarchy(description):
        return ('packet_generator' in description['ip'] and
                'axi_dma_real' in description['ip'] and
                'axi_dma_imag' in description['ip'] and
                description['fullpath'].split('/')[-2] == 'receiver')
    
    def __init__(self, description, adc_tile=None, adc_block=None):
        """Initialise the driver for the adc channel hierarchy.
        """
        super().__init__(description)
        self.adc_tile = adc_tile
        self.adc_block = adc_block
        self._pgen = self.packet_generator
        self._dma_real = self.axi_dma_real
        self._dma_imag = self.axi_dma_imag
        
    def transfer(self, packetsize):
        """Returns a numpy array with inspected data of length packetsize.
        """
        transfersize = int(np.ceil(packetsize/8))
        if transfersize > 4096 or transfersize < 2:
            raise ValueError(
                'Packet size incorrect, should be in range 16 to 32768.')
        self._pgen.packetsize = transfersize
        buffer_re = allocate(shape=(transfersize*8,), dtype=np.int16)
        buffer_im = allocate(shape=(transfersize*8,), dtype=np.int16)
        self._dma_real.recvchannel.transfer(buffer_re)
        self._dma_imag.recvchannel.transfer(buffer_im)
        self._pgen.transfer = 1
        self._dma_real.recvchannel.wait()
        self._dma_imag.recvchannel.wait()
        self._pgen.transfer = 0
        re_data = np.array(buffer_re) * 2**-15
        im_data = np.array(buffer_im) * 2**-15
        buffer_re.freebuffer()
        buffer_im.freebuffer()
        c_data = re_data.astype('double') + 1j * im_data.astype('double')
        return c_data[0:packetsize]
    

class RadioWrapper(DefaultHierarchy):
    """Hierarchy driver for the entire radio subsystem.

    Exposes the transmit, receive, and rfdc as attributes. The rfdc
    dac and adc tiles are passed to the transmitter and receiver
    respectively.
    
    This wrapper assumes the following separate pipelines
    * transmitter -> rfdc -> "the outside world"
    * "the outside world" -> rfdc => receiver
    
    The rfdc core is common between each pipeline.

    Attributes
    ----------
    transmitter : pynq.lib.radio.Transmitter
        The transmit control system
    receiver : pynq.lib.radio.Receiver
        The receive control system
    rfdc : xrfdc package
        The RF Data Converter core

    """

    @staticmethod
    def checkhierarchy(description):
        tx_pipeline = None
        rx_pipeline = None
        rfdc = None
        
        for hier, details in description['hierarchies'].items():
            if details['driver'] == Transmitter:
                tx_pipeline = hier
            elif details['driver'] == Receiver:
                rx_pipeline = hier

        for ip, details in description['ip'].items():
            if details['driver'] == xrfdc.RFdc:
                rfdc = ip

        return (tx_pipeline is not None and
                rx_pipeline is not None and
                rfdc is not None)

    def __init__(self, description):
        super().__init__(description)
        tx_pipeline = None
        rx_pipeline = None
        rfdc = None

        for hier, details in description['hierarchies'].items():
            if details['driver'] == Transmitter:
                tx_pipeline = hier
            elif details['driver'] == Receiver:
                rx_pipeline = hier

        for ip, details in description['ip'].items():
            if details['driver'] == xrfdc.RFdc:
                rfdc = ip

        getattr(self, tx_pipeline)._dac_tiles = getattr(self, rfdc).dac_tiles
        getattr(self, rx_pipeline)._adc_tiles = getattr(self, rfdc).adc_tiles
        
        getattr(self, tx_pipeline)._initialise_dacs()
        getattr(self, rx_pipeline)._initialise_adcs()

