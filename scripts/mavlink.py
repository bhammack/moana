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

BAUD_RATE = 57600 # 115200
#DEVICE = 'udp:127.0.0.1:14550'
#PORT = 'COM3'
DEVICE = '/dev/ttyACM0'
#DEVICE = 'COM3-1-QUADROTOR'
# 115200


print('Awaiting heartbeat...')

conn = mavutil.mavlink_connection(device=DEVICE, baud=BAUD_RATE, autoreconnect=True)
conn.wait_heartbeat()

print('We have a pulse!')