import os 
import  threading
from tkinter import *
import tkinter as tk
import time
import sys
import os
import subprocess

""""The script helps you to launch the Jenkins withour having to navigate to the war file path and launching there from the CMD with the help of command, 
Rather quickly launch it with the help of predefined workflow sophisticated enough to automate the launching process. Depending on your setup, you may ha
-ve to change the path of .war file. The jenkins will be launched on your default browser with new tab. The Window can be minimised to taskbar ( Need to workout to
check if possible to minimise it to notification center in Windows 10."""

def Run_War():
     #Run the war file with regular command with the help of subpocess, 
     #NOTE: CHange the path if war file exists somewhere else on your system.
     output = subprocess.Popen('java -jar \"C:\Program Files\Jenkins\jenkins.war"',stdout=subprocess.PIPE).communicate()[0] 
    

def browser_open():
    #Open browser after 20 seconds to ensure the jenkins is up.
    #Anyone who knows how to log live strings from the command console output can modify the code to add feature of launching jenkins on browser only when jenkins is fully up.
    time.sleep(20)
    w.configure(text="Launched")
    os.system('python -m webbrowser -t ""http://localhost:8080""') #Launching Jenkins in dafault browser with the help of system using regular command.
    
def disable_event():  # Bypass "X" button event from the Title bar.
        pass

def Window_generator(): #Window designer and launcher, you can customise as per your convenience.
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
    
#Threading will be used as Tkinter window may become unresponsive when Run_war doesn't return anything.

worker = threading.Thread(target=Run_War,args=(),)          #Create thread for running war file 
worker.start()
window = threading.Thread(target=Window_generator,args=(),)   #Create thread for window generator.
window.start()
browser = threading.Thread(target=browser_open(), args=(),)    #create thread for browser.
