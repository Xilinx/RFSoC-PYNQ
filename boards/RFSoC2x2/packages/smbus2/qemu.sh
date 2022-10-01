#! /bin/bash
# Copyright (C) 2021 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

. /etc/environment
for f in /etc/profile.d/*.sh; do source $f; done

python3 -m pip install smbus2
