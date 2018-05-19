#!/usr/bin/python

# https://github.com/ArduPilot/pymavlink/
# http://ardupilot.org/dev/docs/mavlink-commands.html
# http://mavlink.org/messages/common

# actually, the pixhawk uses these...
# http://mavlink.org/messages/ardupilotmega
import datetime
from pymavlink import mavutil
import json
import serial

USB_BAUD = 11520
DEVICE = '/dev/ttyACM0' # this is actually a usb interface

PORT = '/dev/ttyS0'
BAUD = 9600

DECIMAL_PLACES = 2
PACKET_SIZE = 80

# pip install serial
# pip install pymavlink

class Telemetry(object):
	def __init__(self):
		self.data = {}
		self.attitude_set = False
		self.vfr_hud_set = False

	def handle_message(self, msg):
		msg_type = msg.get_type()
		#if (msg_type == "ATTITUDE"):
		#	self.set_attitude(msg)
		#	self.set_timestamp()
		if(msg_type == "VFR_HUD"):
			self.set_vfr_hud(msg)
			self.set_timestamp()
	
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


def handle_message(msg):
	msg_type = msg.get_type()
	#print(msg_type)

	if (msg_type == "HEARTBEAT"):
		#print("heartbeat")
		mode = mavutil.mode_string_v10(msg)
		is_armed = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
		is_enabled = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_GUIDED_ENABLED

# Function called when xbee unit receives data. This will always be a control command.
def on_control(raw_data):
	
	print(raw_data)
	#cmd = json.loads(data)
	# send the land command.
	#conn.mav.command_long_send()
	pass

# Function called to issue the motor lock to the autopilot.
def lock_propellers():
	pass

# Function called to issue the emergency land command / motor lock to the autopilot.
def emergency_land():
	# https://discuss.ardupilot.org/t/pymavlink-disarm-command/25425
	# MAV_CMD_NAV_LAND???
	pass


# Function called to release the payload. Is this necessary?
def release_payload():
	pass


# Main entry point of the application.
def main():
	ser = serial.Serial(PORT, BAUD)
	print('Awaiting heartbeat...')
	conn = mavutil.mavlink_connection(device=DEVICE, baud=USB_BAUD, autoreconnect=True)
	conn.wait_heartbeat()
	print('We have a pulse!')
	print('Requesting access to the mavlink data stream...')
	conn.mav.request_data_stream_send(
		conn.target_system, 
		conn.target_component, 
		mavutil.mavlink.MAV_DATA_STREAM_ALL, 
		USB_BAUD, 
		True
	)

	t = Telemetry()
	while(True):
		try:
			# enter what appears to be a non-blocking loop. A blocking mode seems available.
			msg = conn.recv_match(blocking=False)
			if msg:
				handle_message(msg)
				t.handle_message(msg)

				if (t.is_complete()):
					telemetry = json.dumps(t.data, separators=(',', ':'))
					tpacket = telemetry.ljust(PACKET_SIZE).encode('latin-1')
					ser.write(tpacket)
					print(telemetry)
					t = Telemetry()

			if (ser.in_waiting > 0):
					raw_data = ser.read_all()
					on_control(raw_data)
				
		except KeyboardInterrupt:
			break

	conn.close()
	print('Goodbye!')


if __name__ == '__main__':
	main()