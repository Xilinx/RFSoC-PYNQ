overlay_name := bsp

.PHONY: all board_files bsp clean

all: board_files bsp
	@echo
	@tput setaf 2 ; echo "Built $(overlay_name) successfully!"; tput sgr0;
	@echo

board_files:
	wget "https://www.realdigital.org/downloads/9d2af32116d5420d25da904f6a06bb1f.zip" -O bf.zip && \
	unzip bf.zip -d board_files && rm bf.zip

bsp:
	vivado -mode batch -source bsp.tcl -notrace

clean:
	rm -rf bsp *.jou *.log NA .Xil bsp.xsa
