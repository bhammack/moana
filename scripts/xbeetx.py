# GPIO14 (pin 8) is TX
# GPIO15 (pin 10) is RX
from xbee import XBee
import serial

# PORT='/dev/ttyAMA0' This is acutally now the serial port for bluetooth devices.

# TX address
# 0013A200 417546F6

# RX address
# 0013A200 4175463C


PORT='/dev/ttyS0' # this is the standard uart gpio port.

BAUD=9600

ser = serial.Serial(PORT, BAUD)
#xbee = XBee(ser)
#xbee.tx(dest_addr='\x00\x01', data='test')


ser.write('test')


ser.close()