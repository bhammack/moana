import serial

SERIAL_BAUD = 9600
SERIAL_PORT = '/dev/ttyS0'

ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)

msg = 'Hello World!'
wrote = ser.write(msg)
print('Wrote %s bytes: %s' % (wrote, msg))
ser.close()