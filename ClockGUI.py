from tkinter import *
from time import *
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_String = strftime("%A")
    day_label.config(text=day_String)

    date_String = strftime("%B %d, %Y")
    date_label.config(text=date_String)

    window.after(1000,update)


window = Tk()
window.title("Clock")
icon = PhotoImage(file='eu.png')
window.iconphoto(True, icon)

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",25))
day_label.pack()

date_label = Label(window,font=("Ink Free",25))
date_label.pack()

update()

window.mainloop()
