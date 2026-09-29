![pynq_logo](https://github.com/Xilinx/PYNQ/raw/master/logo.png)

This repository contains the source code and build scripts for the RFSoC-PYNQ base design and SD card images. The design files in this repository are compatible with AMD Vivado 2025.2, and PYNQ v4.0 and later.

Currently, the ZCU111, ZCU208, and RFSoC4x2 platforms are supported.

## Getting started

Visit the [RFSoC-PYNQ webpage](https://www.rfsoc-pynq.io/) for complete documentation on boards supported, features unique to RFSoC platforms and how to get support.


## Image rebuilding steps

For optional image rebuilding for any of the boards, you will need Docker and Vivado/Vitis 2025.2 on the host. AMD tools stay on the host; the image is built inside the PYNQ sdbuild container. For host setup instructions see the PYNQ [sdbuild readme](https://github.com/Xilinx/PYNQ/tree/pynq-next/sdbuild).

1. Clone this repository
	
	```bash
	git clone --recursive https://github.com/Xilinx/RFSoC-PYNQ.git
	```

2. To rebuild the SD card image, run
	
	```
	make BOARD=<BOARD>
	```

	The image is written as `<BOARD>-4.0.0.img`.

	To rebuild a PYNQ.remote image instead:

	```
	make pynqremote BOARD=<BOARD>
	```

	The remote image is written as `<BOARD>-4.0.0-remote.img`. See the PYNQ [PYNQ.remote documentation](https://pynq.readthedocs.io/en/latest/pynq_remote.html).

## Rebuilding the Base Overlay

To only rebuild the base overlay for a given board, make sure the Vivado tools are sourced and located on `$PATH`, then run

```
cd boards/<BOARD>/base
make
```

---
Copyright (C) 2022 Xilinx, Inc

Copyright (C) 2022-2026 Advanced Micro Devices, Inc

SPDX-License-Identifier: BSD-3-Clause

