import time
import board
import adafruit_dht
import requests

sensor = adafruit_dht.DHT11(board.D17)

while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.humidity

        pload = 'temp,host=localhost value={0}'.format(temperature)
        r = requests.post('http://localhost:8086/write?db=sensor&u=db&p=seletiva39', data=pload)

        pload = 'humi,host=localhost value={0}'.format(humidity)
        r = requests.post('http://localhost:8086/write?db=sensor&u=db&p=seletiva39', data=pload)
    
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(5)