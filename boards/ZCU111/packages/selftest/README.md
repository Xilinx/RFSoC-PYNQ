# ZCU111 Self-test Package

This package installs `pynq-selftest`, a headless script that verifies a booted
ZCU111 PYNQ (RFSoC) image. Run it on the board as root:

```bash
sudo pynq-selftest
```

Results are printed to the terminal and saved to
`/tmp/pynq-selftest.<timestamp>.log`. The script exits non-zero if any check
fails, so it can also be used in automated bring-up.

ZCU111 ships without an in-repo base overlay, so the board-specific checks use
StrathSDR's `rfsoc_qpsk` example overlay, which is downloaded and installed as
part of the run.

## What is tested

Image-level checks (no external hardware needed):

1. Root filesystem auto-resize ran.
2. Networking — a global IPv4 address is present.
3. CMA pool is at least ~512 MB.
4. Jupyter server is active and listening on `:9090`.
5. XRT runtime opens an FPGA device (`pyxrt.device(0)`).
6. RFSoC Python stack imports (`xrfclk`, `xrfdc`, `xsdfec`).
7. Internet connectivity (needed to download overlays).
8. Overlay download + install (`rfsoc_qpsk`) and PL programming.
9. No unexpected failed systemd units.
10. Image identity (`PynqLinux 4.0.0`).
11. `xilinx` user exists and is in `sudo`.

Board-specific checks (use the downloaded `rfsoc_qpsk` overlay):

* **RFSoC Python stack** — imports `xrfclk`, `xrfdc`, `xsdfec`.
* **QPSK overlay load** — instantiates `QpskOverlay()`, programming the PL.
* **RF reference clocks** — the overlay configures the LMK04208 + LMX2594
  reference clocks over the SC18IS602 I2C-SPI bridge.
* **Static MAC** — the NIC MAC is globally-administered (a factory MAC read from
  the board EEPROM by u-boot), not a locally-administered random/fallback MAC.

Checks whose hardware is absent are reported as `[SKIP]`, not `[FAIL]`.

## Hardware setup

For the fullest coverage, before running the self-test:

1. Insert the SD card with the image and set the boot mode switch to SD.
2. Connect the USB-UART to your PC for the serial console (optional).
3. Connect an Ethernet cable (needed for tests 2, 7, 8).
4. Connect the power supply and power on.

## Adding the package to the SD build

The self-test is added automatically by the PYNQ SD build flow via the
`ZCU111.spec` `STAGE4_PACKAGES` list (entry `selftest`). No manual step is
required for images produced by this repository.
