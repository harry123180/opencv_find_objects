import numpy as np
import math

L1 = 40
L2= 30

d1 = 0
d2 =0
pi=3.14159
a1 = np.array([[math.cos(d1),-1*math.sin(d1),0,L1*math.cos(d1)],
             [math.sin(d2),math.cos(d1),0,L1*math.sin(d1)],
             [0,0,1,0],
             [0,0,0,1]])
a2 = np.array([[math.cos(d2),-1*math.sin(d2),0,L2*math.cos(d2)],
               [math.sin(d2),math.cos(d2),0,L2*math.sin(d2)],
               [0,0,1,0],
               [0,0,0,1]])

T=a1.dot(a2)
c = np.array([[256],
              [256],
              [0],
              [1]])
print(T.dot(c))
def solved2(X,Y):
    v2 = (pow(X,2)+pow(Y,2)-pow(L1,2)-pow(L2,2))/(2*L1*L2)
   # print(v2)
    
    if v2 >1 and v2 <-1:
        print ('cant do that ')
    else:
        d2 = math.acos(v2)
   

    #print("solvd2 have be run and d2 = " , d2*180/pi)
    return d2
def otherd2(d2): 
    d2= d2*-1
    #print('other')
    return d2
def solved1(X,Y,d2):
    k1 = L1+(L2*math.cos(d2))
    k2 = L2*math.sin(d2) 
    d1 = math.atan2(Y,X)-math.atan2(k2,k1)
    return d1
 
def get_d123(X,Y,fai):
    #print(X,Y,fai)
    d2 = solved2(X,Y)*180/pi
    d1 = solved1(X,Y,d2)*180/pi
    if d1 < 0:

        d2 = otherd2(d2)*180/pi
        d1 = solved1(X,Y,d2)*180/pi
        
    d3 = fai - d2-d1
    return d1,d2,d3
"""trans = np.array([[get_d123(-4,0,90)],
                  [get_d123(0,3,45)],
                  [get_d123(3,3,30)],
                  [get_d123(4,0,0)]])
    

print (trans)"""