#!/bin/bash
# Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: BSD-3-Clause

set -e
set -x

target=$1
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

sudo cp -r $script_dir/package $target/root/rfsystem_build
