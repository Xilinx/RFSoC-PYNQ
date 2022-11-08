############################################################################
##  Copyright (C) 2021 Xilinx, Inc
##  SPDX-License-Identifier: BSD-3-Clause
##
##  RFSoC2x2 Rev1.1 - Minimal XDC 11/09/2020
##
##  Includes:
##  Display Port
##
############################################################################

# display port
set_property PACKAGE_PIN AF19     [get_ports "dp_aux_data_in"]
set_property PACKAGE_PIN AF20     [get_ports "dp_aux_data_oe[0]"]
set_property PACKAGE_PIN AG18     [get_ports "dp_aux_data_out"]
set_property PACKAGE_PIN AH18     [get_ports "dp_hot_plug_detect"]
set_property IOSTANDARD LVCMOS18  [get_ports "dp_hot_plug_detect"]
set_property IOSTANDARD LVCMOS18  [get_ports "dp_aux_data_out"]
set_property IOSTANDARD LVCMOS18  [get_ports "dp_aux_data_oe[0]"]
set_property IOSTANDARD LVCMOS18  [get_ports "dp_aux_data_in"]
