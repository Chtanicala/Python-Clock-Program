from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    label_width_array = [len(time_string),
             len(day_string),
             len(date_string)]

    time_label.config(width=max(label_width_array))
    day_label.config(width=max(label_width_array))
    date_label.config(width=max(label_width_array))

    window.after(1000,update)

window = Tk()



time_label = Label(window,
                   font=("Arial",50),
                   fg="red",
                   background="black",
                   width=7)
time_label.pack()

day_label = Label(window,
                   font=("Arial",50),
                   fg="green",
                   background="black",
                   width=7)
day_label.pack()

date_label = Label(window,
                   font=("Arial",50),
                   fg="blue",
                   background="black",
                   width=7)
date_label.pack()

update()

window.mainloop()