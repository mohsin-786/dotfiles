#! /bin/bash

power=$(cat /sys/class/power_supply/BAT1/status)

while true; do
  actual=$(cat /sys/class/power_supply/BAT1/status)

  if [ $actual != $power ]; then
     power=$actual
     notify-send $actual
  fi
done
