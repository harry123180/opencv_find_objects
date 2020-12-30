from serial.tools import list_ports

from pydobot import Dobot

port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
for i in range(20):
    device.move_to(x+40 , y, z, r, wait=False)
    device.move_to(x+40, y+40, z, r, wait=True)  # we wait until this movement is done before continuing
    device.move_to(x , y + 40, z, r, wait=True)  # we wait until this movement is done before continuing
    device.move_to(x , y, z, r, wait=False)
    #device.move_to()

device.close()