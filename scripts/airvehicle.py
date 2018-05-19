#! /usr/bin/python

# https://github.com/ArduPilot/pymavlink/
# http://ardupilot.org/dev/docs/mavlink-commands.html
# http://mavlink.org/messages/common

# actually, the pixhawk uses these...
# http://mavlink.org/messages/ardupilotmega
import datetime
from pymavlink import mavutil
import json
import serial

USB_BAUD = 115200 # oddly bounded by intmax...?
USB_PORT = '/dev/ttyACM0' # this is actually a usb interface

SERIAL_PORT = '/dev/ttyS0'
SERIAL_BAUD = 9600

DECIMAL_PLACES = 2
TELEMETRY_PACKET_SIZE = 80
CONTROL_PACKET_SIZE = 14

# pip install serial
# pip install pymavlink

class Telemetry(object):
	def __init__(self):
		self.data = {}
		self.attitude_set = False
		self.vfr_hud_set = False

	def handle_message(self, msg):
		msg_type = msg.get_type()
		#print(msg_type)
		#if (msg_type == "ATTITUDE"):
		#	self.set_attitude(msg)
		#	self.set_timestamp()
		if (msg_type == "VFR_HUD"):
			self.set_vfr_hud(msg)
			self.set_timestamp()
			self.set_event()
	
	def set_attitude(self, msg):
		#self.roll = msg.roll
		#self.pitch = msg.pitch
		#self.yaw = msg.yaw
		#self.yawspeed = msg.yawspeed
		#self.pitchspeed = msg.pitchspeed
		#self.rollspeed = msg.rollspeed
		self.attitude_set = True

	def set_timestamp(self):
		self.data['ts'] = datetime.datetime.utcnow().isoformat()

	def set_event(self):
		self.data['e'] = 0

	def set_vfr_hud(self, msg):
		#self.airspeed = msg.airspeed
		#self.climb = msg.climb
		self.data['gspd'] = round(msg.groundspeed, DECIMAL_PLACES)
		self.data['hdg'] = msg.heading
		self.data['alt'] = round(msg.alt, DECIMAL_PLACES)
		self.vfr_hud_set = True

	def is_complete(self):
		#return self.attitude_set and self.vfr_hud_set
		return self.vfr_hud_set


#def handle_message(msg):
#	msg_type = msg.get_type()
	#print(msg_type)

	#if (msg_type == "HEARTBEAT"):
		#print("heartbeat")
	#	mode = mavutil.mode_string_v10(msg)
	#	is_armed = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
	#	is_enabled = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_GUIDED_ENABLED

# Function called when xbee unit receives data. This will always be a control command.
def on_control(raw_data):
	data = json.loads(raw_data.decode('utf-8'))
	cmd = data['cmd']
	# Map the command to a function
	if cmd == 'LOCK':
		lock_propellers()
	elif cmd == 'UNLK':
		unlock_propellers()
	elif cmd == 'LAND':
		emergency_land()
	elif cmd == 'DROP':
		release_payload()
	else:
		print('Error: bad command')
	pass


def unlock_propellers():
	print('Unlocking propellers...')

# Function called to issue the motor lock to the autopilot.
def lock_propellers():
	print('Locking propellers...')

# Function called to issue the emergency land command / motor lock to the autopilot.
def emergency_land():
	# https://discuss.ardupilot.org/t/pymavlink-disarm-command/25425
	# MAV_CMD_NAV_LAND???
	print('Initiating emergency land...')


# Function called to release the payload. Is this necessary?
def release_payload():
	print('Releasing payload...')

def wait_heartbeat(pixhawk):
	print('Waiting for APM heartbeat...')
	pixhawk.wait_heartbeat()
	print('Heartbeat from APM (system %u component %u)' % (pixhawk.target_system, pixhawk.target_system))


# Main entry point of the application.
def main():
	ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)
	pixhawk = mavutil.mavlink_connection(device=USB_PORT, baud=USB_BAUD)
	wait_heartbeat(pixhawk)
	print('Requesting access to the mavlink data stream...')
	pixhawk.mav.request_data_stream_send(
		pixhawk.target_system, 
		pixhawk.target_component, 
		mavutil.mavlink.MAV_DATA_STREAM_ALL, 
		4,
		True
	)

	t = Telemetry()
	while(True):
		try:
			# enter what appears to be a non-blocking loop. A blocking mode seems available.
			msg = pixhawk.recv_match(blocking=False)
			if msg:
				#handle_message(msg)

				t.handle_message(msg)
				if (t.is_complete()):
					telemetry = json.dumps(t.data, separators=(',', ':'))
					tpacket = telemetry.ljust(TELEMETRY_PACKET_SIZE).encode('latin-1')
					ser.write(tpacket)
					print(telemetry)
					t = Telemetry()

			if (ser.in_waiting >= CONTROL_PACKET_SIZE):
				raw_data = ser.read(size=CONTROL_PACKET_SIZE)
				on_control(raw_data)
				
		except KeyboardInterrupt:
			break
	print('\nClosing MAVLINK message stream...')
	pixhawk.close()
	ser.close()


if __name__ == '__main__':
	main()