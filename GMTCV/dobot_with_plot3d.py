from serial.tools import list_ports
import threading
import time
from pydobot import Dobot
import numpy as np
import matplotlib.pyplot as plt
port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=False)
state = True
list_x = []
list_y = []
list_z = []
list_r = []
list_j1 = []
list_j2 = []
list_j3 = []
list_j4 = []

def job():
    global state
    while(state):
        (a,b,c,d,e,f,g,h)=device.pose()
        list_x.append(a)
        list_y.append(b)
        list_z.append(c)
        list_r.append(d)
        time.sleep(0.01)
t = threading.Thread(target = job)
#9,166,10
#196,193,10
#target
#196,193,10
#9,166,10
# 執行該子執行緒
#上升高度z=10
#夾取高讀z=-63
(x, y, z, r, j1, j2, j3, j4) = device.pose()
#print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
t.start()
target = [268,20]
for i in range(1):
    device.move_to(58 , -187,10, r, wait=True)
    device.move_to(228,-110,10, r, wait=True)
    device.move_to(target[0], target[1], 10, r, wait=True)
    device.move_to(target[0], target[1], -63, r, wait=True)
    device.suck(True)
    time.sleep(1)
    device.move_to(target[0], target[1], 10, r, wait=True)
    time.sleep(1)
    device.move_to(228,-110,10, r, wait=True)
    device.move_to(58 , -187,10, r, wait=True)
    device.suck(False)
    #device.move_to(x + 100, y + 100, z + 100, r+100, wait=False)
    #device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing
    #device.move_to(x , y + 40, z, r, wait=True)  # we wait until this movement is done before continuing
    #device.move_to(x , y, z, r, wait=False)
    #device.move_to()
state = False
t.join()
device.close()
##動作完畢 開始繪圖
# 建立 3D 圖形
fig = plt.figure()
ax = fig.gca(projection='3d')
# 產生 3D 座標資料
z_array = np.array(list_z)
x_array = np.array(list_x)
y_array = np.array(list_y)

# 繪製 3D 曲線
ax.auto_scale_xyz([0, 500], [0, 500], [0, 500])
ax.plot(x_array, y_array, z_array, color='gray', label='Arm path')
ax.scatter(x_array, y_array, z_array, c=z_array, cmap='jet', label='via point')

# 顯示圖例
ax.legend()
print(list_x)
print("**************************")
print(list_y)
print("**************************")
print(list_z)
print("**************************")

# 顯示圖形
plt.show()


print("Done.")


























