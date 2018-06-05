#!/usr/bin/env python

import sys
import RPi.GPIO as GPIO

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


if sys.argv[1] == '1':
	output_pin = 4
if sys.argv[1] == '2':
	output_pin = 17
if sys.argv[1] == '3':
	output_pin = 27
if sys.argv[1] == '4':
	output_pin = 22
if sys.argv[1] == '5':
	output_pin = 5
if sys.argv[1] == '6':
	output_pin = 6
if sys.argv[1] == '7':
	output_pin = 13
if sys.argv[1] == '8':
	output_pin = 19
if sys.argv[1] == '9':
	output_pin = 26
if sys.argv[1] == '10':
	output_pin = 23
if sys.argv[1] == '11':
	output_pin = 24
if sys.argv[1] == '12':
	output_pin = 25
if sys.argv[1] == '13':
	output_pin = 12
if sys.argv[1] == '14':
	output_pin = 16
if sys.argv[1] == '15':
	output_pin = 20
if sys.argv[1] == '16':
	output_pin = 21





if sys.argv[2] == 'on':
	output_relay = 0 # because it's backwards binary
else:
	if sys.argv[2] == 'off':
		output_relay = 1 # because it's backwards binary
	else:
		print "error"

GPIO.output(output_pin, output_relay)

#EOF
