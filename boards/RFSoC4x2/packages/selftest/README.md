# RFSoC4x2 Self-test Package

This package installs `pynq-selftest`, a headless CLI script that verifies a
booted RFSoC4x2 PYNQ image (image-level checks plus base-overlay peripheral
checks).


## Running

Run it on the board as root:

```bash
sudo pynq-selftest
```

Results are printed to the terminal and saved to
`/tmp/pynq-selftest.<timestamp>.log`. The script exits non-zero if any check
fails, so it can also be used in automated bring-up. Pass `--no-peripherals` to
run only the software/image checks and skip the base-overlay hardware checks.

Checks whose hardware is absent are reported as `[SKIP]`, not `[FAIL]`.

The self-test is added automatically by the PYNQ SD build flow via the
`RFSoC4x2.spec` `STAGE4_PACKAGES` list (entry `selftest`).

## What is tested

Image-level checks (no external hardware needed), tests `[1]`–`[18]`: root
filesystem auto-resize, global IPv4, CMA pool (~512 MB), Jupyter on `:9090`, XRT
device open, PYNQ overlay + DMA allocate, no unexpected failed units, image
identity (`PynqLinux`), `xilinx` user/groups, notebook delivery, serial
autologin, merged-/usr, base-config patches, sysfs GPIO, pybind11 compile,
internet connectivity, overlay download + install (`rfsoc_sam`), and that
`arduino`/`rpi`/`logictools` are dropped.

Board-specific checks, tests `[19]`–`[30]`:

* **`[19]` Pmod/Grove MicroBlaze firmware** — the prebuilt `pmod_*.bin` are present.
* **`[20]` RFSoC Python stack** — `xrfclk`, `xrfdc`, `xsdfec`, `rfsystem` import.
* **`[21]` LMK clock-control GPIO** — resolves the EMIO gpiochip base at runtime
  (matching `ff0a0000.gpio`, never hardcoded) and opens the LMK reset/clk-sel lines.
* **`[22]` PMBus power rails** — reads the on-board rails via `get_rails()` and
  checks each is within ±10% of its nominal voltage.
* **`[23]` LEDs / buttons / switches** — reads all switches/buttons and toggles LEDs.
* **`[24]` RGB LEDs** — cycles both on-board RGB LEDs.
* **`[25]` RF reference clocks** — `init_rf_clks()` programs the LMK04828 + LMX2594.
* **`[26]` RF-DC radio hierarchy** — reads the `base.radio` tx/rx channel descriptions.
* **`[27]` CMAC 100G** — a DMA round-trip through the CMAC's internal loopback.
* **`[28]` On-board OLED** — initialises the OLED and writes text.
* **`[29]` PMODA MicroBlaze IOP** — compiles and boots a program on the Pmod IOP.
* **`[30]` USB webcam** — captures a frame from `/dev/video0`; skipped if absent.

Tests `[23]`–`[30]` program `base.bit` and exercise the base-overlay peripherals;
`[21]`–`[22]` run before the overlay is loaded so they do not disturb the RF
clock configuration.

----

Copyright (C) 2022 Xilinx, Inc
Copyright (C) 2022-2026 Advanced Micro Devices, Inc

SPDX-License-Identifier: BSD-3-Clause
