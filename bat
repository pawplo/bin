#!/bin/sh

source color
source run

d=`date +%m.%G`

if [ ! -f /root/bat/cycle_count/${d} ]; then
    echo "$0 new cycle_count ${d}"
    run echo `date` ">" /root/bat/cycle_count/${d}
    run cat /sys/class/power_supply/BAT0/cycle_count ">>" /root/bat/cycle_count/${d}
    run cat /sys/class/power_supply/BAT1/cycle_count ">>" /root/bat/cycle_count/${d}
fi;