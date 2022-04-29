# RFSoC 4x2 Kit
This repository contains the source code and build scripts for the RFSoC 4x2 base design and image. The design files in this repository are compatible with Xilinx Vivado 2020.2, and PYNQ v2.7.0 and later.

Please view the *RFSoC and PYNQ webpage* for more information on the RFSoC 4x2 platform [www.rfsoc-pynq.io](http://www.rfsoc-pynq.io/).

<p align="center">
  <img width=75% src="./rfsoc_4x2.png" />
</p>

## Getting started

1. Simply download the prebuilt PYNQ image for the RFSoC4x2 from the [PYNQ website](http://www.pynq.io/board.html) and burn to SD card using a tool like [balenaEtcher](https://www.balena.io/etcher/).

2. Boot the board with the burned SD card and make sure the board is connected to your device or network.

3. The board launches a Jupyter Lab server on startup which you can access via your browser `http://<board_ip_address>:9090/lab`

4. Explore!

## (optional) Image rebuilding steps

For image rebuilding you will need a Linux (Ubuntu 18.04/20.04) host machine, with Vivado and Petalinux 2020.2 installed. For more host setup instructions please see the PYNQ [sdbuild readme](https://github.com/Xilinx/PYNQ/tree/master/sdbuild.

1. Clone this repository
	
	```bash
	git clone --recursive https://github.com/Xilinx/RFSoC4x2-PYNQ.git
	```
2. To rebuild just the base overlay, run
	
	```
	make base
	```
3. To rebuild the SD card image, run
	
	```
	make image
	```
---
Copyright (C) 2022 Xilinx, Inc

SPDX-License-Identifier: BSD-3-Clause

