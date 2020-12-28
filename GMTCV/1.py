import numpy as np
import cv2
import math
import time
#import martix_test as mr
#import time
car_width = 60
car_length = 50
V1 = -50
V2 = 50
pi = 3.14159
iccon=360/(2*pi*car_width)
car_x = 175
car_y = 60
Krad=pi/180
Kdeg=180/pi
width = 1000#圖框寬
length = 1000 #圖框長
# 建立一張 512x512 的 RGB 圖片（黑色）
img = np.zeros((width, length, 3), np.uint8)
center_point = (int(width/2),int(length/2))#定義中心點
def rad(x):
    return (math.radians(x))
def draw_car(x,y,deg):
    """pts = np.array([[170, 55],
                    [170, 65],
                    [200, 65],
                    [200, 55]], np.int32)"""
    p1 = np.array([[int(-car_width/2)],[int(-car_length/2)]])
    p2 = np.array([[int(-car_width/2)],[int(car_length/2)]])
    p3 = np.array([[int(car_width/2)],[ int(car_length/2)]])
    p4 = np.array([[int(car_width/2)],[int(-car_length/2)]])

    R = np.array([[math.cos(rad(deg)),-math.sin(rad(deg))],
                  [math.sin(rad(deg)),math.cos(rad(deg))]])
    p1_=R.dot(p1)
    p2_=R.dot(p2)
    p3_=R.dot(p3)
    p4_=R.dot(p4)

    #print('pts=',pts)
    #pts = pts.reshape((-1, 1, 2))
    #cv2.polylines(img, [pts], True, (255, 255, 0), 4)
    #print(p1_[0])
    new = np.array([[int(p1_[0])+x,int(p1_[1])+y],
                    [int(p2_[0])+x,int(p2_[1])+y],
                    [int(p3_[0])+x,int(p3_[1])+y],
                    [int(p4_[0])+x,int(p4_[1])+y]])
    new = new.reshape((-1, 1, 2))
    cv2.polylines(img, [new], True, (255, 255, 255), 4)
    cv2.line(img, (int(p1_[0])+x,int(p1_[1])+y), (int(p4_[0])+x,int(p4_[1])+y), (200, V2, 255), 10)
    cv2.line(img, (int(p2_[0])+x,int(p2_[1])+y), (int(p3_[0])+x,int(p3_[1])+y), (200, V1, 255), 10)
    cv2.putText(img, 'wheel_1_speed=', (10, 40), cv2.FONT_HERSHEY_PLAIN,
      1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, str(V2), (190, 40), cv2.FONT_HERSHEY_PLAIN,
  1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, 'wheel_2_speed=', (10, 100), cv2.FONT_HERSHEY_PLAIN,
      1, (0, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, str(V1), (190, 100), cv2.FONT_HERSHEY_PLAIN,
  1, (0, 255, 255), 1, cv2.LINE_AA)

        
delaytime=0.1#每個畫面間隔時間
i = 0
Tdeg=0
def model(theta,vl,vr):
    if (vl!=vr):
        R_dist=car_width*(vr+vl)/(2*(vr-vl))
    elif(vl == vr):
        R_dist =0
    avg_speed=(vr+vl)/2
    dx=avg_speed*delaytime*math.cos(rad(theta))
    dy=avg_speed*delaytime*math.sin(rad(theta))
    omega=((vr-vl)*180)/(car_width*pi)
    #print(vr-vl)
    theta = theta+omega*delaytime
    return dx,dy,theta
timeg= 0
while(True):
    
    img = np.zeros((width, length, 3), np.uint8)
    
    if (timeg == 100):
        V2=20
    if (timeg == 300):
        V2= 5
    if (timeg == 350):
        V2=20
    
    draw_car(car_x,car_y,Tdeg)
    dx,dy,Tdeg = model(Tdeg,V1,V2)
    print(dx,dy,Tdeg)
    car_x = int(car_x+dx)
    car_y = int(car_y+dy)
    #draw_car(185,60,Tdeg)
    # 繪製多邊形
    cv2.imshow('Window', img)
    #h_flip = cv2.flip(img, 0)
    #cv2.imshow('Window', h_flip)
    time.sleep(delaytime)
    i+=5
    timeg +=1
    if i == 360:
        i=0
    if timeg == 1000000:
        timeg = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


# 顯示圖片
#cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()