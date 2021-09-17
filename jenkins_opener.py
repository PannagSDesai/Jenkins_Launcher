import os 
import  threading
from tkinter import *
import tkinter as tk
import time
import sys
import os
import subprocess

def Run_War():
    #os.system('java -jar \"C:\Program Files\Jenkins\jenkins.war" > Xmp.txt')
    output = subprocess.Popen('java -jar \"C:\Program Files\Jenkins\jenkins.war"',stdout=subprocess.PIPE).communicate()[0]
    

#S = os.system('java -jar \"C:\Program Files\Jenkins\jenkins.war\"')

def browser_open():
    time.sleep(20)
    w.configure(text="Launched")
    os.system('python -m webbrowser -t ""http://localhost:8080""')

def disable_event():
        pass

def Window_generator():
    global root
    global w
    root = Tk()

    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.geometry('430x100')
    root.title("Jenkins Launcher")
    root.resizable(False, False)
    w = Label(root, text='Jenkins will launch on default browser in 20 seconds!')
    b = tk.Button(root, text='Stop', width=25, command=lambda : os._exit(1))
    
    w.grid(row=0, column=1)
    b.grid(row=1, column=1)
    root.mainloop()
    time.sleep(20)
    w.configure(text='Launched')

threads = []
worker = threading.Thread(target=Run_War,args=(),)
worker.start()
window = threading.Thread(target=Window_generator,args=(),)
window.start()
browser = threading.Thread(target=browser_open(), args=(),)
