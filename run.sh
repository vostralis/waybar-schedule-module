#!/bin/bash

source "$HOME/.config/waybar/waybar-schedule-module/venv/bin/activate"

if [ $1 == "-f" ]; then
    python3 fetch-schedule.py
elif [ $1 == "-d"]; then
    python3 display-schedule.py
fi