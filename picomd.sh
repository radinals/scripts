#!/bin/env bash

opt="$1"

if [ -f "/tmp/picomd.lock" ]; then
    echo "picomd lock found..."

    if [ "$opt" = "-F" ]; then
        echo "overriding.."
    elif [ "$opt" = "-R" ]; then
        echo "resetting.."
        rm -f /tmp/picomd.lock
        echo "exiting..."
        exit 0
    else
        echo "exiting..."
        exit 1
    fi

fi

touch "/tmp/picomd.lock"

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

rm -f /tmp/picomd.lock
exit 0
