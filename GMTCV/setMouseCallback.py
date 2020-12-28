import cv2

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(im, (x, y), 1, (255, 255, 255), thickness = -1)
        cv2.putText(im, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255, 255, 255), thickness = 1)
        cv2.imshow("image", im)

im = cv2.imread("1.jpg")
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
        cv2.drawContours(im,c,-1,(0,0,255),3)
cv2.namedWindow("image")
cv2.imshow("image", im)
cv2.resizeWindow("image", 500, 500)
cv2.setMouseCallback("image", mouse)

cv2.waitKey(0)
cv2.destroyAllWindows()