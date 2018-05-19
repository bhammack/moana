import serial

SERIAL_BAUD = 9600
SERIAL_PORT = '/dev/ttyS0'

ser = serial.Serial(SERIAL_PORT, SERIAL_BAUD)
print('Waiting for data...')
while True:
    try:
        print(ser.read())
    except KeyboardInterrupt:
        break

ser.close()