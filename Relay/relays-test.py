#!/usr/bin/env python

import sys
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#chan_list = [4,5,6,17,27,22,13,19,26,23,24,25,12,16,20,21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) # relay 1
GPIO.setup(17, GPIO.OUT) # relay 2
GPIO.setup(27, GPIO.OUT) # relay 3
GPIO.setup(22, GPIO.OUT) # relay 4
GPIO.setup(5, GPIO.OUT) # relay 5
GPIO.setup(6, GPIO.OUT) # relay 6
GPIO.setup(13, GPIO.OUT) # relay 7
GPIO.setup(19, GPIO.OUT) # relay 8
GPIO.setup(26, GPIO.OUT) # relay 9
GPIO.setup(23, GPIO.OUT) # relay 10
GPIO.setup(24, GPIO.OUT) # relay 11
GPIO.setup(25, GPIO.OUT) # relay 12
GPIO.setup(12, GPIO.OUT) # relay 13
GPIO.setup(16, GPIO.OUT) # relay 14
GPIO.setup(20, GPIO.OUT) # relay 15
GPIO.setup(21, GPIO.OUT) # relay 16

#initialize with All relays off
print('initialize all relays off')

GPIO.output(4, 1)
GPIO.output(17, 1)
GPIO.output(27, 1)
GPIO.output(22, 1)
GPIO.output(5, 1)
GPIO.output(6, 1)
GPIO.output(13, 1)
GPIO.output(19, 1)
GPIO.output(26, 1)
GPIO.output(23, 1)
GPIO.output(24, 1)
GPIO.output(25, 1)
GPIO.output(12, 1)
GPIO.output(16, 1)
GPIO.output(20, 1)
GPIO.output(21, 1)

print(' relay 1 HI, waiting 1 second')
time.sleep(1)
GPIO.output(4, 0)

print('relay 1 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(4, 1)

print('relay 2 HI, waiting 1 second')
time.sleep(1)
GPIO.output(17, 0)

print('relay 2 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(17, 1)

print('relay 3 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(27, 0)

print('relay 3 HI, waiting 1 second')
time.sleep(1)
GPIO.output(27, 1)

print('relay 4 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(22, 0)

print('relay 4 HI, waiting 1 second')
time.sleep(1)
GPIO.output(22, 1)

print('relay 5 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(5, 0)

print('relay 5 HI, waiting 1 second')
time.sleep(1)
GPIO.output(5, 1)

print('relay 6 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(6, 0)

print('relay 6 HI, waiting 1 second')
time.sleep(1)
GPIO.output(6, 1)

print('relay 7 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(13, 0)

print('relay 7 HI, waiting 1 second')
time.sleep(1)
GPIO.output(13, 1)

print('relay 8 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(19, 0)

print('relay 8 HI, waiting 1 second')
time.sleep(1)
GPIO.output(19, 1)

print('relay 9 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(26, 0)

print('relay 9 HI, waiting 1 second')
time.sleep(1)
GPIO.output(26, 1)

print('relay 10 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(23, 0)

print('relay 10 HI, waiting 1 second')
time.sleep(1)
GPIO.output(23, 1)

print('relay 11 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(24, 0)

print('relay 11 HI, waiting 1 second')
time.sleep(1)
GPIO.output(24, 1)

print('relay 12 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(25, 0)

print('relay 12 HI, waiting 1 second')
time.sleep(1)
GPIO.output(25, 1)

print('relay 13 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(12, 0)

print('relay 13 HI, waiting 1 second')
time.sleep(1)
GPIO.output(12, 1)

print('relay 14 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(16, 0)

print('relay 14 HI, waiting 1 second')
time.sleep(1)
GPIO.output(16, 1)

print('relay 15 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(20, 0)

print('relay 15 HI, waiting 1 second')
time.sleep(1)
GPIO.output(20, 1)

print('relay 16 LOW, waiting 1 second')
time.sleep(1)
GPIO.output(21, 0)

print('relay 16 HI, waiting 1 second')
time.sleep(1)
GPIO.output(21, 1)

GPIO.cleanup()
print('cleaned up')


#EOF
