from serial.tools import list_ports
import threading
import time
from pydobot import Dobot

port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=False)
state = True
def job():
    global state
    while(state):
        print(device.pose())
        time.sleep(0.01)
t = threading.Thread(target = job)

# 執行該子執行緒

(x, y, z, r, j1, j2, j3, j4) = device.pose()
#print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
t.start()
for i in range(1):
    device.move_to(x+100 , y, z, r, wait=False)
    device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing
    #device.move_to(x , y + 40, z, r, wait=True)  # we wait until this movement is done before continuing
    #device.move_to(x , y, z, r, wait=False)
    #device.move_to()
state = False
t.join()
device.close()

print("Done.")