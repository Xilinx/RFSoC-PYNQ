# Copyright (C) 2021 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

set overlay_name "base"
set design_name "base"

# open block design
open_project ./${overlay_name}/${overlay_name}.xpr

# generate xsa
write_hw_platform -fixed -include_bit -force -file ./${overlay_name}.xsa
validate_hw_platform ./${overlay_name}.xsa

# move and rename bitstream to final location
file copy -force ./${overlay_name}/${overlay_name}.runs/impl_1/${design_name}_wrapper.bit ${overlay_name}.bit

# copy hwh files
file copy -force ./${overlay_name}/${overlay_name}.gen/sources_1/bd/${design_name}/hw_handoff/${design_name}.hwh ${overlay_name}.hwh
