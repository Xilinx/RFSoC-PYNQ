![pynq_logo](https://github.com/Xilinx/PYNQ/raw/master/logo.png)

This repository contains the source code and build scripts for the RFSoC-PYNQ base design and SD card images. The design files in this repository are compatible with Xilinx Vivado 2024.1, and PYNQ v3.1 and later.  

Currently, the ZCU111, ZCU208, and RFSoC4x2 platforms are supported.

## Getting started

Visit the [RFSoC-PYNQ webpage](https://www.rfsoc-pynq.io/) for complete documentation on boards supported, features unique to RFSoC platforms and how to get support.


## Image rebuilding steps

For optional image rebuilding for any of the boards, you will need a Linux (Ubuntu 22.04) host machine, with Vivado and Petalinux 2024.1 installed. For more host setup instructions please see the PYNQ [sdbuild readme](https://github.com/Xilinx/PYNQ/tree/master/sdbuild).


1. Clone this repository
	
	```bash
	git clone --recursive https://github.com/Xilinx/RFSoC-PYNQ.git
	```

1. Copy the BSP (board support package) into the appropriate board folder.

	| Board  | BSP Link |
	| ------------- | ------------- |
	| RFSoC4x2  | [RFSoC4x2_2024.1.bsp](https://github.com/RealDigitalOrg/RFSoC4x2-BSP/raw/refs/heads/master/bsp_releases/RFSoC4x2_2024_1.bsp)  |
	| ZCU208  | [xilinx-zcu208-v2024.1.bsp](https://www.xilinx.com/member/forms/download/xef.html?filename=xilinx-zcu208-v2024.1-05230256.bsp)  |
	| ZCU111  | Link coming soon...  |
	
	```
	cp <local-path-to-bsp> boards/<BOARD>/<BOARD>.bsp
	```

3. To rebuild just the base overlay, run
	
	```
	make BOARD=<BOARD> base
	```
4. To rebuild the SD card image, run
	
	```
	make BOARD=<BOARD> image
	```
---
Copyright (C) 2022 Xilinx, Inc
Copyright (C) 2022-2025 Advanced Micro Devices, Inc

SPDX-License-Identifier: BSD-3-Clause

