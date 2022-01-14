import os
import time
import requests
from gpiozero import CPUTemperature

try:
    while(True):
        cpu = CPUTemperature()
        temp = cpu.temperature
        pload = 'cpu,host=localhost,region=br value={0}'.format(temp)
        r = requests.post('http://localhost:8086/write?db=sensor&u=grafana&p=seletiva39', data=pload)

        gpu = os.popen('echo $(/opt/vc/bin/vcgencmd measure_temp | cut -c 6- | cut -c -4)').read()
        pload2 = 'gpu,host=localhost,region=br value={0}'.format(gpu)
        r2 = requests.post('http://localhost:8086/write?db=sensor&u=grafana&p=seletiva39', data=pload2)

        time.sleep(15)

except KeyboardInterrupt:
    pass