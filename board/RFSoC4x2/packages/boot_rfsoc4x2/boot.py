#!/usr/bin/env python3
# Copyright (c) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

from time import sleep
from pynq.overlays.base import BaseOverlay
from pynq import GPIO
from rfsoc4x2 import oled
import pynq
import subprocess as sp
import netifaces as ni

oled = oled.oled_display()
oled.write("RFSoC-PYNQ\nVersion {}".format(pynq.__version__))

# LMK clock config
lmk_reset = GPIO(345, 'out')
lmk_clk_sel0 = GPIO(346, 'out')
lmk_clk_sel1 = GPIO(350, 'out')

lmk_reset.write(1)
lmk_reset.write(0)
lmk_clk_sel0.write(0)
lmk_clk_sel1.write(0)

base = BaseOverlay('base.bit')

for _ in range(8):
    base.leds[0:4].on()
    sleep(0.2)
    base.leds[0:4].off()
    sleep(0.2)

# Find activate interface name and IP address
iface = ni.gateways()['default'][ni.AF_INET][1]
ip_address = ni.ifaddresses(iface)[2][0]['addr']

oled.write("IP Addr({}):\n{}".format(iface, ip_address))
