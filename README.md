# RFSoC 4x2 Kit
This repository contains the source code and build scripts for the RFSoC 4x2 *base* design. The design files in this repository are compatible with Xilinx Vivado 2020.2, and PYNQ v2.7.0 and later.

A prebuilt PYNQ image for the RFSoC 4x2 can be downloaded at the [PYNQ website](http://www.pynq.io/board.html). Users can find the RFSoC 4x2 Vivado board files at the [Real Digital website](https://www.realdigital.org/). View the *RFSoC and PYNQ webpage* for more information on the RFSoC 4x2 platform [www.rfsoc-pynq.io](http://www.rfsoc-pynq.io/).

<p align="center">
  <img src="./rfsoc_4x2.png" />
</p>

## Steps to rebuild the base overlay (Ubuntu 18.04/20.04)

1. Ensure that Vivado is sourced using the command below. Change `<tool_path>` to the location of the tool installation.

	```bash
	source <tool_path>/Vivado/2020.2/settings64.sh
	```

2. Clone this repository by running the following in the .tcl command window (replace `<local_path>` with an address location):

	```bash
	export RFSoC4x2_REPO=<local_path>
	git clone https://github.com/Xilinx/RFSoC4x2-PYNQ.git $RFSoC4x2_REPO
	```

3. Finally, run the commands below to rebuild the base overlay:

	```bash
	cd $RFSoC4x2_REPO/board/RFSoC4x2/base
	make
	```

## Steps to rebuild the PYNQ SD card image (Ubuntu 18.04/20.04)

1. Open a new terminal window. Clone this repository by running the following commands (replace `<local_path>` with an address location):

	```bash
	export RFSoC4x2_REPO=<local_path>
	git clone --recurse-submodules https://github.com/Xilinx/RFSoC4x2-PYNQ.git $RFSoC4x2_REPO
	```
	
2. Download the RFSoC 4x2 Board Support Package (BSP) from the [Real Digital website](https://www.realdigital.org/). Move the BSP into the RFSoC 4x2 board folder within the repository. For example:

	```bash
	mv /home/<user_name>/Downloads/RFSoC4x2.bsp $RFSoC4x2_REPO/board/RFSoC4x2/RFSoC4x2.bsp
	```
	
3. Download the [board agnostic PYNQ v2.7 image](https://bit.ly/pynq_aarch64_2_7) and download the [PYNQ 2.7 source distribution tarball](https://github.com/Xilinx/PYNQ/releases/download/v2.7.0/pynq-2.7.0.tar.gz). Create new environment variables for the location of each download. For example:

	```bash
	export ROOTFS_IMAGE=/home/<user_name>/Downloads/focal.aarch64.2.7.0_2021_11_17.tar.gz
	export SDIST_TAR=/home/<user_name>/Downloads/pynq-2.7.0.tar.gz
	```
	
4. Ensure that Vivado and PetaLinux 2020.2 are sourced using the commands below. Change `<tool_path>` to the location of the tool installation. Note, that the terminal must also be configured to use a bash shell.

	```bash
	source <tool_path>/Vivado/2020.2/settings64.sh
	source <tool_path>/PetaLinux/2020.2/bin/settings.sh
	```
	
5. Finally, change directory into the SD builds folder, which is inside the PYNQ repository. Then run the PYNQ build process by executing a make command. You may require super user privileges during the execution of the make command. When the build process is completed, the RFSoC 4x2 PYNQ image will be named `RFSoC4x2-2.7.0.img` and stored in the `PYNQ/sdbuild/output/` folder.

	```bash
	cd $RFSoC4x2_REPO/PYNQ/sdbuild/
	make BOARDDIR=$RFSoC4x2_REPO/board PYNQ_SDIST=$SDIST_TAR PREBUILT=$ROOTFS_IMAGE BOARDS=RFSoC4x2
	cd $RFSoC4x2_REPO/PYNQ/sdbuild/output/
	```

---
Copyright (C) 2022 Xilinx, Inc

SPDX-License-Identifier: BSD-3-Clause

