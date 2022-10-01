#! /bin/bash
# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

set -x
set -e

. /etc/environment
for f in /etc/profile.d/*.sh; do source $f; done

export HOME=/root
export BOARD=${PYNQ_BOARD}
export PYNQ_JUPYTER_NOTEBOOKS=/home/xilinx/jupyter_notebooks
TAG_VERSION=v0.2.0

cd /root
if [ ! -d "/root/rfsoc_sam_build" ]; then
	git clone https://github.com/strath-sdr/rfsoc_sam rfsoc_sam_build
fi
cd /root/rfsoc_sam_build
python3 -m pip install . --no-deps

cd /root
rm -rf rfsoc_sam_build
