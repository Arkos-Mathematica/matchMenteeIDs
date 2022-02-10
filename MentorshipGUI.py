from pydoc import text
from tkinter import *
import tkinter
from tkinter import filedialog
import os
from MentorshipAnalysis import generate

def set_short():
    global short_path
    short_path = filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students to Match")
    while os.path.exists(short_path) != True or not(short_path.endswith(".csv")):
        print('error: invalid filetype')
        short_path = filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students to Match")
    short_select.config(text=short_path)

def set_long():
    global long_path
    long_path = filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students and Their IDs")
    while os.path.exists(long_path) != True or not(long_path.endswith(".csv")):
        print('error: invalid filetype')
        long_path= filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students and Their IDs")
    long_select.config(text=long_path)

def set_dir():
    global output_dir
    output_dir = filedialog.askdirectory(initialdir="..", title="Select the Output Directory")
    while os.path.exists(output_dir+r"/Unmatched.csv"):
        print('error: clear old versions out of folder or rename them')
        output_dir = filedialog.askdirectory(initialdir="..", title="Select the Output Directory")
    output_select.config(text=output_dir)

def process(short_path, long_path, output_dir):
    generate(short_path, long_path, output_dir)
    confirm.config(text="Complete!")

top = Tk()
top.configure(bg="#FFFFFF")

long_path = ""
short_path = ""
output_dir = ""

title = Label(top, text = 'Mentorship Analysis UI', font=("Calibri", 44), fg="#346094", bg="#FFFFFF")
title.pack()

short_label = Label(top, text='Please select the CSV file containing students to match:', font=("Calibri", 15), bg="#FFFFFF")
short_select = Label(top, height=1, font=("Calibri", 10), text = short_path, bg="#FFFFFF")
short_button = Button(top, text ="select", relief=RAISED, command=set_short, bg="#99caea")


long_label = Label(top, text='Please select the CSV file containing students and their respective IDs:', font=("Calibri", 15), bg="#FFFFFF")
long_select = Label(top, height=1, font=("Calibri", 10), text=long_path, bg="#FFFFFF")
long_button = Button(top, text ="select", relief=RAISED, command=set_long, bg="#99caea")

output_label = Label(top, text='Please select the directory to output to:', font=("Calibri", 15), bg="#FFFFFF")
output_select = Label(top, height=1, font=("Calibri", 10), text = output_dir, bg="#FFFFFF")
output_button = Button(top, text ="select  ", relief=RAISED, command=set_dir, bg="#99caea")

spacer = Label(top, text="", font=("Calibri", 10), bg="#FFFFFF")
submit_button = Button(top, text='Process!', relief = RAISED, font=("Calibri", 15), command=lambda: process(short_path, long_path, output_dir), bg="#d57e00")
confirm = Label(top, text="", font=("Calibri", 10), bg="#FFFFFF")

short_label.pack()
short_select.pack()
short_button.pack()
long_label.pack()
long_select.pack()
long_button.pack()
output_label.pack()
output_select.pack()
output_button.pack()
spacer.pack()
submit_button.pack()
confirm.pack()

top.mainloop()

