#!/bin/bash
# Copyright (c) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

target=$1
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cat $script_dir/boot.py | sudo tee -a $target/boot/boot.py
