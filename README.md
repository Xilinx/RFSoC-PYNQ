# RFSoC 4x2 Kit
This repository contains the source code and build scripts for the RFSoC 4x2 *base* design. The design files in this repository are compatible with Xilinx Vivado 2020.2, and PYNQ v2.7.0 and later.

A prebuilt PYNQ image for the RFSoC 4x2 can be downloaded at the [PYNQ website](http://www.pynq.io/board.html). Users can find the RFSoC 4x2 Vivado board files at the [Real Digital website](https://www.realdigital.org/). View the *RFSoC and PYNQ webpage* for more information on the RFSoC 4x2 platform [www.rfsoc-pynq.io](http://www.rfsoc-pynq.io/).

<p align="center">
  <img src="./rfsoc_4x2.png" />
</p>

## Steps to rebuild the base overlay and sd card image

1. Ensure that Vivado and PetaLinux 2020.2 are sourced using the commands below. Change `<tool_path>` to the location of the tool installation. Note, that the terminal must also be configured to use a bash shell.

	```bash
	source <tool_path>/Vivado/2020.2/settings64.sh
	source <tool_path>/PetaLinux/2020.2/bin/settings.sh
	```

2. Clone this repository

	```bash
	git clone https://github.com/Xilinx/RFSoC4x2-PYNQ --recursive
	```

3. To rebuild just the base overlay, run

	```
	make base
	```

4. To rebuild the image, run

	```
	make image
	```

---
Copyright (C) 2022 Xilinx, Inc

SPDX-License-Identifier: BSD-3-Clause

