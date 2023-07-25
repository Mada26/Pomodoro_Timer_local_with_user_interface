import time
import PySimpleGUI as sg
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *

seconds = 0
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
seconds_numered=0
minutes=25
count_minutes=0
timer=None
minutes_short=5
minutes_long=15

# Create the main window
window = tk.Tk()
# Specify screen size of the Application window
window.geometry('500x700')
# Specify application name
window.title("invat")

# Create the label to display the elapsed time
outputlabel = Label(font=('Arial 20 bold italic'))
outputlabel.place(x=235, y=190)

def pomodoro25():
    global click
    global seconds
    global seconds_numered
    global count_minutes
    seconds_numered=seconds%60
    
    if count_minutes < minutes :
        if count_minutes<10:
            if int(seconds_numered)<10:
                outputlabel.config(text=f"0{(count_minutes)}:0{int(seconds_numered)}")
            elif int(seconds_numered)<60:
                outputlabel.config(text=f"0{(count_minutes)}:{int(seconds_numered)}")
        elif count_minutes>=10:
            if int(seconds_numered)<10:
                outputlabel.config(text=f"{(count_minutes)}:0{int(seconds_numered)}")
            elif int(seconds_numered)<60:
                outputlabel.config(text=f"{(count_minutes)}:{int(seconds_numered)}")
        seconds +=1 
        if seconds%60==0:
            count_minutes +=1
    

def break5_short():
    global minutes
    minutes=5
    pomodoro25()
    

def break5_tick():
    global timer
    break5_short()
    if seconds > 1500:
        return
    timer=window.after(1000, tick) # after 1,000 milliseconds, call tick() again
    
def break5_funct():
    short_break_button["state"] = "disabled"
    break5_tick()    

def break15_long():
    global minutes
    minutes=15
    pomodoro25()
    
def break15_tick():
    global timer
    break15_long()
    if seconds > 1500:
        return
    timer=window.after(1000, tick) # after 1,000 milliseconds, call tick() again

def break15_funct():
    long_break_button["state"] = "disabled"
    break15_tick()

def tick():
    global timer
    pomodoro25()
    if seconds > 1500:
        return
    timer=window.after(1000, tick) # after 1,000 milliseconds, call tick() again

    
def start_funct():
    start_button["state"] = "disabled"
    tick()
    

def reset_funct():
    global seconds
    global seconds_numered
    global count_minutes
    seconds=0
    seconds_numered=0
    count_minutes=0
    start_button["state"] = "active"
    short_break_button["state"] = "active"
    long_break_button["state"] = "active"
    outputlabel.config(text=f"00:00")
    window.after_cancel(timer)
    
def close_program():   
    exit()

# Create the start and stop buttons
start_button = tk.Button(window, text="25' Study", width=10, command=start_funct)
start_button.place(x=10, y=10)
reset_button = tk.Button(window, text="Reset", width=10, command=reset_funct)
reset_button.place(x=280, y=10)
close_button = tk.Button(window, text="Close", width=10, command=close_program)
close_button.place(x=370, y=10)
short_break_button = tk.Button(window, text="5' Break", width=10, command=break5_funct)
short_break_button.place(x=100, y=10)
long_break_button = tk.Button(window, text="15' Break", width=10, command=break15_funct)
long_break_button.place(x=190, y=10)
# Run the main loop

window.mainloop()