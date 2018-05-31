#!/bin/bash

rm -rf /tmp/2waypipe
mkfifo /tmp/2waypipe

while true
do
	./netcat-processing.sh 0</tmp/2waypipe | nc -l 1234 1>/tmp/2waypipe
done
