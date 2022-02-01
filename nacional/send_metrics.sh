#!/bin/bash

while :
do
    cpu=$(</sys/class/thermal/thermal_zone0/temp)
    cpu=$((cou/1000))
    curl -si -XPOST "http://localhost:8086/write?db=sensor&u=db&p=seletiva39" --data-binary "cpu,host=localhost value=${cpu}" > /dev/null

    gpu=$(/usr/bin/vcgencmd measure_temp | cut -c 6- | cut -c -4)
    curl -si -XPOST "http://localhost:8086/write?db=sensor&u=db&p=seletiva39" --data-binary "gpu,host=localhost value=${gpu}" > /dev/null

    sleep 5
    done