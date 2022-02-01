#!/bin/bash
while :
do
    gpu="$(/opt/vc/bin/vcgencmd measure_temp | cut -c 6- | cut -c -4)"
    curl -si -XPOST "http://localhost:8086/write?db=sensor&u=grafana&p=seletiva39" --data-binary "gpu,host=localhost,region=br value=${gpu}" > /dev/null

    cpu=$(</sys/class/thermal/thermal_zone0/temp)
    cpu_final=$((cpu/1000))
    curl -si -XPOST "http://localhost:8086/write?db=sensor&u=grafana&p=seletiva39" --data-binary "cpu,host=localhost,region=br value=${cpu_final}" > /dev/null
    sleep 30
done