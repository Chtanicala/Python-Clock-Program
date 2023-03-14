from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window = Tk()

window.geometry("500x250")
window.title("Digital Clock")

Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.columnconfigure(window,0,weight=1)

time_label = Label(window,
                   font=("Arial",50),
                   fg="red",
                   background="black")
time_label.grid(row=0,column=0,sticky="NSEW")

day_label = Label(window,
                   font=("Arial",50),
                   fg="green",
                   background="black")
day_label.grid(row=1,column=0,sticky="NSEW")

date_label = Label(window,
                   font=("Arial",50),
                   fg="blue",
                   background="black")
date_label.grid(row=2,column=0,sticky="NSEW")

update()

window.mainloop()