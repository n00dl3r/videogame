""" 
Using the two blocks of code below, create a window that creates a folder, and creates a file with content from the window.

"""
# https://automatetheboringstuff.com/2e/chapter9/

# Using pathlib and OS to create directories and add files
from pathlib import Path
import os

# using tkinter to create a usable window
#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

#Define a function to show a message
def myclick():
    print(Path.cwd())

    os.chdir('C:/github')

    print(Path.cwd())

    os.makedirs('C:/github'+(entry.get()))

    os.chdir('C:/github'+(entry2.get()))

    print(Path.cwd())

    p = Path('spam.txt')

    p.write_text('C:/github'+(entry3.get()))

    p.read_text()

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
entry = ttk.Entry(frame, width= 40)
entry2 = ttk.Entry(frame, width= 40)
entry3 = ttk.Entry(frame, width= 40)
entry.insert(INSERT, "Enter Your Name...")
entry2.insert(INSERT, "Enter Your File Name...")
entry3.insert(INSERT, "Enter File Data...")
entry.pack()
entry2.pack()
entry3.pack()

userInput = entry3

#Create a Button
ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
win.mainloop()