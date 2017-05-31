import cv2
from  Tkinter import *
from thread import *
import numpy as np
cam = 1
cap = cv2.VideoCapture(cam)
cv2.startWindowThread()
cv2.namedWindow('Reading')
global croped

def mkfrm():
    window = Tk()
    window.minsize(400, 200)
    window.minsize(400, 200)
    window.title('Digital Level 0.01')
    #----Read Staff --------
    ldimg = Button(window, height=10, width=10, text='Read Staff ', command=get_elev)
    ldimg.pack()
    ldimg.place(x=10, y=10)
    global lbl
    lbl = Label(window, height=10, width=20, text='0.000')
    lbl.pack()
    lbl.place(x=150, y=10)
    window.mainloop()

def get_elev():
    print'Read .'
    tot =''
    for i in range(0,230,20):
        tt =np.sum(croped[:,i:i+19]>100)/(croped[:,i:i+19].size)

        tot =str((tt>0.5)*1)+tot
    print tot
    tot =int(tot,2)/1000.0
    lbl.configure(text=tot)


start_new_thread(mkfrm,())

while True:
    re, img = cap.read()
    if re:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        
        x = 200
        y = 200
        w = 240
        h = 6
        croped = gray[y:y+h,x:x+w]
        
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))
        cv2.rectangle(img, (x-1, y-100), (x + w+1, y + h+100), (0, 255, 0))
        cv2.imshow('Reading', img)
