#!/usr/bin/env python

import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# using GPIO 4 as the relay 1 output

chan_list = [4]
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)

GPIO.output(4, 0)

#EOF
