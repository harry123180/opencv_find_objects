import matplotlib.pyplot as plt
import time
#plt.ion() #开启interactive mode 成功的关键函数
#plt.figure(1)
e=2.71828459045
A=2
K=150
deg=[]
amp=1
round_=0
ts=20
OK=False
maxOS=10
AAA=[]
TG=[]
for i in range(0,10,1):
    for ms in range(100):
        mt=i+(ms/100)
        TG.append(1)
plt.xlim((0, 1000)) 
plt.ylim((0, 1.1))
plt.axvline(200, 0.0, 1.1, linestyle= '--')

def modle(t,ampx,p,d):
    
    sisu =pow((pow((A+d*K),2)-(4*K*p)),0.5)
    addpow = ((1/2)*sisu)-(A/2)-(d*K/2)
    antipow = (-1/2*sisu)-(A/2)-(d*K/2)
   
    one = -A*pow(e,antipow*t)
    two=A*pow(e,addpow*t)
    three = d*K*pow(e,antipow*t)
    four = d*K*pow(e,addpow*t)
    five= sisu*pow(e,antipow*t)
    six=sisu*pow(e,addpow*t)
   
    y = ampx*(1-((one+two+three-four+five+six)/(2*sisu)))
    return float(y.real)
def check(target,y):
    top=target*(1+(maxOS/100))
    down = target*(1+(maxOS/200))
    if y<top and y > down :
        state = True
    elif y>top or y < down:
        state = False
    return state
"""

for i in range(0,10,1):
    for ms in range(100):
        mt=i+(ms/100)
        if i<2:
            print(mt)
        
        AAA.append(modle(mt,1,0.43,0.005))
        TG.append(1)
plt.xlim((0, 10)) 
plt.ylim((0, 1.1))
plt.axvline(2, 0.0, 1.1, linestyle= '--')
plt.plot(AAA)
plt.plot(TG)



"""

for findp in range(70,100,1):
    if (OK==True):
        break
    for findd in range(0,1000,1):
        if (OK == True):
            break
        p=findp/100
        d=findd/1000
        round_+=1
        print('round=',round_)
        
        for i in range(0,10,1):
            for ms in range(100):
                mt=i+(ms/100)
                deg.append(modle(mt/10,1,p,d))
        if (check(1,max(deg))==True and int(deg.index(max(deg)))<=200):
            print(max(deg))
            print('ts=',int(deg.index(max(deg)))/100)
            print ('Kp=',p)
            print('Kd=',d)
            #plt.clf()
                 
            #plt.plot(deg) # 一条轨迹
            #plt.pause(0.001)
            plt.plot(deg)
            plt.plot(TG)
            OK=True
            print(OK)
        deg.clear()

 
print('end!')
#print(max(deg))
