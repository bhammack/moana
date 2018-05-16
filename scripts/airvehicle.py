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
PACKET_SIZE = 128

# pip install serial
# pip install pymavlink

class Telemetry(object):
	def __init__(self):
		self.data = {}
		self.attitude_set = False
		self.vfr_hud_set = False

	def handle_message(self, msg):
		msg_type = msg.get_type()
		if (msg_type == "ATTITUDE"):
			self.set_attitude(msg)
		elif(msg_type == "VFR_HUD"):
			self.set_vfr_hud(msg)
	
	def set_attitude(self, msg):
		#self.roll = msg.roll
		#self.pitch = msg.pitch
		#self.yaw = msg.yaw
		#self.yawspeed = msg.yawspeed
		#self.pitchspeed = msg.pitchspeed
		#self.rollspeed = msg.rollspeed
		self.attitude_set = True
		self.data['timestamp'] = datetime.datetime.utcnow().isoformat()

	def set_vfr_hud(self, msg):
		#self.airspeed = msg.airspeed
		self.data['groundspeed'] = round(msg.groundspeed, DECIMAL_PLACES)
		self.data['heading'] = msg.heading
		self.data['altitude'] = round(msg.alt, DECIMAL_PLACES)
		#self.climb = msg.climb
		self.vfr_hud_set = True
		self.data['timestamp'] = datetime.datetime.utcnow().isoformat()

	def is_complete(self):
		return self.attitude_set and self.vfr_hud_set


def handle_message(msg):
	msg_type = msg.get_type()
	#print(msg_type)

	if (msg_type == "HEARTBEAT"):
		#print("heartbeat")
		mode = mavutil.mode_string_v10(msg)
		is_armed = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
		is_enabled = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_GUIDED_ENABLED

	elif (msg_type == "ATTITUDE"):
		attitude_data = (msg.roll, msg.pitch, msg.yaw, msg.rollspeed, msg.pitchspeed, msg.yawspeed)
		#print "Roll\tPit\tYaw\tRSpd\tPSpd\tYSpd"
		#print "%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t" % attitude_data

	elif (msg_type == "VFR_HUD"):
		# airspeed 		(m/s)
		# groundspeed 	(m/s)
		# heading 		(deg)
		# throttle		(%)
		# alt			(met)
		# climb			(m/s), climb rate
		hud_data = (msg.airspeed, msg.groundspeed, msg.heading, msg.throttle, msg.alt, msg.climb)
		#print "Aspd\tGspd\tHead\tThro\tAlt\tClimb"
		#print "%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f" % hud_data

	elif (msg_type == "AHRS2"):
		pass
	#	ahrs2 = (msg.roll, msg.pitch, msg.yaw, msg.altitude, msg.lat, msg.lng)
	#	print "Roll\tPit\tYaw\tAlt\tLat\tLng"
	#	print "%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f" % ahrs2

	# No need for this case, as it's the same infor as AHRS2...
	elif (msg_type == "AHRS3"):
		pass
	#	ahrs3 = (msg.roll, msg.pitch, msg.yaw, msg.altitude, msg.lat, msg.lng, msg.v1, msg.v2, msg.v3, msg.v4)
	#	print("ahrs3", msg.v1, msg.v2, msg.v3, msg.v4)

	elif (msg_type == "BAD_DATA"):
		pass
		#print('bad data')
		#if (mavutil.all_printable(msg.data)):
		#sys.stdout.write(msg.data)
		#	sys.stdout.flush()
	'''
	elif (msg_type == "STATUSTEXT"):
		print("StatusText:", msg.severity, msg.text)

	elif (msg_type == "PARAM_VALUE"):
		print("ParamValue:", msg.param_id, msg.param_value, msg.param_type, msg.param_count, msg.param_index)

	else:
		print("New message type received:", msg_type)
	'''


# Function called when xbee unit receives data. This will always be a control command.
def on_control(data):
	# send the land command.
	#conn.mav.command_long_send()
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
			if not msg: 
				continue
			handle_message(msg)
			t.handle_message(msg)

			if (t.is_complete()):
				telemetry = json.dumps(t.data, separators=(',', ':'))
				tpacket = telemetry.ljust(PACKET_SIZE).encode('latin-1')
				ser.write(tpacket)
				t = Telemetry()
				
		except KeyboardInterrupt:
			break

	conn.close()
	print('Goodbye!')


if __name__ == '__main__':
	main()