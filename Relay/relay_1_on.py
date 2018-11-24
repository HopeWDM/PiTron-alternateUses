#!/usr/bin/env python

# location:
# /home/production/python/relay_1_on.py

import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# using GPIO 4 as the relay 1 output
# chan_list not necessary but helpful if multiple channels are intialized

chan_list = [4]
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)

# GPIO.output(channel, 0 = on 1 = off)
GPIO.output(4, 0)

#EOF
