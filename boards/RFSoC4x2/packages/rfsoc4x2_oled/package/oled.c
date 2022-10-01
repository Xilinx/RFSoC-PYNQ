/*
 *  Copyright (C) 2022 Xilinx, Inc
 *  SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/spi/spidev.h>

#define OLED_DEV "/dev/spidev1.0"

int oled = 0;

u_int8_t bitfix (u_int8_t data)
/*
 * Routine that corrects the bit positions for the OLED.  This code maps
 * the bits as follows:
 *   D0 -> D7
 *   D1 -> D6
 *   D2 -> D5
 *   D3 -> D4
 * Bits 3 to 0 are set to 0.
 */
{
	int i;
	u_int8_t mask = 0x80;
	u_int8_t result = 0;

	for (i = 0; i < 4; i++) {
		if ((data & 0x01) == 0x01)
			result = result | mask;
		mask = mask >> 1;
		data = data >> 1;
	}
	return result;
}

void send_oled_cmd (u_int8_t cmd)
/*
 * Sends a command to the OLED via SPI.
 */
{
	u_int8_t buf[3];
	int size;

	buf[0] = 0xf8;
	buf[1] = bitfix (cmd & 0x0f);
	buf[2] = bitfix (cmd >> 4);

	size = write (oled, buf, 3);
	if (size != 3)
		printf ("Unable to send OLED command.\n");
	usleep (10000);
}

void send_oled_data (u_int8_t data)
/*
 * Sends a data byte to the OLED via SPI.
 */
{
	u_int8_t buf[3];
	int size;

	buf[0] = 0xfa;
	buf[1] = bitfix (data & 0x0f);
	buf[2] = bitfix (data >> 4);

	size = write (oled, buf, 3);
	if (size != 3)
		printf ("Unable to send OLED data.\n");
	usleep (10000);
}

void send_oled_str (char *str)
/*
 * Routine to send a text string to the OLED display.
 */
{
    int i;
    int current_line = 0;
    
    send_oled_cmd (0x01);
    send_oled_cmd (0x80);
    send_oled_cmd (0x0c);
    usleep (100000);
    
    for (i = 0; i < strlen(str); i++){
        // if end of line, switch to newline
        if ((current_line == 0) && ((i == 16) || (str[i] == '\n'))){
            send_oled_cmd (0xC0);
            current_line = 1;
        }
        // only print non-newline chars
	if (str[i] != '\n')
            send_oled_data ((u_int8_t)str[i]);
    }
}

void init (void)
/*
 * Routine that initializes the OLED display.
 */
{
	u_int8_t data;
	int status;

	oled = open (OLED_DEV, O_RDWR | O_SYNC);
	if (oled < 0) {
		printf ("Unable to open OLED SPI file, error: %d, %s\n",
			errno, OLED_DEV);
		exit (2);
	}

	data = SPI_MODE_3;
	status = ioctl  (oled, SPI_IOC_WR_MODE, &data);
	if (status < 0) {
		printf ("SPI_IOC_WR_MODE failed.\n");
		exit (3);
	}

	data = 8;
	status = ioctl  (oled, SPI_IOC_WR_BITS_PER_WORD, &data);
	if (status < 0) {
		printf ("SPI_IOC_WR_BITS_PER_WORD failed.\n");
		exit (3);
	}
	usleep (100000);

	// Initialize OLED
	send_oled_cmd (0x2a);
	send_oled_cmd (0x71);
	send_oled_data (0x00);
	send_oled_cmd (0x28);
	send_oled_cmd (0x08);
	send_oled_cmd (0x2a);
	send_oled_cmd (0x79);
	send_oled_cmd (0xd5);
	send_oled_cmd (0x70);
	send_oled_cmd (0x78);
	send_oled_cmd (0x08);
	send_oled_cmd (0x06);
	send_oled_cmd (0x72);
	send_oled_data (0x00);
	send_oled_cmd (0x2a);
	send_oled_cmd (0x79);
	send_oled_cmd (0xda);
	send_oled_cmd (0x00);
	send_oled_cmd (0xdc);
	send_oled_cmd (0x00);
	send_oled_cmd (0x81);
	send_oled_cmd (0x7f);
	send_oled_cmd (0xd9);
	send_oled_cmd (0xf1);
	send_oled_cmd (0xdb);
	send_oled_cmd (0x40);
	send_oled_cmd (0x78);
	send_oled_cmd (0x28);
}

