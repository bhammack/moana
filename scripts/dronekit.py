#import dronekit_sitl
from dronekit import connect, VehicleMode

#ADDR = 'tcp:127.0.0.1:5760'
ADDR = 'COM3-1-QUADROTOR'

vehicle = connect(ADDR, wait_ready=True)

print('Heading', str(vehicle._heading))

vehicle.close()

#sitl.stop()