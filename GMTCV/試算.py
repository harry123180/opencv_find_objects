point = [180,294]

rs = []

rs.append(point[0]*0.571-103.28)
rs.append(point[1]*0.541+48.602)
print(rs)
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
window = tk.Tk()
window.geometry("500x500")

def image():
    cap = cv2.VideoCapture(0)
    def video_button():
        ret, frame = cap.read()
        if (ret == True):
            image_canvas.delete("all")
            video_frame = cv2.cvtColor(cv2.resize(frame, (530,315)), cv2.COLOR_BGR2RGB)
            img_frame = ImageTk.PhotoImage(Image.fromarray(video_frame))
            image_canvas.create_image(0,0,anchor = NW, image = img_frame)
            image_canvas.img = img_frame
            #每30毫秒重置副程式
            image_canvas.after(30, video_button)
        cap.release()
    video_button()
#建立canvas 顯示圖片
image_canvas = tk.Canvas(window, bg = '#333f50',height = 315, width = 480)
image_canvas.place(x = 10, y = 5)
#建立讀取讀片按鈕
button = tk.Button(window, text = "讀入本機攝像頭", width = 12, height = 2, command = image)
button.place(x = 400, y = 465)
window.mainloop()