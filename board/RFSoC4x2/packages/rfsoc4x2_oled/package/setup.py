# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import find_packages, setup

setup(
    name="rfsoc4x2",
    version='1.0',
    author_email="pynq_support@xilinx.com",
    package_data={
        '': ['*.py', '*.so'],
    },
    packages=find_packages(),
    description="A package to control OLEDs")
