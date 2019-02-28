import pyautogui
from tkinter import *
import webbrowser
import time
import sys
import configparser, os
import pynput

from pynput.keyboard import Key, Controller

config = configparser.RawConfigParser()
permvar = "C:\\Users\\Ömer Aramaz\\PycharmProjects\\NewBot\\permvar.ini"
exx1 = "C:\\Users\\Ömer Aramaz\\PycharmProjects\\NewBot\\permvar.ini"
config.read(permvar)
id_name = config.get('takeid', 'id_name')
keyboard = Controller()

root = Tk()
root.title("NewBot")
root.geometry("500x500")
root.resizable(0, 0)
pyautogui.FAILSAFE = False

def onb():
    pyautogui.click(x=0, y=0)

def hitsro_webpage():
    config.read(permvar)
    id_name = config.get('takeid', 'id_name')
    id_count = config.get('takeid', 'id_count')
    email_name = config.get('takeid', 'email_name')
    email_count = config.get('takeid', 'email_count')
    web_password = config.get('takeid', 'web_password')
    print(id_name + id_count + email_name + email_count + web_password)
    webbrowser.open('http://www.hitsro.com/homepage')
    time.sleep(2)
    pyautogui.click(x=1379, y=681)
    time.sleep(0.1)
    pyautogui.click(x=954, y=405)
    keyboard.type(id_name)
    keyboard.type(id_count)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(web_password)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(web_password)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(email_name + email_count + "@gmail.com")
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    id_count = int(id_count) + int(1)
    email_count = int(email_count) + int(1)
    config.set('takeid', 'id_count', id_count)
    config.set('takeid', 'email_count', email_count)
    with open('C:\\Users\\Ömer Aramaz\\PycharmProjects\\NewBot\\permvar.ini', 'w') as configfile:
        config.write(configfile
    print(id_count)



def open_id():
    time.sleep(1)



button1 = Button(root, text="Click", height=3, width=5, command=onb)
button2 = Button(root, text="Hitsro", height=3, width=5, command=hitsro_webpage)
button3 = Button(root, text="Open ID", height=3, width=5, command=open_id)

button1.place(x=10, y=10)
button2.place(x=60, y=10)
button3.place(x=110, y=10)

root.mainloop()