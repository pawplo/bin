#!/bin/sh

if [ -f ~/.openwrt ]; then

w=`wifi status radio0 | grep "\"up\": false"`
if [ "$w" ]; then
    echo "`date` [0]" >> /var/log/wifi_up
    wifi
    /root/beep.sh
fi

w=`wifi status radio1 | grep "\"up\": false"`
if [ "$w" ]; then
    echo "`date` [1]" >> /var/log/wifi_up
    wifi
    /root/beep.sh
fi

else
    echo "???"
fi