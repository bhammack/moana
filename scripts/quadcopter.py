#! /usr/bin/python

# https://github.com/ArduPilot/pymavlink/
# http://ardupilot.org/dev/docs/mavlink-commands.html
# http://mavlink.org/messages/common

# actually, the pixhawk uses these...
# http://mavlink.org/messages/ardupilotmega

# STABILIZE mode appears to have supersceded MANUAL mode.

import datetime
import json
import serial
from dronekit import connect, VehicleMode

# optional for temp
import Adafruit_DHT
import tsl2591

USB_BAUD = 115200 # oddly bounded by intmax...?
#USB_PORT = '/dev/ttyACM0' # this is actually a usb interface
USB_PORT = '/dev/ttyACM1' # this is actually a usb interface

SERIAL_PORT = '/dev/ttyS0'
SERIAL_BAUD = 9600

DECIMAL_PLACES = 2
TELEMETRY_PACKET_SIZE = 128
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
	# Arm the vehicle
	vehicle.armed = True

# Function called to issue the motor lock to the autopilot.
def lock_propellers(vehicle):
	print('Locking propellers...')
	# Disarm the vehicle.
	vehicle.armed = False


# Function called to issue the emergency land command / motor lock to the autopilot.
def emergency_land(vehicle):
	print('Initiating emergency land...')
	# Land the vehicle. Steal back control.
	vehicle.mode = VehicleMode("LAND")


def begin_mission(vehicle):
	vehicle.mode = VehicleMode("STABILIZE")
	vehicle.armed = True


# Function called to release the payload. Is this necessary?
def release_payload(vehicle):
	print('Releasing payload...')

def read_am2302(GPIOPIN):
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, GPIOPIN)
	temperature = temperature * 1.8 + 32 # convert c to f.
	return (humidity, temperature)

def read_tsl2591(tsl):
	full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
	lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
	return lux

# Main entry point of the application.
def main():
	ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)
	vehicle = connect(USB_PORT, baud=USB_BAUD, wait_ready=True)
	tsl = tsl2591.Tsl2591()
	tsl.set_gain(tsl2591.GAIN_HIGH)
	GPIOPIN = 4

	while True:
		try:
			# enter what appears to be a non-blocking loop. A blocking mode seems available.
			#msg = pixhawk.recv_match(blocking=False)
			#if msg:
				#handle_message(msg)
			t = {}
			t['hdg'] = round(vehicle.heading, DECIMAL_PLACES)
			t['spd'] = round(vehicle.groundspeed, DECIMAL_PLACES)
			t['alt'] = round(vehicle.location.global_frame.alt, DECIMAL_PLACES)
			t['dt'] = datetime.datetime.utcnow().isoformat()
			t['vol'] = vehicle.battery.voltage # millivolts
			t['cur'] = vehicle.battery.current # 10 * milliamperes
			humidity, temperature = read_am2302(GPIOPIN)
			t['tmp'] = round(temperature, DECIMAL_PLACES)
			#t['hum'] = round(humidity, DECIMAL_PLACES)
			lux = read_tsl2591(tsl)
			t['lux'] = int(lux)
			t['e'] = 0

			telemetry = json.dumps(t, separators=(',', ':'))
			tpacket = telemetry.ljust(TELEMETRY_PACKET_SIZE).encode('latin-1')
			written = ser.write(tpacket)
			print('Wrote packet size %s' % written)
			#print(telemetry)

			if (ser.in_waiting >= CONTROL_PACKET_SIZE):
				raw_data = ser.read(size=CONTROL_PACKET_SIZE)
				on_control(raw_data, vehicle)
				
		except KeyboardInterrupt:
			print('KeyboardInterrupt - closing')
			break

		except IOError:
			print('IOError - packet not sent')
			
	print('\nClosing serial connections...')
	vehicle.close()
	ser.close()


if __name__ == '__main__':
	main()