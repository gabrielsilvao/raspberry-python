import time
import board
import adafruit_dht
import requests

dhtDevice = adafruit_dht.DHT11(board.D17)

while True:
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity

    pload = 'temp,host=localhost value={0}'.format(temperature)
    r = requests.post('http://localhost:8086/write?db=sensor&u=db&p=seletiva39', data=pload)

    pload = 'humi,host=localhost value={0}'.format(humidity)
    r = requests.post('http://localhost:8086/write?db=sensor&u=db&p=seletiva39', data=pload)
    time.sleep(2.0)