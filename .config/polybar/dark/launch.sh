#!/usr/bin/env bash

# Add this script to your wm startup file.

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

THEDARKARTS="$HOME/.config/polybar/dark/config.ini"

PATH_TO_CONFIG=$THEDARKARTS

# Launch the bar
if [ "$PATH_TO_CONFIG" = "$THEDARKARTS" ]; then
		polybar -c $PATH_TO_CONFIG main-left &
		polybar -c $PATH_TO_CONFIG main-left-extended &
		polybar -c $PATH_TO_CONFIG main-left-links &
		# polybar -c $PATH_TO_CONFIG main-middle &
		polybar -c $PATH_TO_CONFIG main-right &
		#polybar -c $PATH_TO_CONFIG main-right-extended &
		polybar -c $PATH_TO_CONFIG main-tray &
		polybar -c $PATH_TO_CONFIG main-profile &
	
fi	
