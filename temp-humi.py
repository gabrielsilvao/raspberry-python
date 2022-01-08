import adafruit_dht
import time
import board
import json

sensor = adafruit_dht.DHT11(board.D4)

while(1):
   temp = sensor.temperature
   humi = sensor.humidity
   resultado = '{"Temperatura": " %.2f", "Umidade": " %.2f" }' % (temp, humi)
   json_object = json.loads(resultado)
   print(json.dumps(json_object, indent=3))
   time.sleep(2.0)