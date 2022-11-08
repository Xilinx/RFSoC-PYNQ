# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause



import numpy as np
import plotly.graph_objs as go


class SpectrumProcessor:
    """A spectrum processor class to simplify data movement.
    
    The class calculates the frequency spectrum for a given
    array of time domain data. The frequency spectrum is derived
    as the PSD in dBs. Calling get_spectrum() will obtain a
    new time series and calculate the FFT, returning the PSD."""
    
    def __init__(self,
                 channel,
                 sample_frequency,
                 number_samples):
        """SpectrumProcessor constructor.
        """
        
        self._channel = channel
        self._sample_frequency = sample_frequency
        self._number_samples = number_samples
        self._window = np.array(np.blackman(self._number_samples)[:])
        
    def _get_samples(self):
        """Returns a numpy array
        
        Transfer samples from the Programmable Logic.
        
        """
        return self._channel.transfer(packetsize=self._number_samples)
    
    def _apply_window(self, data):
        """Returns a numpy array
        
        Apply a preprocessing window.
        
        """
        return data * self._window

    def _apply_fft(self, data):
        """Returns a numpy array
        
        Apply an FFT to the time domain signal. Also ensure the
        FFT is shifted appropriately.
        
        """
        return np.fft.fftshift(np.fft.fft(data))
    
    def _convert_to_psd(self, data):
        """Returns a numpy array
        
        Convert the frequency data to PSD.
        
        """
        return (abs(data)**2)/(self._sample_frequency*np.sum(self._window**2))
    
    def _convert_to_db(self, data):
        """Returns a numpy array
        
        Convert the PSD to dBs.
        
        """
        return 10*np.where(data > 0, np.log10(data), 0)
    
    def get_spectrum(self):
        """Returns a numpy array
        
        Obtains samples from the Programmable Logic, applies a
        window, an FFT, a PSD conversion and a dB conversion.
        
        """
        data = self._get_samples()
        data = self._apply_window(data)
        data = self._apply_fft(data)
        data = self._convert_to_psd(data)
        return self._convert_to_db(data)


class SpectrumPlot:
    """A simple spectrum plot for frequency analysis.
    
    This class displays the frequency spectrum using plotly.
    The frequency plot has a variable centre frequency that
    updates the plot's x-axis as appropriate.
    
    Use update_plot(data) to change the contents of the plot.
    
    Use get_plot() to retrieve the plot handle.
    
    """
    
    def __init__(self,
                 sample_frequency,
                 number_samples,
                 centre_frequency,
                 title,
                 height,
                 width):
        """SpectrumPlot constructor
        """
        
        self._centre_frequency = centre_frequency
        self._sample_frequency = sample_frequency
        self._number_samples = number_samples
        
        self._data = go.Scatter(
            x=np.arange(
                -self._sample_frequency/2,
                self._sample_frequency/2,
                self._sample_frequency/self._number_samples) +
            self._centre_frequency,
            y=np.zeros(self._number_samples),
            name='Spectrum')
        
        self._plot = go.FigureWidget(
            data=self._data,
            layout={'title': title,
                    'height': height,
                    'width': width,
                    'xaxis': {'title': 'Frequency (Hz)'},
                    'yaxis': {'title': ''.join(['Amplitude (dB)']),
                              'range': [-200, -60]}})

    @property
    def centre_frequency(self):
        """Dynamically set the centre frequency of the plot.
        Useful for spectrum analysis.
        """
        return self._centre_frequency

    @centre_frequency.setter
    def centre_frequency(self, centre_frequency):
        self._centre_frequency = centre_frequency
        self._plot.data[0].x = np.arange(
            -self._sample_frequency/2,
            self._sample_frequency/2,
            self._sample_frequency/self._number_samples) + \
            self._centre_frequency
        self._plot.layout.xaxis.range = (min(self._plot.data[0].x),
                                         max(self._plot.data[0].x))
    
    def update_plot(self, data):
        """Update the contents of the plot with new data.
        """
        self._plot.data[0].y = data
        
    def get_plot(self):
        """Returns the plotly.go FigureWidget
        """
        return self._plot
    
    
class FrequencySelector:
    """A frequency selector that dynamically changes Nyquist Zone.
    
    The frequency selector changes the centre frequency and, if required,
    the Nyquist Zone of an RF DC block. The block type matters and should
    either be adc, or dac.
    
    """
    
    def __init__(self, block, block_type='adc'):
        """FrequencySelector constructor"""
        
        self._block = block
        self._block_type = block_type
        self._sample_frequency = self._block.BlockStatus['SamplingFreq']*1e3
        self._nyquist_zone = round(
            abs(self._block.MixerSettings['Freq'])/(self._sample_frequency/2))+1

    @property
    def centre_frequency(self):
        """Dynamically set the centre frequency during runtime."""
        return self._block.MixerSettings['Freq']
    
    @centre_frequency.setter
    def centre_frequency(self, centre_frequency):
        self._nyquist_zone = int(
            centre_frequency/(self._sample_frequency/2))+1
        if self._nyquist_zone != self._block.NyquistZone:
            self._block.NyquistZone = self._nyquist_zone
        even_zone = ((self._nyquist_zone % 2) == 0)
        if even_zone:
            if self._block_type == 'adc':
                self._block.MixerSettings['Freq'] = centre_frequency
            else:
                self._block.MixerSettings['Freq'] = -centre_frequency
        else:
            if self._block_type == 'adc':
                self._block.MixerSettings['Freq'] = -centre_frequency
            else:
                self._block.MixerSettings['Freq'] = centre_frequency
        self._block.UpdateEvent(1)
        
        
class SpectrumAnalyser:
    """A wrapper class to hold the SpectrumPlot, Processor, and
    FrequencySelector.
    
    Attributes
    ----------
    spectrum_plot: the SpectrumPlot object.
    
    frequency_selector: the FrequencySelector object.

    """
    
    def __init__(self, channel, sample_frequency, number_samples,
                 title, height, width):
        """SpectrumAnalyser constructor"""

        self.spectrum_plot = SpectrumPlot(
            sample_frequency=sample_frequency,
            number_samples=number_samples,
            centre_frequency=round(
                abs(channel.adc_block.MixerSettings['Freq']))*1e6,
            title=title,
            height=height,
            width=width)

        self._spectrum_processor = SpectrumProcessor(
            channel=channel,
            sample_frequency=sample_frequency,
            number_samples=number_samples)
        
        self.frequency_selector = FrequencySelector(
            block=channel.adc_block)
        
        self._data = None
        self.update_spectrum()

    def update_spectrum(self):
        """Retrieve new spectrum data and update the plot.
        """
        self._data = self._spectrum_processor.get_spectrum()
        self.spectrum_plot.update_plot(self._data)
        
    def get_spectrum(self):
        """Get the data currently on the spectrum plot.
        """
        return self._data

    
class ToneGenerator:
    """A wrapper class to hold the FrequencySelector and
    Amplitude Controller
    
    Attributes
    ----------
    
    frequency_selector : the FrequencySelector object
    amplitude_controller : the AmplitudeController IP Class
    
    """
    
    def __init__(self,
                 channel):
        """ToneGenerator constructor"""
        self.frequency_selector = FrequencySelector(block=channel.dac_block,
                                                    block_type='dac')
        self.amplitude_controller = channel.amplitude_controller

