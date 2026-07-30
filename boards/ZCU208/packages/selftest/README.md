# ZCU208 Self-test Package

This package installs `pynq-selftest`, a headless script that verifies a booted
ZCU208 PYNQ (RFSoC) image. Run it on the board as root:

```bash
sudo pynq-selftest
```

Results are printed to the terminal and saved to
`/tmp/pynq-selftest.<timestamp>.log`. The script exits non-zero if any check
fails, so it can also be used in automated bring-up.

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

Base-overlay hardware checks — `base.bit` is programmed once (`[12]`), then each
peripheral runs as its own numbered, timeout-guarded sub-test with step-by-step
logging (so a hang trips the per-test timeout and is reported as `FAIL` with the
stalled step in the log, instead of blocking the run):

* **`[12]` Base overlay load** — programs the PL with `base.bit`.
* **`[13]` PL DDR4** — write/read verify of the `DSPmemory/DSPddr4` region.
* **`[14]` SFP (25G XXV Ethernet + AXI DMA)** — a DMA round-trip through the
  MAC's **internal** loopback. Passes with or without a physical SFP loopback
  module. To additionally validate the optical/copper path, fit an external
  loopback (see below) and set `ctl_local_loopback = 0`.
* **`[15]` LEDs / push-buttons / DIP switches** — reads all switches/buttons and
  toggles an LED via the overlay GPIO drivers.
* **`[16]` USB webcam** — captures a frame from `/dev/video0`; skipped if no
  camera is connected.

Checks whose hardware is absent are reported as `[SKIP]`, not `[FAIL]`.

## Hardware setup

For the fullest coverage, before running the self-test:

1. Insert the SD card with the image and set the boot mode switch to SD.
2. Connect the USB-UART (J2) to your PC for the serial console (optional).
3. Connect an Ethernet cable (needed for tests 2, 7, 8).
4. (optional) Plug a **USB webcam** into the USB host port to exercise test 12's
   webcam check.
5. (optional) Fit an **SFP+ loopback module** in the upper-right cage (SFP00) to
   validate the external transceiver path; the default internal-loopback test
   needs no module.
6. (optional, for the RF notebooks) Fit SMA loopbacks between the DAC and ADC
   SMAs as described in the `rfdc` notebooks; the self-test itself does not
   require RF loopback.
7. Connect the power supply and power on.

## Adding the package to the SD build

The self-test is added automatically by the PYNQ SD build flow via the
`ZCU208.spec` `STAGE4_PACKAGES` list (entry `selftest`). No manual step is
required for images produced by this repository.
