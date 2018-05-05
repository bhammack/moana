#!/usr/bin/python

# https://github.com/ArduPilot/pymavlink/
# http://ardupilot.org/dev/docs/mavlink-commands.html

# pip install serial
# pip install pymavlink

'''
Auto-detected serial ports are:
/dev/serial/by-id/usb-3D_Robotics_PX4_FMU_v2.x_0-if00
Connecting to /dev/serial/by-id/usb-3D_Robotics_PX4_FMU_v2.x_0-if00
Connect /dev/serial/by-id/usb-3D_Robotics_PX4_FMU_v2.x_0-if00 source_system=255
Log Directory:
Telemetry log: mav.tlog
MAV> Waiting for heartbeat from /dev/serial/by-id/usb-3D_Robotics_PX4_FMU_v2.x_0                                                           -if00
9IAPM: EKF2 IMU1 tilt alignment complete
online system 1
STABILIZE> Mode STABILIZE
APM: PreArm: RC Roll not configured
APM: PreArm: Compass not calibrated
APM: PreArm: Throttle below Failsafe
        Q!APM: APM:Copter V3.5.5 (27229c83)
APM: PX4: 0384802e NuttX: 1bcae90b
APM: Frame: QUAD
APM: PX4v2 003A003C 31375114 34373939
fence breach
Received 773 parameters
Saved 773 parameters to mav.parm
MAV> APM: PreArm: RC Roll not configured
'''


from pymavlink import mavutil

BAUD_RATE = 11520
DEVICE = '/dev/ttyACM0' # this is actually a usb interface



print('Awaiting heartbeat...')
conn = mavutil.mavlink_connection(device=DEVICE, baud=BAUD_RATE, autoreconnect=True)
conn.wait_heartbeat()
print('We have a pulse!')
print('Requesting access to the mavlink data stream...')
conn.mav.request_data_stream_send(conn.target_system, conn.target_component, mavutil.mavlink.MAV_DATA_STREAM_ALL, BAUD_RATE, True)

while(True):
    try:
		# enter what appears to be a non-blocking loop. A blocking mode seems available.
		msg = conn.recv_match(blocking=False)
		if not msg: 
			continue

		msg_type = msg.get_type()

		if (msg_type == "HEARTBEAT"):
			print("heartbeat")
			mode = mavutil.mode_string_v10(msg)
			is_armed = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
			is_enabled = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_GUIDED_ENABLED

		if (msg_type == "ATTITUDE"):
			attitude_data = (msg.roll, msg.pitch, msg.yaw, msg.rollspeed, msg.pitchspeed, msg.yawspeed)
			print "Roll\tPit\tYaw\tRSpd\tPSpd\tYSpd"
			print "%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t" % attitude_data

		if (msg_type == "VFR_HUD"):
			hud_data = (msg.airspeed, msg.groundspeed, msg.heading, msg.throttle, msg.alt, msg.climb)
			print "Aspd\tGspd\tHead\tThro\tAlt\tClimb"
			print "%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f" % hud_data
			
    except KeyboardInterrupt:
		conn.close()
		break

