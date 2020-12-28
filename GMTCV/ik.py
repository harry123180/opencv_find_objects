import math
l1 =  4
l2 =  3
pi = 3.14159
x =-4
y = 0
theta = 90
Kdeg = 180/pi
def ik(x,y,theta):
    v2 = (pow(x,2)+pow(y,2)-pow(l1,2)-pow(l2,2))/(2*l1*l2)
    d2 = math.acos(v2)
    k1 = l1+l2*math.cos(d2)
    k2 = l2*math.sin(d2)
    d1 = math.atan2(y,x)-math.atan2(k2,k1)
    fai = theta*pi/180
    d3 = (fai-d2-d1)
    #beta = (d2*180/pi)+(d1*180/pi)
    #gama=d3+beta
    #print('gama= ' ,gama)
    #d1 = d1*Kdeg
    #d2 = d2*Kdeg
    #d3 = d3*Kdeg
    return d1,d2,d3

print(ik(-4,0,90))
