#!/bin/bash

set -x
set -e

# Disabling pynq-x11.service due to lack of PS DisplayPort support.
systemctl disable pynq-x11.service
