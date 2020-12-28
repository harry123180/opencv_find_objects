import tkinter as tk
 
#from tkFileDialog import askopenfilename 
import tkinter.filedialog as tt
from PIL import Image,ImageTk

if __name__ == "__main__": 
    root = tk.Tk() 

    #setting up a tkinter canvas with scrollbars 
    frame = tk.Frame(root, bd=2, relief=tk.SUNKEN) 
    frame.grid_rowconfigure(0, weight=1) 
    frame.grid_columnconfigure(0, weight=1) 
    xscroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL) 
    xscroll.grid(row=1, column=0, sticky=tk.E+tk.W) 
    yscroll = tk.Scrollbar(frame) 
    yscroll.grid(row=0, column=1, sticky=tk.N+tk.S) 
    canvas = tk.Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set) 
    canvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W) 
    xscroll.config(command=canvas.xview) 
    yscroll.config(command=canvas.yview) 
    frame.pack(fill=tk.BOTH,expand=1) 

    #adding the image 
    File = tt.askopenfilename(parent=root, initialdir="C:/User/user/Desktop/Python/GMTCV/2.jpg",title='Choose an image.') 
    
    img = ImageTk.PhotoImage(Image.open(File)) 
    canvas.create_image(0,0,image=img,anchor="nw") 
    canvas.config(scrollregion=canvas.bbox(tk.ALL)) 

    #function to be called when mouse is clicked 
    def printcoords(event): 
     #outputting x and y coords to console 
     print (event.x,event.y) 
    #mouseclick event 
    canvas.bind("<Button 1>",printcoords) 

    root.mainloop() 