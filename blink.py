#!/usr/bin/python

import machine
import utime

for i in range(30):
    led = machine.Pin(i, machine.Pin.OUT)
    led.toggle()
    print("led: ", i)
    utime.sleep(1)
    led.toggle()