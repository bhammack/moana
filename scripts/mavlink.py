#!/usr/bin/python

# https://github.com/ArduPilot/pymavlink/
# http://ardupilot.org/dev/docs/mavlink-commands.html
from pymavlink import mavutil

BAUD_RATE = 57600
DEVICE = 'udp:127.0.0.1:14550'



conn = mavutil.mavlink_connection(device=DEVICE, baud=BAUD_RATE, autoreconnect=True)
conn.wait_heartbeat()
