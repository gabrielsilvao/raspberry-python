import adafruit_dht
import time
import logging
import board
from influxdb import InfluxDBClient

sensor = adafruit_dht.DHT11(board.D4)

client = InfluxDBClient(host='localhost', port=8086, username='grafana', password='seletiva39', ssl=False, verifiy_ssl=False)

temp = sensor.temperature
humi = sensor.humidity

logging.basicConfig(filename='temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)

while True:
    logging.info('Temp=%.2f C and Humidity=%.2f' % (temp,humi))
