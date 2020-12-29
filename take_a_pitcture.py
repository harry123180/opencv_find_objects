# coding=utf-8
import cv2

video_capture = cv2.VideoCapture(0) # 改變括號內數字可選擇webcam

i = 0;
while True:
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
    elif cv2.waitKey(1) & 0xFF == ord('s'): # 按s存檔
        i = i + 1;
        cv2.imwrite('photo' + str(i) + '.png',frame)
        print ('儲存:','photo' + str(i) + '.png')

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()