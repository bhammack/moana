#! /usr/bin/python
# API mode must be enabled on the XBee device in order to work with this script.

import time
import serial

# https://pypi.python.org/pypi/paho-mqtt/1.1
import paho.mqtt.client as mqtt
# https://pypi.python.org/pypi/XBee
from xbee import XBee


HOSTNAME = "broker.mqttdashboard.com"
PORT = 1883
TELEMETRY_TOPIC = 'telemetry'
CONTROL_TOPIC = 'control'

BAUD_RATE = 9600
SERIAL_ADDR = '/dev/ttyUSB0'

#serial_port = serial.Serial(SERIAL_ADDR, BAUD_RATE);
#xbee = XBee(serial_port, callback=on_telemetry)


def on_connect(client, userdata, flags, rc):
	print("Connected to " + HOSTNAME + ":" + str(PORT))
	client.subscribe(CONTROL_TOPIC)
	
def on_disconnect(client, userdata, rc):
	print("Disconnected from broker with rc:", rc)
	
def on_control(client, userdata, message):
	payload = str(message.payload)
	print(message.topic, payload)
	# send the data to an xbee
	# http://python-xbee.readthedocs.io/en/latest/#sending-data-to-an-xbee-device
	#xbee.send("at", frame='A' command='MY' parameter=None)

def on_telemetry(data):
	# publish the telemetry data to mqtt
	#client.publish(TELEMETRY_TOPIC, '{}', 0, True)
	print(data)
	
print("Initalizing communications relay...")
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.message_callback_add(CONTROL_TOPIC, on_control)
client.connect(HOSTNAME, PORT)


client.loop_start()
#client.loop_forever()
while True:
	try:
		# since we're using asynchronous callbacks for both mqtt and xbee,
		# we don't need anything in the thread loop.
		
		time.sleep(0.001)
	except KeyboardInterrupt:
		break

# Kill MQTT connection.
client.loop_stop()
client.disconnect()

# Kill XBee connection.
xbee.halt()
serial_port.close()


