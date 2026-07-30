#! /bin/bash
# Copyright (C) 2021 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

target=$1
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

sudo install -D -m 0755 "$script_dir/pynq-selftest" "$target/usr/local/bin/pynq-selftest"
