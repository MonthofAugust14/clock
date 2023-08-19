import tkinter as tk
import time as t


def timeUpdate():
    time_string = t.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = t.strftime("%A")
    day_label.config(text=day_string)

    date_string = t.strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, timeUpdate)


window = tk.Tk()
window.title("Clock")

time_label = tk.Label(window, font=("", 50), background='grey')
time_label.pack(fill=tk.BOTH)

day_label = tk.Label(window, font=("", 50), background='grey')
day_label.pack(fill=tk.BOTH)

date_label = tk.Label(window, font=("", 50), background='grey')
date_label.pack(fill=tk.BOTH)

timeUpdate()

window.mainloop()