#   Copyright (C) 2026 Advanced Micro Devices, Inc.
#   SPDX-License-Identifier: BSD-3-Clause

from setuptools import find_packages, setup


setup(
    name="rfsystem",
    version='1.0',
    author="David Northcote",
    author_email="pynq_support@xilinx.com",
    packages=find_packages(),
    description="A radio hierarchy system for RFSoC.")
