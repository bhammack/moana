#! /usr/bin/python

import time
import serial
import datetime
import math
import json
import serial

# https://pypi.python.org/pypi/paho-mqtt/1.1
import paho.mqtt.client as mqtt

# API mode must be enabled on the XBee device in order to work with this script.
# https://pypi.python.org/pypi/XBee

# The XBee library may be overkill. We may be able to use just the standard pySerial library.
# https://stackoverflow.com/questions/13436471/how-can-i-send-strings-of-data-to-an-xbee-with-a-python-library
#from xbee import XBee

HOSTNAME = "broker.mqttdashboard.com"
PORT = 1883
TELEMETRY_TOPIC = 'telemetry'
CONTROL_TOPIC = 'control'
CALIBRATION_TOPIC = 'calibration'
PACKET_SIZE = 128 # packet size in bytes.
BAUD = 9600
PORT = '/dev/ttyS0'

LAST_LATITUDE = 0
LAST_LONGITUDE = 0
LAST_TIMESTAMP = datetime.datetime.now()


#serial_port = serial.Serial(SERIAL_ADDR, BAUD_RATE);
#xbee = XBee(serial_port, callback=on_telemetry)


# Calculate the next latitude and longitude using a given latlng, heading angle, and distance (in meters).
def next_position(lat, lng, heading, distance):
    # https://stackoverflow.com/questions/19352921/how-to-use-direction-angle-and-speed-to-calculate-next-times-latitude-and-longi
    R = 6371000 # earth radius in meters
    newlat = math.asin(math.sin(math.pi / 180 * lat) * math.cos(distance / R) + math.cos(math.pi / 180 * lat) * math.sin(distance / R) * math.cos(math.pi / 180 * heading))
    newlng = math.pi / 180 * lng + math.atan2(math.sin(math.pi / 180 * heading) * math.sin(distance / R) * math.cos(math.pi / 180 * lat), math.cos(distance / R) - math.sin(math.pi / 180 * lat) * math.sin(newlat))
    # truncate the final values to 6 decimal places.
    finalnewlat = 180 / math.pi * newlat
    finalnewlng = 180 / math.pi * newlng
    return(round(finalnewlat, 6), round(finalnewlng, 6))


# Updates the global state with the newest information.
def update_position(lat, lng, timestamp):
	global LAST_LATITUDE
	global LAST_LONGITUDE
	global LAST_TIMESTAMP
	LAST_LATITUDE = lat
	LAST_LONGITUDE = lng
	LAST_TIMESTAMP = timestamp


# Function called when the mqtt client connects to the web server.
def on_connect(client, userdata, flags, rc):
	print("Connected to " + HOSTNAME + ":" + str(PORT))
	client.subscribe(CONTROL_TOPIC)
	client.subscribe(CALIBRATION_TOPIC)


# Function called when the mqtt client disconnects from the web server.
def on_disconnect(client, userdata, rc):
	print("Disconnected from broker with rc: %s" % rc)


# Function called when the mqtt client receives calibration on the position channel.
def on_calibration(client, userdata, message):
	# Save off the newest true position for dead reckoning.
	payload = json.loads(str(message.payload))
	print(message.topic, payload)
	update_position(payload['latitude'], payload['longitude'], datetime.datetime.now())
	print('Calibrating dead reckoning. Current position is %s, %s' % (LAST_LATITUDE, LAST_LONGITUDE))


# Function called when the mqtt client receives commands on the control channel.
def on_control(client, userdata, message):
	payload = str(message.payload)
	print(message.topic, payload)
	# send the data to an xbee
	# http://python-xbee.readthedocs.io/en/latest/#sending-data-to-an-xbee-device
	#xbee.send("at", frame='A' command='MY' parameter=None)


# Function called when data is received from the XBee radio.
def on_telemetry(data):
	# get these values from the packet
	altitude = data['altitude']
	heading = data['heading']
	groundspeed = data['groundspeed']
	temperature = 0
	power = 0
	# also get the timestamp.

	# Perform dead reckoning and get the position we're at.
	now = datetime.datetime.now()
	seconds = (now - LAST_TIMESTAMP).total_seconds()
	distance = groundspeed * seconds
	lat, lng = next_position(LAST_LATITUDE, LAST_LONGITUDE, heading, distance)
	update_position(lat, lng, now)
	eventCode = 0
	
	# Create the telemetry packet.
	telemetry = {}
	telemetry['latitude'] = lat
	telemetry['longitude'] = lng
	telemetry['heading'] = heading
	telemetry['speed'] = groundspeed
	telemetry['altitude'] = altitude
	telemetry['eventCode'] = eventCode
	telemetry['temperature'] = temperature
	telemetry['power'] = power
	
	# Publish the telemetry packet
	client.publish(TELEMETRY_TOPIC, json.dumps(telemetry), 0, True)


# Main entry point for the application.
def main():
	ser = serial.Serial(PORT, BAUD)

	print("Initalizing communications relay...")
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_disconnect = on_disconnect
	client.message_callback_add(CONTROL_TOPIC, on_control)
	client.message_callback_add(CALIBRATION_TOPIC, on_calibration)
	client.connect(HOSTNAME, PORT)

	client.loop_start()
	#client.loop_forever()
	while True:
		try:
			# since we're using asynchronous callbacks for both mqtt and xbee,
			# we don't need anything in the thread loop.
			raw_data = ser.read(PACKET_SIZE)
			jsdata = json.loads(raw_data)
			on_telemetry(jsdata)

		except KeyboardInterrupt:
			break

	# Kill MQTT connection.
	client.disconnect()
	client.loop_stop()

	# Kill XBee connection.
	xbee.halt()
	serial_port.close()


if __name__ == "__main__":
	main()