from serial.tools import list_ports
import cv2
from pydobot import Dobot
import tkinter as tk
import random as rd
from PIL import Image, ImageTk
from tkinter import *
import threading
import time
import matplotlib.pyplot as plt
import numpy as np
list_x = []
list_y = []
list_z = []
list_r = []
list_j1 = []
list_j2 = []
list_j3 = []
list_j4 = []
state = True
itt=0
def job():
    global state
    global list_z, list_x, list_y
    while(state):
        print('do')
        (a,b,c,d,e,f,g,h)=device.pose()
        list_x.append(a)
        list_y.append(b)
        list_z.append(c)
        list_r.append(d)
        time.sleep(0.01)
from tkinter import filedialog
root  = tk.Tk()
root.geometry('900x800')
root.title("操作介面")
""" GUI Function set """
btn = []
btn_context = ['Home','Detect','Next','Previous','Sucker','Move','Place']
port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=False)
(x, y, z, r, j1, j2, j3, j4) = device.pose()
detect_state=False
if(detect_state==False):
    target=[0,0]
def Home():
    print('Home')

    #PTPMode.MOVJ_ANGLE
    device.move_to(j1, j2, j3, j4, wait=False)
    #device.PTPMode.MOVJ_ANGLE(j1+10, j2, j3, j4, wait=True)
    var = []
    for j in range(6):
        var.append(ent[j].get())
    print(var)
def Detect():
    t1 = threading.Thread(target=CVJOB)
    t1.start()
def CVJOB():
    global target,detect_state
    detect_state =True
    cap = cv2.VideoCapture(0)
    itt = 0
    while (True):
        ret, frame = cap.read()
        im = cv2.resize(frame, (500, 500), interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        low_threshold = 1
        high_threshold = 10
        edges = cv2.Canny(blurred, low_threshold, high_threshold)
        contours, hierachy = cv2.findContours(edges, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        cnt_count = []
        centerX = []
        centerY = []
        for cnt in range(len(contours)):
            epsilon = 0.04 * cv2.arcLength(contours[cnt], True)
            approx = cv2.approxPolyDP(contours[cnt], epsilon, True)
            area = cv2.contourArea(contours[cnt])
            if (len(approx) < 5 and len(approx) > 3 and area > 2000 and area < 4000):

                cv2.drawContours(im, contours[cnt], -1, (255, 255, 255), 3)
                M = cv2.moments(contours[cnt])
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cnt_count.append(cnt)
                    centerX.append(cX)
                    centerY.append(cY)
                    f1 = int(cY * 0.541 + 48.602)
                    f2 = int(cX * 0.571 - 93.28)
                    target[0]=f1
                    target[1]=f2
                    text = str( f1) + ',' + str( f2 )
                    cv2.putText(im, text, (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 1, cv2.LINE_AA)
                    cv2.circle(im, (cX, cY), 10, (1, 227, 254), -1)
        cv2.imshow('123', im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('s'):  # 按s存檔
            itt = itt + 1;


    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    print('Detect')
def Next():
    global itt, im
    itt +=1
    #print('Next')
    cv2.imwrite('data\photo' + str(itt) + '.png', im)
    print('儲存:', 'photo' + str(itt) + '.png')
def Previous():
    print("Previous")
def Sucker():
    print("Sucker")
def Move():
    global target
    t3 = threading.Thread(target=MoveJOB)

    # 執行該子執行緒
    t3.start()
    print("Move")
def MoveJOB():
    global state
    t = threading.Thread(target=job)
    # 執行該子執行緒
    t.start()
    P0, P1, P2 = np.array([[58, -187, 40],
                           [228-rd.randint(-10,10), -110-rd.randint(-10,10), 10],
                           [target[0], target[1], 10]])
    # define bezier curve
    P = lambda t: (1 - t) ** 2 * P0 + 2 * t * (1 - t) * P1 + t ** 2 * P2
    # evaluate the curve on [0, 1] sliced in 50 points
    points = np.array([P(t) for t in np.linspace(0, 1, 50)])
    # get x and y coordinates of points separately
    xb, yb, zb = points[:, 0], points[:, 1], points[:, 2]  # plot
    for st in range(0,len(xb),2):
        device.move_to(xb[st], yb[st], zb[st], r, wait=False)
    device.move_to(xb[49], yb[49], -63, r, wait=True)
    device.suck(True)
    time.sleep(1)
    device.move_to(xb[49], yb[49], 10, r, wait=True)
    time.sleep(1)
    for st in range(len(xb)-1,0,-2):
        device.move_to(xb[st], yb[st], zb[st], r, wait=False)
    device.move_to(58, -187, -60, r, wait=True)
    device.suck(False)
    device.move_to(58, -187, 30, r, wait=True)
    state = False




def Place():
    global list_z,list_x,list_y,itt
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
    plt.savefig('data\mat'+str(itt)+'.png')  # 儲存圖片
    list_x = []
    list_y = []
    list_z = []
"""把function 放進List"""
fun_list = [Home,Detect,Next,Previous,Sucker,Move,Place]
for j in range(7):
    btn.append(tk.Button(root,text = btn_context[j],
                         command = fun_list[j],
                         width = 12,height = 3,
                         font=('microsoft yahei', 10, 'bold')))
    btn[j].place(x=j*120+20,y=500)
"""處理button 放置"""
"""ABC三點xy共6個entry"""
ent = []

for j in range(6):
    ent.append(tk.Entry(root, show=None,width = 12))
    if(j%2==0):
        ent[j].place(x=50,y=j*30+20)
        print("j=",j,"%2=0")
    else:
        print("j=", j, "%2!=0")
        ent[j].place(x=190,y=(j-1)*30+20)

"""放label"""
lb = []
計數器=1
for j in range(6):
    if(j%2==0):
        lb.append(tk.Label(root, text=str(target[0]), bg='green', font=('Arial', 12), width=5,
                           height=1))
        lb[j].place(x=0,y=j*30+20)
    else:
        lb.append(tk.Label(root, text=str(target[1]), bg='green', font=('Arial', 12), width=5,
                           height=1))
        lb[j].place(x=140,y=(j-1)*30+20)
        計數器+=1
計數器=0


root.mainloop()



device.close()