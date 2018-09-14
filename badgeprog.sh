#!/bin/bash

enable=3
io0=2

# init GPIO
raspi-gpio set $enable op
raspi-gpio set $io0    op

echo "Putting module into program mode"

raspi-gpio set $enable dl
raspi-gpio set $io0    dl
sleep 1
raspi-gpio set $enable dh
python esptool.py --chip esp32 --port /dev/ttyS0 --baud 460800 write_flash -z --flash_mode dio --flash_freq 40m 0x1000 firmware.bin

sleep 5

echo "Booting Module"
raspi-gpio set $io0    dh
sleep 1
raspi-gpio set $enable dl
sleep 1
raspi-gpio set $enable dh
