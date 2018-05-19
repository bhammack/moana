#! /usr/bin/python

import time
import serial
import datetime
import math
import json
import serial
import datetime

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
TELEMETRY_PACKET_SIZE = 128 # packet size in bytes.
CONTROL_PACKET_SIZE = 14


SERIAL_BAUD = 9600
SERIAL_PORT = '/dev/ttyS0'

LAST_LATITUDE = 0
LAST_LONGITUDE = 0
LAST_TIMESTAMP = datetime.datetime.now()

COMMAND = ''

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
	print("Disconnected from " + HOSTNAME + ":" + str(PORT))


# Function called when the mqtt client receives calibration on the position channel.
def on_calibration(client, userdata, message):
	# Save off the newest true position for dead reckoning.
	payload = json.loads(message.payload.decode('utf-8'))
	update_position(payload['latitude'], payload['longitude'], datetime.datetime.now())
	print('Setting new seed position: %s, %s' % (LAST_LATITUDE, LAST_LONGITUDE))


# Function called when the mqtt client receives commands on the control channel.
def on_control(client, userdata, message):
	payload = json.loads(message.payload.decode('utf-8'))
	# contruct a command packet. Smaller size than the control packet.
	cmd = payload['command']
	global COMMAND
	COMMAND = json.dumps({'cmd': cmd}, separators=(',',':'))
	print('Received command signal: ', cmd)


# Function called when data is received from the XBee radio.
def on_telemetry(client, raw_data):
	data = json.loads(raw_data.decode('utf-8'))
	# get these values from the packet
	altitude = data['alt']
	heading = data['hdg']
	groundspeed = data['gspd']
	voltage = data['vol']
	current = data['cur']
	temperature = data['temp']
	humidity = data['hum']
	timestamp = data['ts']
	eventCode = data['e']
	print('Received data created at:', timestamp)

	# This is so fking stupid. 
	# Python has .isoformat(), but has no native way of converting an iso back to dt.
	# Turns out they're adding it in Python 3.7... but until then... ugh
	created_dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
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
	telemetry['voltage'] = voltage
	telemetry['current'] = current
	telemetry['altitude'] = altitude
	telemetry['eventCode'] = eventCode
	telemetry['temperature'] = temperature
	telemetry['humidity'] = humidity
	
	# Publish the telemetry packet
	client.publish(TELEMETRY_TOPIC, json.dumps(telemetry), 0, True)


# Method to cause the serial port to read until it has a full json object.
def read_json(ser):
	is_json = False
	raw_packet = None

	# While we need to, read a byte.
	while not is_json:
		byte = ser.read()
		print(byte)
		if (byte.decode('utf-8') == '}'):
			raw_packet = ser.read(size=TELEMETRY_PACKET_SIZE)
			print(raw_packet)
			is_json = True
	return raw_packet


# Main entry point for the application.
def main():

	global COMMAND
	ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)

	print("Initalizing communications relay...")
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_disconnect = on_disconnect
	client.message_callback_add(CONTROL_TOPIC, on_control)
	client.message_callback_add(CALIBRATION_TOPIC, on_calibration)
	client.connect(HOSTNAME, PORT)

	client.loop_start()
	#client.loop_forever()
	# https://robotics.stackexchange.com/questions/11897/how-to-read-and-write-data-with-pyserial-at-same-time
	while True:
		try:
			# since we're using asynchronous callbacks for both mqtt and xbee,
			# we don't need anything in the thread loop.
			try:
				if COMMAND:
					written = ser.write(COMMAND.encode('latin-1'))
					COMMAND = None
					print('Wrote packet size %s' % written)

				#if (ser.in_waiting >= TELEMETRY_PACKET_SIZE):
				#raw_data = ser.read(size=TELEMETRY_PACKET_SIZE)
				#print(ser.read_all())
				raw_data = read_json(ser)
				#on_telemetry(client, raw_data)
				
			except ValueError:
				print('ValueError')
				ser.flushInput()

		except KeyboardInterrupt:
			break

	# Kill MQTT connection.
	client.disconnect()
	client.loop_stop()

	# Kill XBee connection.
	ser.close()


if __name__ == "__main__":
	main()