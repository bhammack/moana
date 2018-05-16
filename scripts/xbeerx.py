# GPIO14 (pin 8) is TX
# GPIO15 (pin 10) is RX
from xbee import XBee
import serial

# PORT='/dev/ttyAMA0'
PORT='/dev/ttyS0'

BAUD=9600

ser = serial.Serial(PORT, BAUD)
'''
xbee = XBee(ser)
while True:
    try:
        response = xbee.wait_read_frame()
        print response
    except KeyboardInterrupt:
        break
'''


print(ser.read())



ser.close()