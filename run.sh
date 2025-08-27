#!/bin/bash

if [ $1 == "-f" ]; then
    $HOME/.config/waybar/waybar-schedule-module/python3 $HOME/.config/waybar/waybar-schedule-module/fetch-schedule.py
elif [ $1 == "-d"]; then
    $HOME/.config/waybar/waybar-schedule-module/python3 $HOME/.config/waybar/waybar-schedule-module/display-schedule.py
fi