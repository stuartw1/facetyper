#!/usr/bin/python3

#facetyper.py
#2015 Stuart Walker - https://github.com/stuartw1/facetyper
#License: GPLv2

# Based on https://cynthion.readthedocs.io/en/latest/getting_started_facedancer.html

import asyncio
from facedancer import main
from facedancer.devices.keyboard import USBKeyboardDevice

device = USBKeyboardDevice()

async def type_letters():

    print(2)
    # Wait for device to connect
    await asyncio.sleep(2)
    print(3)
    # Type a string with the device
    await device.type_string("echo hello, facedancer\n")
    print(4)

print(1)
main(device, type_letters())
