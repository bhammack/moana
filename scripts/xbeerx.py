# GPIO14 (pin 8) is TX
# GPIO15 (pin 10) is RX
#from xbee import XBee
import serial

# PORT='/dev/ttyAMA0'
PORT='/dev/ttyS0'

BAUD=9600

ser = serial.Serial(PORT, BAUD)

while True:
    try:
        data = ser.read(128)
        print(data)
    except KeyboardInterrupt:
        break

ser.close()