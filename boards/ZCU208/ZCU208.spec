# Copyright (C) 2022 Xilinx, Inc
# Copyright (C) 2022-2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

ARCH_ZCU208 := aarch64
BSP_ZCU208 := ZCU208.bsp

REMOTE_PACKAGES_ZCU208 := librfdc xrfclk-tics

STAGE4_PACKAGES_ZCU208 := pynq ethernet xrt xrfclk xrfdc xsdfec
STAGE4_PACKAGES_ZCU208 += smbus2 rfsystem tics selftest
