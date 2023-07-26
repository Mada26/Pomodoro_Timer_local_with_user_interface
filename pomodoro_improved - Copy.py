import time
import PySimpleGUI as sg
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *

seconds = 0
timer = None
seconds_numered=0
minutes=25
count_minutes=0
timer=None
learned_minutes=0
hours=0
min=0

# Create the main window
window = tk.Tk()
# Specify screen size of the Application window
window.geometry('600x500')
# Specify application name
window.title("Pomodoro timer")

# Create the label to display the elapsed time
outputlabel = Label(font=('Arial 20 bold italic'))
outputlabel.place(x=235, y=190)
leanedtimelabel = Label(font=('Arial 20 bold italic'))
leanedtimelabel.place(x=40, y=290)

def pomodoro25():
    global seconds
    global seconds_numered
    global count_minutes
    global timer
    global learned_minutes
    global learned_minutes
    
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
            learned_minutes=learned_minutes+1


def tick():
    global timer
    global hours
    global min
    if count_minutes<minutes:
        pomodoro25()
        hours=int(learned_minutes/60)
        min=learned_minutes%60
        leanedtimelabel.config(text=f"You have learned {(hours)} hours and {(min)} minutes.\nKeep on going!")
        timer=window.after(1000, tick) # after 1,000 milliseconds, call tick() again
    elif count_minutes==minutes :
        reset_funct()
        open_popup_after_learn()
    
def start_funct():
    if count_minutes<minutes:
        start_button.configure(bg="cyan", activebackground="cyan")
        start_button["state"] = "disabled"
        short_break_button["state"] = "disabled"
        long_break_button["state"] = "disabled"
        tick()
            
    
    
    
    
def break5_short():
    global minutes
    minutes=5
    pomodoro25()


def break5_tick():
    global timer
    if count_minutes<minutes:
        break5_short()
        timer=window.after(1000, break5_tick) # after 1,000 milliseconds, call tick() again
    elif count_minutes==minutes :
        reset_funct()
        open_popup_after_break()
    
def break5_funct():
    if count_minutes<minutes:
        short_break_button.configure(bg="cyan", activebackground="cyan")
        start_button["state"] = "disabled"
        short_break_button["state"] = "disabled"
        long_break_button["state"] = "disabled"
        break5_tick()    
        
        
            
    
def open_popup_after_learn():
    win=Toplevel()
    win.wm_title("Time for a break")
    win.geometry('1000x500')
    l=Label(win,font=('Arial 40 bold italic') , text="25 MINUTES OF LEARNING \nHAVE PASSED.\nTIME FOR A BREAK!")
    l.place(x=235, y=190)
    
def open_popup_after_break():
    win=Toplevel()
    win.wm_title("Back to study")
    win.geometry('1000x500')
    l=Label(win,font=('Arial 40 bold italic') , text="YOUR BREAK IS OVER! \nBACK TO STUDY!")
    l.place(x=235, y=190)
    



def break15_long():
    global minutes
    minutes=15
    pomodoro25()
    
def break15_tick():
    global timer
    if count_minutes<minutes:
        break15_long()
        timer=window.after(1000, break15_tick) # after 1,000 milliseconds, call tick() again
    elif count_minutes==minutes :
        reset_funct()
        open_popup_after_break()

def break15_funct():
    if count_minutes<minutes:
        long_break_button.configure(bg="cyan", activebackground="cyan")
        start_button["state"] = "disabled"
        short_break_button["state"] = "disabled"
        long_break_button["state"] = "disabled"
        break15_tick()


def reset_total():
    global learned_minutes
    global hours
    global min
    reset_funct()
    learned_minutes=0   
    hours=0
    min=0 

def reset_funct():
    global seconds
    global seconds_numered
    global count_minutes
    start_button.configure(bg="red", activebackground="red")
    short_break_button.configure(bg="red", activebackground="red")
    long_break_button.configure(bg="red", activebackground="red")
    outputlabel.config(text=f"00:00")
    seconds=0
    seconds_numered=0
    count_minutes=0
    start_button["state"] = "active"
    short_break_button["state"] = "active"
    long_break_button["state"] = "active"
    window.after_cancel(timer)
    
def pause_timer():
    global seconds
    global seconds_numered
    global count_minutes
    if start_button["state"]=="disabled":
        start_button["state"] = "active"
    elif short_break_button["state"]=="disabled":
        short_break_button["state"] = "active"
    elif long_break_button ["state"]=="disabled":
        long_break_button["state"] = "active"
    window.after_cancel(timer)    
    
def close_program():   
    exit()

# Create buttons
start_button = tk.Button(window, text="25' Study", width=10, command=start_funct, bg="red")
start_button.place(x=10, y=10)

short_break_button = tk.Button(window, text="5' Break", width=10, command=break5_funct, bg="red")
short_break_button.place(x=100, y=10)

long_break_button = tk.Button(window, text="15' Break", width=10, command=break15_funct, bg="red")
long_break_button.place(x=190, y=10)

stop_button = tk.Button(window, text="Pause", width=10, command=pause_timer, bg= "pink")
stop_button.place(x=280, y=10)

reset_button = tk.Button(window, text="Reset", width=10, command=reset_total, activebackground="green")
reset_button.place(x=370, y=10)

close_button = tk.Button(window, text="Close", width=10, command=close_program)
close_button.place(x=460, y=10)



# Run the main loop

window.mainloop()