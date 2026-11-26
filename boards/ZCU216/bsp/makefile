# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

.PHONY: all clean
all: bsp.xsa

bsp.xsa: bsp.tcl
	vivado -mode batch -source bsp.tcl -notrace

clean:
	rm -rf bsp *.jou *.log NA .Xil bsp.xsa
