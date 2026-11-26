#   Copyright (C) 2026 Advanced Micro Devices, Inc.
#   SPDX-License-Identifier: BSD-3-Clause

import pynq
import pynq.lib
import rfsystem
import xrfclk


class BaseOverlay(pynq.Overlay):
    """ZCU216 base overlay with four RF receive and transmit channels.

    The overlay provides eight red LEDs, five pushbuttons, eight switches,
    PL DDR4 memory and an SFP Ethernet offload engine.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_loaded():
            self.leds = self.leds_gpio.channel1
            self.leds.setdirection('out')
            self.leds.setlength(8)
            self.buttons = self.btns_gpio.channel1
            self.buttons.setdirection('in')
            self.buttons.setlength(5)
            self.switches = self.sws_gpio.channel1
            self.switches.setdirection('in')
            self.switches.setlength(8)

    def init_rf_clks(self, lmk_freq=245.76, lmx_freq=491.52):
        """Initialize the CLK104 LMK and LMX reference clocks, in MHz."""
        if self.device.has_capability('REMOTE'):
            xrfclk.set_ref_clks(lmk_freq=lmk_freq, lmx_freq=lmx_freq,
                               device=self.device)
        else:
            xrfclk.set_ref_clks(lmk_freq=lmk_freq, lmx_freq=lmx_freq)
