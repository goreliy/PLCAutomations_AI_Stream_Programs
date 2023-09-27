# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:59:43 2023

@author: gorelyi
"""

import tkinter as tk
import json

def save_values(event=None):
    values = {
        "slider1": slider1.get(),
        "slider2": slider2.get(),
        "slider3": slider3.get(),
        "slider4": slider4.get(),
        "slider5": slider5.get()
    }
    with open("values.json", "w") as outfile:
        json.dump(values, outfile)

def start_recording():
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    circle_canvas.itemconfigure(circle_item, fill="green")

def stop_recording():
    stop_button.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)
    circle_canvas.itemconfigure(circle_item, fill="red")

root = tk.Tk()

slider1 = tk.Scale(root, from_=-100, to=100, orient=tk.HORIZONTAL, command=save_values)
slider1.pack()

slider2 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=save_values)
slider2.pack()

slider3 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=save_values)
slider3.pack()

slider4 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=save_values)
slider4.pack()

slider5 = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=save_values)
slider5.pack()

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack()

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording, state=tk.DISABLED)
stop_button.pack()

circle_canvas = tk.Canvas(root, width=50, height=50)
circle_item = circle_canvas.create_oval(0, 0, 50, 50, fill="red")
circle_canvas.pack()

root.mainloop()