---
layout: default
---

# Frequently Asked Questions

These FAQ are primarily for the RFSoC 4x2 and 2x2. 

## Can you tell me more about the RFSoC 4x2?

In Feb 2021, the PYNQ team launched the RFSoC 2x2, an exciting new platform for software-defined
radio and instrumentation. However, due to the well-documented interruptions in the global supply
chain, sourcing some parts on the RFSoC 2x2 became increasingly difficult. Our first response to this challenge was to respin
the 2x2 board to use only parts that were more readily available. However, we took this instead
as an opportunity to design a completely new board, the RFSoC 4x2. This new board retains all the best features of the 2x2 while adding the most commonly-requested new features,
especially the most sought after feature - an upgrade to the Zynq UltraScale+ RFSoC Gen 3.


## How does the RFSoC 4x2 compare to the RFSoC 2x2?

The RFSoC 4x2 uses a Gen 3 RFSoC ZU48DR device which dramatically improves the performance of
the RF data converters. Where previously the RF-ADCs converted 12-bit samples at a maximum rate
of 4,096 GSPS, the newer Gen 3 ADCs have an input bandwidth of 6 GHz and can capture 14-bit
samples at 5 Giga-samples per second (GSPS). Meanwhile, the board's RF-DACs output 14-bit samples
at 9.85 GSPS, up from 6.554 GSPS for the Gen 1 parts. As shown on the left-hand side of the board
photo, the RFSoC 4x2 board doubles the number of high-speed ADC ports to four.

The RFSoC also has a dedicated QSFP28 (quad small form factor pluggable) interface. This enables
high-speed data transfer directly between an external host and the Gen 3 device's programmable
logic and RF converter tiles. The compact, hot-swappable QSFP28 interface supports 4x25Gbps,
2x50Gbps or 1x100Gbps Ethernet, depending on the external transceiver chosen by the user.

Other very practical enhancements include a new OLED display which provides boot-time status
information to greatly simplify connecting to the board. Once boot is complete, the OLED display
becomes user programmable.

## Who is the RFSoC 4x2 kit for? 

The RFSoC 4x2 kit has been developed by the PYNQ Team in partnership with Real Digital. It is intended for academic users and only available to universities and research institutes.

## What open-source materials are supplied with the RFSoC 4x2?

The RFSoC 4x2 kit comes with the RFSoC-PYNQ software framework and educational materials
including open-source SDR applications and comprehensive tutorials. RFSoC-PYNQ includes new
reusable designs that target the improved hardware capabilities. For example, the open-source
spectrum analyzer design has been upgraded to operate from DC to 4.915 GHz with an instantaneous
bandwidth of 2.457 GHz. There are also new reusable designs that demonstrate how to perform highspeed
offload over the QSFP28 interface using UDP over Ethernet.

For more details see the [Overlays](./overlays.md), and [Educational resources](./educational_resources.md) sections.

## How to I buy an RFSoC 4x2 board?

The RFSoC 4x2 is manufactured and sold by [Real Digital](https://www.realdigital.org/). The board is only available to academia and to buy the board, academics must first apply
to the [AMD Xilinx University Program](https://www.xilinx.com/support/university/xup-boards/RFSoC4x2.html#Purchasing_at_academic_price)  to get pre-approval to purchase the RFSoC 4x2 kit. and submit a request to purchase the RFSoC 4x2. 

## Who are Real Digital?

Real Digital share our passion to
produce the most capable RFSoC board possible at an exceptional academic price. The company was
founded four years ago by Clint Cole. Some of you will know that Clint previously founded Digilent,
and later sold it to National Instruments. He has a long pedigree of producing excellent development
boards for use in academia.

## How have you made the board more *Open Source*? 

Real Digital have also helped us to deliver on our vision of making the RFSoC 4x2 a more fully open-source
project. So not just the RFSoC-PYNQ framework and design examples but also the board
schematics, bill of materials, and even the PCB Gerber files are available open-source. This will enable
research teams, for example, to use the RFSoC 4x2 as the starting point for developing custom
boards which they may require in their specific research experiments.

To get access to the PCB Gerber files [contact XUP](mailto:xup@xilinx.com).

## Can I still purchase an RFSoC 2x2?

The RFSoC 2x2 board, produced in partnership with High Tech Global, is officially discontinued. No
further units are available for sale.

A small number of reserve units are available for a short period from the AMD Xilinx University
Program in the event that some team has an urgent need. In all other cases, we recommend that
users migrate to the newer and more capable RFSoC 4x2 kits.

## Will support continue for the RFSoC 2x2?

Existing RFSoC 2x2 boards will be supported by the RFSoC-PYNQ framework for the foreseeable
future. Any change in this status will be communicated with a minimum advance notice of 6 months.
Even after new development for the RFSoC 2x2 boards stops, it will be possible to continue using the
last, feature-frozen version of the RFSoC-PYNQ framework and the source software will continue to
be available.


