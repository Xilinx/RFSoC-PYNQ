# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

OBJSC = oled.o 

all:	
	gcc -fPIC -c -g oled.c
	gcc -shared -fPIC -rdynamic $(OBJSC) -o libNHD0216AWSB3.so
	rm *.o
