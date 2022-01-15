from flask import Flask, jsonify
import adafruit_dht
import board
import subprocess

sensor = adafruit_dht.DHT11(board.D4)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return 'Hello World!'

@app.route('/remote_sensor', methods=['GET'])
def temp():
    temp = sensor.temperature
    humi = sensor.humidity
    resultado =  {
        "temp": temp,
        "humidity": humi
    }
    return jsonify(resultado)

app.run(host='0.0.0.0')