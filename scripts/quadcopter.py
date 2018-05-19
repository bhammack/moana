#! /usr/bin/python

# https://github.com/ArduPilot/pymavlink/
# http://ardupilot.org/dev/docs/mavlink-commands.html
# http://mavlink.org/messages/common

# actually, the pixhawk uses these...
# http://mavlink.org/messages/ardupilotmega
import datetime
import json
import serial
from dronekit import connect, VehicleMode

USB_BAUD = 115200 # oddly bounded by intmax...?
USB_PORT = '/dev/ttyACM0' # this is actually a usb interface

SERIAL_PORT = '/dev/ttyS0'
SERIAL_BAUD = 9600

DECIMAL_PLACES = 2
TELEMETRY_PACKET_SIZE = 80
CONTROL_PACKET_SIZE = 14

# Function called when xbee unit receives data. This will always be a control command.
def on_control(raw_data, vehicle):
	data = json.loads(raw_data.decode('utf-8'))
	cmd = data['cmd']
	# Map the command to a function
	if cmd == 'LOCK':
		lock_propellers(vehicle)
	elif cmd == 'UNLK':
		unlock_propellers(vehicle)
	elif cmd == 'LAND':
		emergency_land(vehicle)
	elif cmd == 'DROP':
		release_payload(vehicle)
	else:
		print('Error: bad command')
	pass


def unlock_propellers(vehicle):
	print('Unlocking propellers...')


# Function called to issue the motor lock to the autopilot.
def lock_propellers(vehicle):
	print('Locking propellers...')


# Function called to issue the emergency land command / motor lock to the autopilot.
def emergency_land(vehicle):
	print('Initiating emergency land...')


# Function called to release the payload. Is this necessary?
def release_payload(vehicle):
	print('Releasing payload...')


# Main entry point of the application.
def main():
	ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)
	vehicle = connect(USB_PORT, baud=USB_BAUD, wait_ready=True)
	
	while True:
		try:
			# enter what appears to be a non-blocking loop. A blocking mode seems available.
			#msg = pixhawk.recv_match(blocking=False)
			#if msg:
				#handle_message(msg)

			t = {}
			t['hdg'] = round(vehicle.heading, DECIMAL_PLACES)
			t['gspd'] = round(vehicle.groundspeed, DECIMAL_PLACES)
			t['alt'] = round(vehicle.location.global_frame.alt, DECIMAL_PLACES)
			t['ts'] = datetime.datetime.utcnow().isoformat()
			t['e'] = 0

			telemetry = json.dumps(t, separators=(',', ':'))
			tpacket = telemetry.ljust(TELEMETRY_PACKET_SIZE).encode('latin-1')
			ser.write(tpacket)
			print(telemetry)

			if (ser.in_waiting >= CONTROL_PACKET_SIZE):
				raw_data = ser.read(size=CONTROL_PACKET_SIZE)
				on_control(raw_data, vehicle)
				
		except KeyboardInterrupt:
			break
	print('\nClosing serial connections...')
	vehicle.close()
	ser.close()


if __name__ == '__main__':
	main()