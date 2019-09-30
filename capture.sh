#!/bin/bash

while [ 1 ]
do
DATE=$(date +"%Y-%m-%d_%H%M%S")

fswebcam -r 640x480 --no-banner /home/pi/images/$DATE.jpg
sleep 0.8
done
