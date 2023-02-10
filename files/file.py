'''
If you are reading this, it means that you are learning Python.
So run this file!!!
'''
import os
import tkinter as t
from PIL import ImageTk, Image
from tkinter import font
import random

butonNormalColor ='#404040'
butonSelectedColor ='#303030'
i=0
def E(e):
    global i
    e.widget["bg"] = butonSelectedColor
    if (i < 3):
        x =random.uniform(0.1, 0.9)
        y = random.uniform(0.1, 0.9)
        button.place(relx=x, rely=y, anchor=t.CENTER)
        i+=1

def L(e):    e.widget["bg"] = butonNormalColor

def WinProperties(win):
    win.geometry("1000x634+300+100")
    win.title("Program")
    win.attributes("-alpha", 0.95)
    win.config(bg="#36393F")
    win.resizable(False, False)
    win.iconbitmap(False, "icon.ico")

def Present():
    print("take it")
    os.system("start parrot.bat")

win = t.Tk()
font1 = font.Font(family= "Terminal", size=16, weight="normal", slant="roman")
WinProperties(win)
canvas = t.Canvas(master=win,width=1000, height=634, background='#242424', highlightthickness=0)
canvas.place(relx=0.5,rely=0.5,anchor=t.CENTER)
image = Image.open('pxfulllogo.png')
(width, height) = image.size
#image = image.resize((int(width/1.2),int(height/1.2)))
image = ImageTk.PhotoImage(image)
imagesprite = canvas.create_image(500, 319, image=image)
button=t.Button(win,text='take a present',bg = butonNormalColor,fg = '#B4B6B9',font=font1,bd='0',activebackground=butonNormalColor,activeforeground='#474849',state=t.NORMAL,command=Present)
button.place(relx=0.5,rely=0.73,anchor=t.CENTER)
button.bind("<Enter>", E)
button.bind("<Leave>", L)
win.mainloop()
