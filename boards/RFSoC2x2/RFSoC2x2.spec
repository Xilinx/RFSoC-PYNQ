# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

ARCH_RFSoC2x2 := aarch64
BSP_RFSoC2x2 :=
BITSTREAM_RFSoC2x2 := base/base.bit
FPGA_MANAGER_RFSoC2x2 := 1

STAGE4_PACKAGES_RFSoC2x2 := pynq xrt_zocl usbgadget ethernet smbus2
STAGE4_PACKAGES_RFSoC2x2 += sensorconf boot_leds
STAGE4_PACKAGES_RFSoC2x2 += xrfclk xrfdc xsdfec rfsystem rfsoc_sam
