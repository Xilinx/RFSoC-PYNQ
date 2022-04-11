#!/bin/bash
# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

set -e
set -x

target=$1
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ ! -z ${RFSOC_SAM} ]; then
	sudo cp -rf ${RFSOC_SAM} $target/root/rfsoc_sam_build
fi
