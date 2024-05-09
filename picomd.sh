#!/bin/env bash

battery_num=1

battery_info="/sys/class/power_supply/BAT$battery_num"
[ ! -d "$battery_info" ] && exit 1

while true ; do

    battery_status="$(cat "$battery_info/status")"
    if grep -q -o "Discharging" <<< "$battery_status"; then
        [ "$(pgrep picom)" ] && killall picom >/dev/null
    else
        [ ! "$(pgrep picom)" ] && exec picom -b >/dev/null &
    fi

    sleep 60s

done
