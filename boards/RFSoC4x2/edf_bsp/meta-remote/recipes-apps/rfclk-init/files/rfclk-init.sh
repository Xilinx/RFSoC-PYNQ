#!/bin/sh
# RFSoC4x2: set the LMK clock-select lines and pulse the LMK reset at boot, via
# the sysfs GPIO interface. Mirrors boards/RFSoC4x2/packages/boot_rfsoc4x2/boot.py
# (the classic on-board boot), which the minimal PYNQ.remote image does not run.

# Find the gpiochip whose realpath contains ff0a0000.gpio and take its base number.
base=
for chip in /sys/class/gpio/gpiochip*; do
    if readlink -f "$chip" | grep -q ff0a0000.gpio; then
        base=${chip##*/gpiochip}
        break
    fi
done
if [ -z "$base" ]; then
    echo "rfclk-init: ff0a0000.gpio gpiochip not found" >&2
    exit 1
fi

reset=$((base + 7))
clk_sel0=$((base + 8))
clk_sel1=$((base + 12))

for gpio in "$reset" "$clk_sel0" "$clk_sel1"; do
    [ -d "/sys/class/gpio/gpio$gpio" ] || echo "$gpio" > /sys/class/gpio/export
    echo out > "/sys/class/gpio/gpio$gpio/direction"
done

# Pulse reset, then select the on-board reference (clk_sel0 = clk_sel1 = 0).
echo 1 > "/sys/class/gpio/gpio$reset/value"
echo 0 > "/sys/class/gpio/gpio$reset/value"
echo 0 > "/sys/class/gpio/gpio$clk_sel0/value"
echo 0 > "/sys/class/gpio/gpio$clk_sel1/value"
