# Copyright (C) 2022 Xilinx, Inc
# Copyright (C) 2022-2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

ARCH_ZCU111 := aarch64
BSP_ZCU111 := ZCU111.bsp

REMOTE_PACKAGES_ZCU111 := librfdc xrfclk-tics

STAGE4_PACKAGES_ZCU111 := pynq ethernet xrt xrfclk xrfdc xsdfec
STAGE4_PACKAGES_ZCU111 += smbus2 tics selftest zcu111_sensors
