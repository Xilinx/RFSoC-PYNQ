# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

ARCH_RFSoC4x2 := aarch64
BSP_RFSoC4x2 := RFSoC4x2.bsp
BITSTREAM_RFSoC4x2 := 
FPGA_MANAGER_RFSoC4x2 := 1

STAGE4_PACKAGES_RFSoC4x2 := pynq xrt_zocl usbgadget ethernet smbus2 
STAGE4_PACKAGES_RFSoC4x2 += sensorconf boot_rfsoc4x2
STAGE4_PACKAGES_RFSoC4x2 += xrfclk xrfdc xsdfec rfsystem
STAGE4_PACKAGES_RFSoC4x2 += tics rfsoc4x2_oled rfsoc_sam
