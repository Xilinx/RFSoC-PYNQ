# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

ARCH_ZCU111 := aarch64
BSP_ZCU111 := ZCU111.bsp
RFSoC_ZCU111 := 1

STAGE4_PACKAGES_ZCU111 := pynq xrfclk xrfdc xsdfec
STAGE4_PACKAGES_ZCU111 += ethernet zcu111_sensors xrt
