#!/bin/sh

if [ -f ~/.openwrt ]; then

    if [ `wifi status radio0 | grep "\"up\": false"` ]; then
        echo "`date` [0]" >> /var/log/wifi_up
        wifi
        /root/beep.sh
    fi

    if [ `wifi status radio1 | grep "\"up\": false"` ]; then
        echo "`date` [1]" >> /var/log/wifi_up
        wifi
        /root/beep.sh
    fi

else
    echo "???"
fi