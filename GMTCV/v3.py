import cv2
import tkinter 
from PIL import ImageTk
import PIL.Image

# Load an color image
#img = cv2.imread('img.png')
im  = cv2.imread('2.jpg')
def mouse(event): 
    print( "Point 1 coordinate :",event.x,event.y )
#im  = cv2.imread('2object.JPG')
#cv2.imshow('title1',im)
clone = im.copy()
im = cv2.resize(im, (500, 500), interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(7,7),0)
thresh = cv2.Canny(blurred,128,256)
#ret,binary = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY)
#_,contours,_ = cv2.findContours(thresh,cv2.PETR__EXTERNAL,cv2.CHAIN__APPROX_SIMPLE)
def onmouse(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
(cnts, _) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cnts:

        # CV2.moments會傳回一系列的moments值，我們只要知道中點X, Y的取得方式是如下進行即可。

        M = cv2.moments(c)
        if int(M["m00"])!=0:
            
            cX = int(M["m10"] / M["m00"])

            cY = int(M["m01"] / M["m00"])

 

        # 在中心點畫上黃色實心圓

        cv2.circle(im, (cX, cY), 1, (1, 227, 254), -1)
#cv2.drawContours(im,contours,-1,(0,0,255),3)"""

#cv2.imshow('title',im)
#Rearrang the color channel
b,g,r = cv2.split(im)
#cv2.imshow('123',im)
im = cv2.merge((r,g,b))

# A root window for displaying objects
root = tkinter.Tk() 

# Convert the Image object into a TkPhoto object
img2 = PIL.Image.fromarray(im)
imgtk = ImageTk.PhotoImage(image=img2) 



frame = tkinter.Frame(root, background='white', width=640, height=480) 
imLabel=tkinter.Label(frame,image=imgtk).pack()
frame.pack() # pack frame(or make frame visible) 

frame.bind('<Button-1>', mouse) 


root.mainloop() # Start the GUI