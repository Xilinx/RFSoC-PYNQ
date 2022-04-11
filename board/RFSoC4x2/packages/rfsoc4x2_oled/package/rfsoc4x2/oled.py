# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

import cffi
import os
import warnings

LIB_SEARCH_PATH = os.path.dirname(os.path.realpath(__file__))

_lib_header = R"""
typedef int... u_int8_t;
u_int8_t bitfix (u_int8_t data);
void send_oled_cmd (u_int8_t cmd);
void send_oled_data (u_int8_t data);
void send_oled_str (char *str);
void init (void);
"""

_lib_location = os.path.join(LIB_SEARCH_PATH, "libNHD0216AWSB3.so")


class oled_display:
    """
    This class controls the OLED display found on the RFSoC4x2 board.
    """

    _lib = None
    _ffi = None

    @staticmethod
    def _initialise_ffi():
        oled_display._ffi = cffi.FFI()
        oled_display._ffi.cdef(_lib_header)
        oled_display._lib = oled_display._ffi.dlopen(_lib_location)

    def __init__(self):
        """
        Create new oled_display object.
        """
        if oled_display._lib is None:
            oled_display._initialise_ffi()

        self._lib.init()

    def write(self, text):
        """
        Write a string to the OLED display. The OLED can show 2x16 characters at a time, which means the string shouldn't exceed 32 characters (excluding the newline symbol).
        """
        if len(text.replace("\n", "")) > 32:
            warnings.warn("Message longer than 32 chars")
            
        self._lib.send_oled_str(text.encode())
