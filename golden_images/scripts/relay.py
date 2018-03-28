#! /usr/bin/python

# API mode must be enabled on the XBee device in order to work with this script.

# https://pypi.python.org/pypi/paho-mqtt/1.1
import paho.mqtt.client as mqtt

# https://pypi.python.org/pypi/XBee
from xbee import XBee, ZigBee
import serial

# The callback method is called whenever data is received.
def publish_data(data):
	client.publish('telemetry', {}, qos=0, retain=True), 
	print(data)

def on_connect(client, userdata, flags, rc):
	print("Connected with result code:", str(rc))
	# subs happen here
	
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
	
def on_publish(client, userdata, mid):
	pass
	
def on_subscribe(client, userdata, mid, granted_qos):
	pass
	
def on_unsubscribe(client, userdata, mid):
	pass
	
def on_control(client, userdata, message):
	print(message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.message_callback_add('control', on_control)

client.connect('iot.eclipse.org', 1883, 60)

# other loop functions are available.
client.loop_forever()


baud_rate = 9600
serial_port = serial.Serial('/dev/ttyUSB0', baud_rate);
xbee = XBee(serial_port, callback=publish_data)

# you may need to use bytearray(b'\x01\x02') instead of the raw bytestring.
DIO_on = b'\x05'
DIO_off = b'\x04'

#xbee.remote_at(dest_addr=b'\x56\x78', command='D2', parameter=b'\x04')
# looping thread. This will block until valid frames are received.
while True:
	try:
		#xbee.wait_read_frame()
		time.sleep(0.001)
	except KeyboardInterrupt:
		break
xbee.halt()
serial_port.close()



'''
while true
	determine if there's telemetry data to read in
	if there is, publish it to the server
	
	determine if there's control data to read from mqtt
	if there is, publish it to the xbee
	
	These two operations cannot block on each other, otherwise one will occur immediately following the other.
	OR, if it is necessary to implement some blocking, make sure it is on telemetry reception
'''

