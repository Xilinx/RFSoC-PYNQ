#! /bin/bash
# Copyright (C) 2021 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

set -x
set -e

. /etc/environment

dest=$(ls -d /usr/local/share/pynq-venv/lib/python3.*/site-packages/xrfclk 2>/dev/null | head -1)
if [ -z "$dest" ]; then echo "ERROR: xrfclk not found under pynq-venv (xrfclk must be installed first)" >&2; exit 1; fi

cd /root/tics_build
cp -a . $dest

cd /root
rm -rf tics_build
