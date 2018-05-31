#!/bin/bash


# while loop on = process everything for one session, but doesn't restart nc
# while loop off = processes only first line, kills session after 2nd line, but then restarts nc


while true
do
	if read line </tmp/2waypipe
	then
		if [[ "$line" == 'format' ]]
		then
			echo "FORMATTY FORMAT"
		else
			echo $line
		fi
	else
		exit
	fi
done
