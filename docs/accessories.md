---
layout: default
---

# Accessories

The accessories on this page are primarily for the RFSoC 4x2 and 2x2. 

The RFSoC 2x2 and 4x2 kits come with a Micro SD card, a Micro USB 3.0 cable, a power supply and two SMA cables. Other optional accessoriescan be used including RF antennas, filters and amplifiers, as described below. 

## Included accessories

### SD Card

A 16GB SD card is included with the kit.

If you need to make a new PYNQ image, the recommended Micro SD card size for PYNQ is 8GB. We recommend you use a 16GB or greater *branded/high quality* SD card. A larger capacity card will allow you to install more packages and overlays and save more data to the card. 

A branded card, or a higher quality card is likely to be more reliable and higher speed cards will be faster to burn, and may give some (modest) performance increase when using your board. 

### RFSoc 4x2 Power supply

A 12V x 10A (120W) power supply is included. 

Barrel jack:
* Centre positive
* 5.4mm (outer radius)
* 21.mm (inner radius)


### Micro USB 3.0 Cable

A composite USB 3.0 cable is used as a USB *Ethernet gadget* between your computer and the board. *Ethernet Gadget* supports Ethernet over USB using the [Remote Network Driver Interface Specification (RDNIS)](https://en.wikipedia.org/wiki/RNDIS) protocol. You can replace this cable with any compatible USB 3.0 A to Micro B cable. 

The Micro USB 3.0 port is backward compatible with USB 2.0 cables. You can use a Micro USB (2.0) cable and connect it to the left side of the USB composite port on the board. 

USB 3.0 is faster than USB 2.0, but for Ethernet Gadget the performance difference may not be significant. 

### SMA cables

2x RF cables with SMA connectors are included with the board and are mainly intended for loopback testing or connecting to other equipment. You can use other compatible SMA cables as required.  

## Recommended RF accessories

### Antenna

When selecting an antenna, be aware of its operational frequency range and the requirements of the target application. Below, are off-the-shelf suggestions of antennas you can use with your board.

* [Nooelec RaTLSnake](https://www.nooelec.com/store/sdr/sdr-addons/antennas/ratlsnake-m6.html)
    * Brand: NooElec
    * Frequency Range: 100-800MHz, 700-1200MHz, 1100-1800MHz
    * Style: Tilt / Swivel, Telescopic
    * Applications: UHF, DVB-T/T2

* [ANT500 Telescopic Antenna](https://www.nooelec.com/store/sdr/sdr-addons/antennas/ant500.html)
    * Brand: NooElec
    * Frequency Range: 75 MHz to 1 GHz
    * Style: Tilt / Swivel, Telescopic
    * Applications: AM/FM Radio

* [ANT-2.4-LCW-SMA](https://linxtechnologies.com/wp/product/lcw-series-low-cost-2-4ghz-dipole-antenna/)
    * Brand: Linx Technologies
    * Frequency Range: 2400 MHz to 2500 MHz
    * Style: Tilt / Swivel
    * Applications: WiFi, Bluetooth&trade;, ZigBee&trade;, Thread&trade;

### Filters

There are a wide range of filters available for the RFSoC. The primary purpose of external filtering is to suppress unwanted signals and extract your band of interest. When selecting a filter, you should also consider the RFSoC's Nyquist Zone properties, and ensure that your filter attenuates neighbouring zones as required by your target application.

* [Mini-Circuits VLF-1800+](https://www.mouser.co.uk/ProductDetail/Mini-Circuits/VLF-1800%2b?qs=xZ%2FP%252Ba9zWqZiMerIBdUJuQ%3D%3D)
    * Brand: Mini-Circuits
    * Frequency Range: DC to 1800 MHz
    * Type: Low Pass Filter
    * Applications: Suitable for suppressing Nyquist Zone 2 on your RFSoC 4x2 development board (when an RF Data Converter's sample rate is ≥ 3600 Msps)

* [Mini-Circuits VBF-2435+](https://www.mouser.co.uk/ProductDetail/Mini-Circuits/VBF-2435+/?qs=xZ%2FP%2Ba9zWqZjJLm3iKqs2g==)
    * Brand: Mini-Circuits
    * Frequency Range: 2340 MHz to 2530 MHz
    * Type: Band Pass Filter
    * Applications: WiFi

### Amplifiers

Signal amplification should be applied carefully to your RFSoC development board. If you are unsure on how to approach signal amplification, please seek professional support, as you may damage your RFSoC development board. Some amplifiers should be cascaded with appropriate attenuation to prevent overvoltage, see [Attenuators](#attenuators) below.

* [VeGA Barebones](https://www.nooelec.com/store/vega-barebones.html)
    * Brand: NooElec
    * Frequency Range: 30 MHz to 4000 MHz
    * Type: Low-Noise Variable Gain Amplifier
    * Control: Manual using digital switches and analogue pot

### Attenuators <a class="anchor" id="attenuators"></a>

You should attenuate your input signal if you are using the VeGA amplifier on the RF ADC front-end. NooElec provide an SMA attenuator kit that will interface to the VeGA and RFSoC development board. We suggest connecting an attenuator of -14dB at the output of the VeGA amplifier (before the RF ADC input). This will convert the output 5V signal to 1V, (suitable for the RFSoC 2x2 and 4x2).

* [SMA Attenuator Kit](https://www.nooelec.com/store/sdr/sdr-addons/attenuators/attenuator-bundle.html)
    * Brand: NooElec
    * Frequency Range: DC - 6 GHz
    * Attenuation Range: 1 dB to 42 dB

## Recommended Ethernet offload accessories

The RFSoC 4x2 also has a QSFP28 port that can be used to offload data to a different system.

* [100G QSFP28 Passive Loopback Testing Module](https://www.fs.com/products/105548.html?attribute=3853&id=181682) this module can help to verify the QSFP28 without using any other external equipment.

* [100G QSFP28 Passive Direct Attach Copper](https://www.fs.com/products/65897.html?attribute=1426&id=181883) this cable can be used to connect the RFSoC 4x2 to other network equipment.

* [100G QSFP28 Active Optical Cable](https://www.fs.com/products/50172.html?attribute=1786&id=197191) this cable can be used to connect the RFSoC 4x2 to other network equipment.

> **Note: Make sure the transceiver is compatible with your network equipment.**

## Optional Accessories

#### Micro USB (2.0) cable

The RFSoC 2x2 and 4x2 both have a Micro USB UART/JTAG port. A standard Micro USB (2.0) micro B cable is optional and can be connected to this port. You can use this if you need to access a serial terminal on the UART. You can also use JTAG on this cable/port to connect to the board from Vivado to download a bitstream, or for JTAG debug. 

### Ethernet cable

USB Ethernet gadget is the recommended way to connect to the board and use PYNQ. If you do not want to use this, or you have an issue using Ethernet Gadget, you can use an Ethernet cable to connect your computer to your board instead. You can also use an Ethernet cable to connect your board to a network. Any standard Ethernet cable can be used. 

If you connect the board to your network where a DHCP server manages IP addresses, the board can be automatically allocated an IP address. If you want to connect your board directly to your computer, you will need to configure the Ethernet connection on your computer. 

This needs to be done for other boards that use PYNQ via an Ethernet cable. You can follow the same [PYNQ documentation for configuring an Ethernet connection for the ZCU104](https://pynq.readthedocs.io/en/latest/getting_started/zcu104_setup.html#ethernet).

### DisplayPort

A Mini DisplayPort cable (to DisplayPort, or to Mini DisplayPort) can be used to connect a compatible display. The Zynq Ultrascale+ RFSoC DisplayPort controller supports DisplayPort 1.2a. Please check that you have a compatible monitor. A short list of [tested Zynq Ultrascale+ DisplayPort monitors](https://www.xilinx.com/support/answers/68671.html) is available.

#### Display port to HDMI adapter

If you do not have a DisplayPort monitor, you may be able to use a Mini DisplayPort to HDMI adapter. Adapters tend to come in two types - active and passive. Passive adapters are generally not compatible, and it is not guaranteed that all DisplayPort to HDMI adapters will work with the Zynq Ultrascale+ DisplayPort controller. 

For more information and recommended adapters, see this discussion on [supported Zynq Ultrascale+ DisplayPort to HDMI adapters on the Element 14 community forum](https://www.element14.com/community/thread/72867/l/ultra96-v2-mini-dp-to-hdmi-adapter).

### USB devices

You can add standard USB peripherals to your board. E.g. USB webcam, keyboard, mouse, USB WiFi dongles.  

Be aware any USB WiFi or USB Bluetooth devices you connect may interfere with any RF signals you are trying to capture.