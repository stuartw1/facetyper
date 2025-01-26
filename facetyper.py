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

    # Wait for device to connect
    await asyncio.sleep(2)
    #Input loop
    print("Entering loop. Enter to send. Ctrl+C to exit")#
    while True:
        sendstring = ""
        sendstring = input("Type string to send: ")
        assert type(sendstring) == str, "input should be a String"
        # Type a string with the device
        await device.type_string(sendstring)
    print("Sent: "+sendstring)

print(1)
main(device, type_letters())
