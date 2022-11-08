# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause



from pynq import DefaultIP


class PacketGenerator(DefaultIP):
    """Driver for the Packet Generator core.
    
    The Packet Generator is a simple IP core written in
    VHDL. The core is used to generate AXI-Stream packets
    for interfacing to an AXI DMA. The AXI-Stream packets
    are written to the master AXI-Stream interface when
    requested by the user through the transfer register.
    
    Attributes
    ----------
    packetsize : an int
        The packetsize defines the number of valid samples
        between the start of an AXI-Stream packet and a valid
        tlast strobe. The acceptable range is an int between
        2 and 4096.
        
    transfer : a bool
        The transfer property allows the user to communicate
        with the packet generator, such that an AXI-Stream
        packet of size packetsize, is transferred to the
        master AXI-Stream interface on the rising edge.
    
    """
    
    def __init__(self, description):
        super().__init__(description=description)
        
    bindto = ['xilinx.com:ip:packet_generator:1.0']

    @property
    def packetsize(self):
        """The number of valid samples between the start
        of an AXI-Stream packet and a valid tlast strobe."""
        return self.read(0x00)
    
    @packetsize.setter
    def packetsize(self, packetsize):
        if 2 <= packetsize <= 4096:
            self.write(0x00, packetsize)
        else:
            raise ValueError(
                'Packet size incorrect, should be in range 2 to 4096.')

    @property
    def transfer(self):
        """On the rising edge, transfer an AXI-Stream packet
        to the master AXI-Stream interface."""
        return self.read(0x04)
    
    @transfer.setter
    def transfer(self, transfer):
        if transfer:
            self.write(0x4, int(1))
        else:
            self.write(0x4, int(0))

