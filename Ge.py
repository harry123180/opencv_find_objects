import numpy as np
import cv2
import math
import time
import matplotlib.pyplot as plt
import random
# import serial
# ser = serial.Serial('COM1', 9600)
# import martix_test as mr
# import time
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 建立 VideoWriter 物件，輸出影片至 output.avi
# FPS 值為 20.0，解析度為 640x360
out = cv2.VideoWriter('output2.avi', fourcc, 20.0, (512, 512))

pi = 3.14159
Krad = pi / 180
Kdeg = 180 / pi
width = 512  # 圖框寬
length = 512  # 圖框長
# 建立一張 512x512 的 RGB 圖片（黑色）
img = np.zeros((width, length, 3), np.uint8)
center_point = (int(width / 2), int(length / 2))  # 定義中心點
# 將圖片用淺灰色 (200, 200, 200) 填滿
link1_length = 40  # 定義Link1的長度
link2_length = 30  # 定義Link2的長度
link1_initial = center_point
theta1 = 70
delaytime = 0.1  # 每個畫面間隔時間


def ik(x, y, theta):
    v2 = (pow(x, 2) + pow(y, 2) - pow(link1_length, 2) - pow(link2_length, 2)) / (2 * link1_length * link2_length)
    d2 = math.acos(v2)
    k1 = link1_length + link2_length * math.cos(d2)
    k2 = link2_length * math.sin(d2)
    d1 = math.atan2(y, x) - math.atan2(k2, k1)
    fai = 90 * pi / 180
    d3 = fai - d2 - d1
    return d1, d2, d3


def final_link(d1, d2):
    img.fill(200)
    # d1=d1*Krad
    # d2=d2*Krad
    a1 = np.array([[math.cos(d1 * Krad), -math.sin(d1 * Krad), 0, link1_length * math.cos(d1 * Krad)],
                   [math.sin(d1 * Krad), math.cos(d1 * Krad), 0, link1_length * math.sin(d1 * Krad)],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    a2 = np.array([[math.cos(d2), -1 * math.sin(d2), 0, link2_length * math.cos(d2)],
                   [math.sin(d2), math.cos(d2), 0, link2_length * math.sin(d2)],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    """a3 = np.array([[-1,0,0,0],
                   [0,1,0,0],
                   [0,0,-1,0],
                   [0,0,0,1]])"""
    T = a1.dot(a2)
    c = np.array([[256],
                  [256],
                  [0],
                  [1]])
    T2 = a1.dot(c)
    # T3 = T2.dot(c)
    T4 = T.dot(c)
    link1_final = (T2[0], int(512 - T2[1]))
    link2_final = (T4[0], int(512 - T4[1]))
    cv2.line(img, link1_initial, link1_final, (0, 0, 255), 1)
    cv2.line(img, link1_final, link2_final, (0, 255, 255), 1)
    # print(T.dot(c))


def link_c(d1, d2, d3):
    cv2.circle(img, (256, 256), 1, (6, 255, 255), 1)
    beta = d2 + d1  # -(90*pi/180)
    link1_final = (256 + int(link1_length * math.cos(d1)), 256 + int(link1_length * math.sin(d1)))
    link2_final = (
    int(link2_length * math.cos(beta) + link1_final[0]), int(link2_length * math.sin(beta) + link1_final[1]))
    cv2.line(img, link1_initial, link1_final, (0, 0, 255), 8)
    cv2.line(img, link1_final, link2_final, (0, 255, 255), 8)
    way.append(link2_final)
    for cnt in range(len(way)):
        cv2.circle(img, way[cnt], 1, (95, 85, 205), 1)
    # print(d1)

max_=5
min_=-5
a = np.array([[0, random.randint(min_,max_), random.randint(min_,max_), 90],
              [3, random.randint(min_,max_), random.randint(min_,max_), 45],
              [6, random.randint(min_,max_), random.randint(min_,max_), 30],
              [9, random.randint(min_,max_), random.randint(min_,max_), 0]])
print((ik(a[0][1]*10,a[0][2]*10,a[0][3])))
print((ik(a[1][1]*10,a[1][2]*10,a[1][3])))
print((ik(a[2][1]*10,a[2][2]*10,a[2][3])))
ik_list=[]

for target_deg in range(4):
    ik_list.append(ik(a[target_deg][1]*10,a[target_deg][2]*10,a[target_deg][3]))
print(ik_list[0])
#js 相當於是筆記上面的 係打矩陣12x3
js = np.array([[ik_list[0][0], ik_list[0][1], ik_list[0][2]],
               [ik_list[1][0], ik_list[1][1], ik_list[1][2]],
               [ik_list[1][0], ik_list[1][1], ik_list[1][2]],
               [ik_list[2][0], ik_list[2][1], ik_list[2][2]],
               [ik_list[2][0], ik_list[2][1], ik_list[2][2]],
               [ik_list[3][0], ik_list[3][1], ik_list[3][2]],
               [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]])





# print(js)
condition_table = np.array([[a[0][1], a[0][2], a[0][3]],  # 第一段位置左邊界
                            [a[1][1], a[1][2], a[1][3]],  # 第一段位置右邊界
                            [a[1][1], a[1][2], a[1][3]],  # 第二段位置左邊界
                            [a[2][1], a[2][2], a[2][3]],  # 第二段位置右邊界
                            [a[2][1], a[2][2], a[2][3]],  # 第三段位置左邊界
                            [a[3][1], a[3][2], a[3][3]],  # 第四段位置右邊界
                            [0, 0, 0],  # 初速度
                            [0, 0, 0],  # 末點速度
                            [0, 0, 0],  # Via1速度
                            [0, 0, 0],  # Via1加速度
                            [0, 0, 0],  # Via2速度
                            [0, 0, 0]])  # Via2加速度
dt = np.array([[a[1][0] - a[0][0], a[2][0] - a[1][0], a[3][0] - a[2][0]]])
# print(dt[0][1])
dt1 = dt[0][0]
dt2 = dt[0][1]
dt3 = dt[0][2]
T = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, dt1, pow(dt1, 2), pow(dt1, 3), 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, dt2, pow(dt2, 2), pow(dt2, 3), 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, dt3, pow(dt3, 2), pow(dt3, 3)],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2 * dt3, 3 * pow(dt3, 2)],
              [0, 1, 2 * dt1, 3 * pow(dt1, 2), 0, -1, 0, 0, 0, 0, 0, 0],
              [0, 0, 2, 6 * dt2, 0, 0, -2, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 2 * dt2, 3 * pow(dt2, 2), 0, -1, 0, 0],
              [0, 0, 0, 0, 0, 0, 2, 6 * dt2, 0, 0, -2, 0]])
inverse_T = np.linalg.inv(T)#T的逆矩陣
A = inverse_T.dot(condition_table)
Ajs = inverse_T.dot(js)
#print(Ajs)
check_a = np.array([[0, 0, 0, 0]])
i = 0


def put_target(a):  # 放置目標點位
    """a=np.array([[0,-4,0,90],
            [2,0,3,45],
            [4,3,3,30],
            [7,4,0,0]])"""
    zu = 8
    #print("大小",type(a.shape[1]))
    for point_nun in range(a.shape[1]):
        #print(a[point_nun][1])
        #print((256 + a[point_nun][2]*10, 256 + a[point_nun][3]*10))
        cv2.circle(img, (256 + int(a[point_nun][1]*10), 256 + int(a[point_nun][2]*10)), 1, (255, 255, 255), zu)


def polynomials(genre, N, jikan_):  # 多項通式 給定類型/段數/時間 計算出當前角度
    # genre=0 = d1 N = 0 =第一段
    # genre=1 = d2 N = 1 =第二段
    # genre=2 = d3 N = 2 =第三段
    global check_a

    sita = Ajs[N][genre] + Ajs[N + 1][genre] * jikan_ + Ajs[N + 2][genre] * pow(jikan_, 2) + Ajs[N + 3][genre] * pow(
        jikan_, 3)

    #print( Ajs[N][genre],Ajs[N + 1][genre],Ajs[N + 2][genre],Ajs[N + 3][genre])

    return sita


def cur_deg(timer):
    jikan = timer * delaytime  # 算現在運行到第幾秒ㄌ

    if jikan <= a[1][1]:  # 第一段
        i1 = polynomials(0, 0, jikan)
        i2 = polynomials(1, 0, jikan)
        i3 = polynomials(2, 0, jikan)
        link_c(i1, i2, i3)
    elif jikan > a[1][1] and jikan <= a[1][2]:  # 第二段
        i1 = polynomials(0, 4, jikan)
        i2 = polynomials(1, 4, jikan)
        i3 = polynomials(2, 4, jikan)
        link_c(i1, i2, i3)
    elif jikan > a[1][2] and jikan <= a[1][3]:  # 第三段
        i1 = polynomials(0, 8, jikan)
        i2 = polynomials(1, 8, jikan)
        i3 = polynomials(2, 8, jikan)
        link_c(i1, i2, i3)


t_table = np.array([0])
pos = np.array([[2.3728, 1.9552, -2.7572]])
way = []
value = 0
while (True):
    # print('tset')
    img = np.zeros((width, length, 3), np.uint8)
    # link_c(i,0,0)
    # line = ser.readline()
    # 在圖片上畫一條紅色的對角線，寬度為 5 px
    put_target(a)
    # print(i)
    # cur_deg(i)
    jikan = i * delaytime  # 算現在運行到第幾秒ㄌ
    # print(a[1][0])
    if jikan <= a[1][0]:  # 第一段
        # print(a[1][0])
        i1 = polynomials(0, 0, jikan)
        i2 = polynomials(1, 0, jikan)
        i3 = polynomials(2, 0, jikan)
        # print(i1*Kdeg,i2*Kdeg,i3*Kdeg)
        # link_c(i1,i2,i3)
    elif jikan > a[1][0] and jikan <= a[2][0]:  # 第二段
        # print('end')
        jikan_m = jikan - a[1][0]
        i1 = polynomials(0, 4, jikan_m)
        i2 = polynomials(1, 4, jikan_m)
        i3 = polynomials(2, 4, jikan_m)
        # link_c(i1,i2,i3)
    elif jikan > a[2][0] and jikan <= a[3][0]:  # 第三段
        jikan_m = jikan - a[2][0]
        i1 = polynomials(0, 8, jikan_m)
        i2 = polynomials(1, 8, jikan_m)
        i3 = polynomials(2, 8, jikan_m)
    if jikan == a[1][0]:
        genre = 0
        N = 0#第一段
        #print((i1, i2, i3))
        check_a = np.append(check_a, [[Ajs[N][genre], Ajs[N + 1][genre], Ajs[N + 2][genre], Ajs[N + 3][genre]]], axis=0)
        # print(i1,i2,i3)
    elif jikan == a[2][0]:
        genre = 0
        N = 4#第五段
        #print((i1, i2, i3))
        check_a = np.append(check_a, [[Ajs[N][genre], Ajs[N + 1][genre], Ajs[N + 2][genre], Ajs[N + 3][genre]]], axis=0)
        # print(i1,i2,i3)
    elif jikan == a[3][0]:
        genre = 0
        N = 8
        #print((i1, i2, i3))
        #print([[Ajs[N][genre], Ajs[N + 1][genre], Ajs[N + 2][genre], Ajs[N + 3][genre]]])
        # print(i1,i2,i3)

    pos = np.append(pos, [[i1 * Kdeg, i2 * Kdeg, i3 * Kdeg]], axis=0)
    t_table = np.append(t_table, [[jikan]])
    """judge = ((int(line)+1))-512


    if judge <-10:
        value -= 3
    elif judge > 10:
        value += 3
    print(value)"""

    # value*Krad
    link_c(i1, i2, i3)
    # print(int(line))
    i += 1
    h_flip = cv2.flip(img, -1)
    cv2.imshow('Window', h_flip)

    time.sleep(delaytime)
    out.write(h_flip)

    if i >= 700:
        i = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        fig = plt.figure()
        plt.plot(t_table, pos[:, 0], color='blue', lw=3, label='$sita1$')
        plt.plot(t_table, pos[:, 1], color='red', lw=3, label='$sita2$')
        plt.plot(t_table, pos[:, 2], color='black', lw=3, label='$sita3$')
        plt.xticks(fontsize=1)
        plt.yticks(fontsize=1)
        plt.grid()
        plt.show()
        break




# 顯示圖片
# cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
    if jikan == a[1][0]:

        #print(i1,i2,i3)
    elif jikan == a[2][0]:

        #print(i1,i2,i3)
    elif jikan == a[3][0]:
        #print(i1,i2,i3)
"""