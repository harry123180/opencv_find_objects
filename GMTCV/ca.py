import tkinter as tk
root  = tk.Tk()
root.geometry('900x800')
root.title("操作介面")
""" GUI Function set """
btn = []
btn_context = ['Home','Detect','Next','Previous','Sucker','Move','Place']
def Home():
    print('Home')
    var = []
    for j in range(6):
        var.append(ent[j].get())
    print(var)
def Detect():
    print('Detect')
def Next():
    print('Next')
def Previous():
    print("Previous")
def Sucker():
    print("Sucker")
def Move():
    print("Move")
def Place():
    print("place")
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
        lb.append(tk.Label(root, text='x'+str(計數器), bg='green', font=('Arial', 12), width=5,
                           height=1))
        lb[j].place(x=0,y=j*30+20)
    else:
        lb.append(tk.Label(root, text='y'+str(計數器), bg='green', font=('Arial', 12), width=5,
                           height=1))
        lb[j].place(x=140,y=(j-1)*30+20)
        計數器+=1
計數器=0

root.mainloop()