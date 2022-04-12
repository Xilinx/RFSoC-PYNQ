# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

set -x
set -e

cd /root/oled_build
make
cp libNHD0216AWSB3.so rfsoc4x2

source /etc/profile.d/pynq_venv.sh
python3 -m pip install .

cd /root
rm -rf oled_build
