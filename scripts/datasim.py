#! /usr/bin/python


# https://pypi.python.org/pypi/paho-mqtt/1.1
import paho.mqtt.client as mqtt
import time
from random import randint
import json

def on_connect(client, userdata, flags, rc):
    print('connected')

def on_publish(client, userdata, mid):
    print('published')

def generate_telemetry():
    telemetry = {}
    telemetry['altitude'] = randint(0, 100)
    telemetry['power'] = randint(0, 100)
    telemetry['temperature'] = randint(0, 100)
    telemetry['latitude'] = randint(27000000, 29000000) / 1000000.0
    telemetry['longitude'] = randint(-82000000, -80000000) / 1000000.0
    telemetry['eventCode'] = randint(0, 15)
    return telemetry


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
#client.on_message = on_message
client.connect('localhost', 1883, 60)
#client.loop_start()
while True:
    # generate random data
    try:
        time.sleep(0.5)
        client.loop(0.01)
        tjson = json.dumps(generate_telemetry())
        print(tjson)
        client.publish('telemetry', payload=tjson, qos=0, retain=True)
    except KeyboardInterrupt:
        #client.loop_stop()
        print('disconnecting...')
        break
client.disconnect()