import numpy as np
import cv2
import math
import time
pi = 3.14159
coefficient_of_rad = pi/180
initialA=(50,50)
width = 512#圖框寬
length = 512 #圖框長
img = np.zeros((width, length, 3), np.uint8)
center_point = (int(width/2),int(length/2))#定義中心點
# 將圖片用淺灰色 (200, 200, 200) 填滿
link1_length = 80#定義Link1的長度
link2_length = 60#定義Link2的長度
link3_length = 40#定義Link3的長度
link1_initial=center_point
theta1 = 70
delaytime=0.1#每個畫面間隔時間
path=[]
ball_A=(initialA)
Krad=pi/180
t = 0
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(5,0,0),1)
        print('do')
def matrices(d1,d2,d3):
    T1 = np.array([[math.cos(d1),-math.sin(d1),0,link1_length*math.cos(d1)],
                   [math.sin(d1), math.cos(d1),0,link1_length*math.sin(d1)],
                   [      0     ,        0      ,        1      ,      0    ],
                   [      0     ,        0      ,        0      ,      1    ]])
    T2 = np.array([[math.cos(d2),-math.sin(d2),0,link2_length*math.cos(d2)],
                   [math.sin(d2),math.cos(d2),0,link2_length*math.sin(d2)],
                   [      0     ,        0      ,        1      ,      0    ],
                   [      0     ,        0      ,        0      ,      1    ]])
    """T3 = np.array([[math.cos(d3),-math.sin(d3),0,link3_length*math.cos(d3)],
                   [math.sin(d3),math.cos(d3),0,link3_length*math.sin(d3)],
                   [      0     ,        0      ,        1      ,      0    ],
                   [      0     ,        0      ,        0      ,      1    ]])"""
    Org = np.array([[0],
                    [0],
                    [0],
                    [1]])
    T13=np.array([[math.cos(d1+d2+d3),-math.sin(d1+d2+d3),0,(link1_length*math.cos(d1))+(link2_length*math.cos(d1+d2))+(link3_length*math.cos(d1+d2+d3))],
                  [math.sin(d1+d2+d3),math.cos(d1+d2+d3),0,(link1_length*math.sin(d1))+(link2_length*math.sin(d1+d2))+(link3_length*math.sin(d1+d2+d3))],
                  [0,0,1,0],
                  [0,0,0,1]])
    T12 = T1.dot(T2)
    #T123 =T12.dot(T3)
    S1 = T1.dot(Org)
    S2 = T12.dot(Org)
    S3 = T13.dot(Org)
    te1=str(S1)
    te2=str(S2)
    te3=str(S3)
    cv2.putText(img, te1, (200, 40), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, te2, (200, 80), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, te3, (200, 120), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.line(img, (int(Org[0][0])+256,int(Org[1][0])+256),(int(S1[0][0])+256,int(S1[1][0])+256), (0, 170, 75), 8)
    cv2.line(img,(int(S1[0][0])+256,int(S1[1][0])+256) , (int(S2[0][0])+256,int(S2[1][0])+256), (0, 255, 255), 8)
    cv2.line(img, (int(S2[0][0])+256,int(S2[1][0])+256), (int(S3[0][0])+256,int(S3[1][0])+256), (255, 2, 25), 8)
    
def link_c(d1,d2,d3):
    
    cv2.circle(img,(256, 256), 1, (6, 255, 255), 1)
    beta = d2+d1#-(90*pi/180)
    gama = beta+d3
    link1_final = (256+int(link1_length*math.cos(d1)),256+int(link1_length*math.sin(d1)))
    link2_final = (int(link2_length*math.cos(beta)+link1_final[0]),int(link2_length*math.sin(beta)+link1_final[1]))
    link3_final = (int(link3_length*math.cos(gama)+link2_final[0]),int(link3_length*math.sin(gama)+link2_final[1]))
    cv2.line(img, link1_initial, link1_final, (0, 0, 255), 8)
    cv2.line(img, link1_final, link2_final, (0, 255, 255), 8)
    cv2.line(img, link2_final, link3_final, (255, 2, 25), 8)
    text1 = str(link1_final)
    text2 = str(link2_final)
    text3 = str(link3_final)
    cv2.putText(img, text1, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, text2, (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, text3, (10, 120), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 255), 1, cv2.LINE_AA)
    path.append(link3_final)
    for cnt in range(len(path)):
        cv2.circle(img,path[cnt], 1, (195, 185, 205), 1)
    #print(link2_final)

while(True):    
    cv2.setMouseCallback('image',draw_circle)
    img.fill(100)#灰度200填充
    if t == 360:
        t=0
    degree =[t,t,0]
    
    radian=[degree[0]*coefficient_of_rad,degree[1]*coefficient_of_rad,degree[2]*coefficient_of_rad]
    link_c(radian[0]*0.5,radian[1],radian[2])
    matrices(radian[0],radian[1],radian[2])
    

    cv2.imshow('Window', img)#把圖show出來
    
    t+=0.1#時間+1
    time.sleep(0.0001)#底類時間
    if cv2.waitKey(1) & 0xFF == ord('q'):        #等待  如果我按q她就
        cv2.destroyAllWindows()#關掉視窗
        break#離開迴圈



# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
