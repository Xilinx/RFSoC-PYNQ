# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

ARCH_ZCU216 := aarch64
BSP_ZCU216 := ZCU216.bsp

REMOTE_PACKAGES_ZCU216 := librfdc xrfclk-tics

STAGE4_PACKAGES_ZCU216 := pynq ethernet xrt xrfclk xrfdc xsdfec
STAGE4_PACKAGES_ZCU216 += smbus2 rfsystem tics selftest
