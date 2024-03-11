#!/bin/env bash

battery_num=1

battery_info="/sys/class/power_supply/BAT$battery_num"
[ ! -d "$battery_info" ] && exit 1

while [[ true ]]; do

    battery_status="$(cat "$battery_info/status")"
    grep -q -o "Discharging" <<< "$battery_status" && [ "$(pgrep picom)" ] && killall picom >/dev/null
    grep -q -o "Not charging" <<< "$battery_status" || grep -q -o "Charging" <<< "$battery_status" && [ ! "$(pgrep picom)" ] && exec picom -b >/dev/null &

    sleep 60s

done
