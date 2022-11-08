#! /bin/bash
# Copyright (C) 2021 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

set -x
set -e

. /etc/environment

dest=/usr/local/share/pynq-venv/lib/python3.10/site-packages/xrfclk

cd /root/xrfclk-patch

patch $dest/xrfclk.py xrfclk.patch

cd /root
rm -rf xrfclk-patch