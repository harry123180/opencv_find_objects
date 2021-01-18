import cv2
import numpy as np
#import argparse
def get_gray(img):#灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    return gray

def get_blurred(img):#模糊化
    gray = get_gray(img)
    blurred = cv2.GaussianBlur(gray,(7,7),0)
    
    return blurred

def get_binary(img):#黑白化
    blur= get_blurred(img)
    ret,binary = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
    
    return binary
def get_contours(img):#獲取輪廓
    binary = get_binary(img)
    contours,hierachy = cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    
    return contours
def draw_contours(img):#畫輪廓
    
    contours = get_contours(img)
    cv2.drawContours(img,contours,-1,(0,0,255),3)
    
    return None


def all_contour_X_Y(img):#要返回所有輪廓的X，Y值
    
    g_img = get_gray(img)
    binary_img = get_binary(g_img)
    cnt = get_contours(binary_img)
    draw_contours(img,cnt,-1(0,0,255),3)

    return img




    
"""    lefttext = 'L'+str(Num+1)
    cv2.putText(im, lefttext, (leftmost), cv2.FONT_HERSHEY_DUPLEX,1, (0, 255, 255), 1, cv2.LINE_AA)
    print (leftmost)# show point and check 
    """
"""
    print (centerX)
    print (centerY)
    
    print ("X=",leftY[0]/(-1*mRB[0]))
    print ('left point ',left_point)
    print ('bottom point ',bottom_point)
    print ('right point ',right_point)
    print( 'mRb' ,mRB) #把numpy轉換成list
    print('mLB',mLB)
    """
   # cv2.imshow('123',binary)
    
    #cv2.waitKey()
#im  = cv2.imread('2object.JPG')
im  = cv2.imread('photo1.png')
im = cv2.resize(im, (1000, 1000), interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(13,13),0)
ret,binary = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY)
low_threshold = 1
high_threshold = 10
edges = cv2.Canny(binary, low_threshold, high_threshold)
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations = 1)
erosion = cv2.erode(dilation, kernel, iterations = 1)
contours,hierachy = cv2.findContours(erosion,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(im,contours,-1,(0,0,255),3)
cnt_count = []
#cnt_count_index = cnt_count -1
centerX =[]
centerY =[]
for cnt in range(len(contours)):
    epsilon = 0.01 * cv2.arcLength(contours[cnt], True)
    approx = cv2.approxPolyDP(contours[cnt], epsilon, True)
    #print(len(approx))
    area = cv2.contourArea(contours[cnt])
    if( area >1000):
        print('輪廓號=',cnt,'角點數=', len(approx))
        cv2.drawContours(im, contours[cnt], -1, (255, 255, 255), 3)
        M = cv2.moments(contours[cnt])
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # print(area)
            cnt_count.append(cnt)
            centerX.append(cX)
            centerY.append(cY)
            #cnt_count = cnt_count + 1
            text = str(cnt)
            cv2.putText(im, text, (cX + 5, cY), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.circle(im, (cX, cY), 10, (1, 227, 254), -1)


left_point = [] #define for save 4 most point
right_point = []
top_point = []
bottom_point = []
##############################################

mRB=[]
mLB=[]
for Num in range(len(cnt_count)):
    cnt = contours[cnt_count[Num]]
    leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
    rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
    topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
    bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
    ## get 4 most point 
    cv2.circle(im,leftmost,10,[0,90,255],-1)
    cv2.circle(im,topmost,10,[0,90,255],-1)
    cv2.circle(im,rightmost,10,[0,90,255],-1)
    cv2.circle(im,bottommost,10,[0,90,255],-1)
    ## draw 4 most point 
    left_point.append(leftmost)
    right_point.append(rightmost)
    top_point.append(topmost)
    bottom_point.append(bottommost)
    ## tuple type change to list type
    npleft = np.array(left_point)
    npright = np.array(right_point)
    #nptop = np.array(top_point)
    npbottom = np.array(bottom_point)
        ## change list to np.array
    leftX = list(npleft [ : ,  0 ] )
    rightX= list(npright [ : ,  0 ] )
        #topX = list(nptop [ : ,  0 ] )
    bottomX=list(npbottom [ : ,  0 ] )
    leftY=list(npleft [ : ,  1 ] )
    rightY=list(npright [ : ,  1 ] )
        #topY=list(nptop [ : ,  1 ] )
    bottomY=list(npbottom [ : ,  1 ] )
    mRB.append((bottomY[Num]-rightY[Num])/(bottomX[Num]-rightX[Num]))
    mLB.append((bottomY[Num]-leftY[Num])/(bottomX[Num]-leftX[Num]))
    X_position=leftY[0]/(-1*mRB[0])
    """
print (centerX)
print (centerY)
    
print ("X=",leftY[0]/(-1*mRB[0]))
print ('left point ',left_point)
print ('bottom point ',bottom_point)
print ('right point ',right_point)
print( 'mRb' ,mRB) #把numpy轉換成list
print('mLB',mLB)
"""
cv2.imshow('edges',edges)
cv2.imshow('im',im)
cv2.imshow('bin',binary)
    
cv2.waitKey()