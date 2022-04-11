#! /bin/bash
# Copyright (C) 2021 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

target=$1
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# the current boot.py will overwrite all existing boot.py
sudo cp -rf $script_dir/boot.py $target/boot/boot.py
