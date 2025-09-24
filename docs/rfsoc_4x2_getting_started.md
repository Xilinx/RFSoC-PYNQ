---
layout: default
---

# Getting started with your RFSoC 4x2

This guide will show you how to setup your computer and RFSoC 4x2 board using PYNQ. 

### Prerequisites 

Included in the kit:

* RFSoC 4x2 board
* Micro SD card (16GB or more recommended)
* Micro USB 3.0 Cable  
* 120W (12V x 10A) power supply for RFSoC 4x2 board

Optional: 

* Micro USB (2.0) cable (for serial terminal)
* Optional: Ethernet cable (for use instead of USB "Ethernet Gadget")

## Setup video

You can watch the getting started video guide or follow the instructions below. If you have any problems getting started, post a question to the [PYNQ support forum](https://discuss.pynq.io).

<iframe width="560" height="315" src="https://www.youtube.com/embed/HMbYNFAhBY4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Setup instructions

### Recommended: Update the Micro SD card with the latest PYNQ image

Your board comes with a Micro SD card, pre-loaded with a PYNQ image. An updated PYNQ image may be available.

* Download the [RFSoC 4x2 latest PYNQ image](https://www.pynq.io/boards.html) and write the image to a Micro SD card

See the PYNQ documentation on [writing an image to an SD card](https://pynq.readthedocs.io/en/latest/appendix/sdcard.html) for more information. 

### Setup the board

Check the following steps to setup the board. 

![](./images/board_setup.png)


1. Insert the Micro SD card (pre-loaded with the RFSoC 4x2 PYNQ image).
2. Set the boot mode switch to the **SD** position.
3. Connect the provided micro B USB 3.0 cable from your computer to the USB 3.0 Composite port of your board, and connect the power cable. 
   Optional: Use an Ethernet cable instead of the USB 3.0 cable to connect your board to your network.
4. Slide the power switch to the right to turn on the board.

### PYNQ Boot sequence

After you power-on the board, you will see the following sequence:

![](./images/boot_sequence.png)

1. The power status LEDs are on the bottom right side of the board. After powering on all 10 power status LEDs will turn on.   

   You may see other LEDs turn on or flash occasionally during boot. E.g. the Ethernet LEDs will flash.

2. After about 40 seconds, you will see the green **DONE** and **INIT** LEDs near the top left of the board turn on. The *DONE* LED turning on indicates a bitstream has been downloaded to the programmable logic and is a good indication that the boot is progressing correctly. 

3. A few seconds later, the 4 white *user LEDs* (LED0-LED3) on the bottom center of the board will flash briefly and remain on. 

4. The OLED will display information about the network connection and IP address of the board. 

   You can now connect to the board.

See the [Troubleshooting section for issues](support.md#troubleshooting), or post questions to the [PYNQ support forum](https://discuss.pynq.io/).

#### Connect to the board

* On your computer, open a web browser. Chrome/Safari/Firefox are recommended for use with Jupyter Lab.

* Browse to [http://192.168.3.1/lab](http://192.168.3.1/lab)
   If you connected your board to your network, replace 192.168.3.1 with the IP address of your board which will be displayed on the OLED
	
The Jupyter Lab log-in screen will load.

![](./images/jupyter_login.png)

* Enter **xilinx** as the password and click **Log in**

You are now in the Jupyter Lab IDE and the PYNQ framework. Use the example notebooks included with PYNQ to start exploring the RFSoC 4x2.

![](./images/jupyter_home.png)

## Accessories

You can find a list of [accessories](accessories.html) that you can use with your RFSoC 4x2 board. 


## Next steps

Review the [overlays](./overlays.html) page for details on available overlays that can be used with your board. Overlays are prepacked PYNQ designs that you can use with your board. 
