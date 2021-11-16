import csv
from sys import argv
import os
from tkinter import *
from tkinter import filedialog
#TODO add in help 
#TODO we somehow have more names unmatched now than before (it's not spacing). It seems like we were previously matching things that we shouldn't have
#TODO shorten

#inputs: the relative path of the short file, the relative path of the long file, directory of output
if len(argv)<4:
    short_path = filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students to Match")
    while os.path.exists(short_path) != True or not(short_path.endswith(".csv")):
        short_path = filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students to Match")
    
    long_path = filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students and Their IDs")
    while os.path.exists(long_path) != True or not(long_path.endswith(".csv")):
        long_path= filedialog.askopenfilename(initialdir="..", title="Select the CSV of Students and Their IDs")
    output_dir = filedialog.askdirectory(initialdir="..", title="Select the Output Directory")
    while not(os.path.isdir(output_dir)):
        output_dir = filedialog.askdirectory(initialdir="..", title="Select the Output Directory")
else:
    short_path = argv[1]
    long_path = argv[2]
    output_dir = argv[3]



with open(short_path, "r") as short_csv:
    short = [f"{string.split(',')[1].strip()},{string.split(',')[2].strip()},{string.split(',')[0][-2:].strip()}" for string in short_csv.readlines()]
    short_set = set(short[1:])

with open(long_path, "r") as long_csv:
    long_lines = long_csv.readlines()
    long_matchable = [f"{string.split(',')[2].strip()},{string.split(',')[1].strip()},{string.split(',')[0].strip()}" for string in long_lines]
    long_set = set(long_matchable)
    IDs = [string.split(',')[4].strip() for string in long_lines]


#file of unmatched names
with open(output_dir+"/Unmatched.csv", "w", newline = "", encoding = "UTF8") as f:
    writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL) 
    writer.writerow(["Last","First","Class",f"Unmatched: {len(short_set-long_set)}"])
    for i in (list(short_set-long_set)):
        writer.writerow(i.split(','))


match=[x for x in short if x in long_matchable]

#file of names with IDs
# open the file in the write mode
with open(output_dir+f'/{len(match)/len(short)}_percent_mentees_with_ids.csv', 'w', newline="", encoding='UTF8') as f:
    # create the csv writer
    writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
    # write a row to the csv file 
    writer.writerow(["Last","First","Class","ID"])
    for i in (match):
        row=i.split(',')
        row.append(IDs[long_matchable.index(i)])
        writer.writerow(row)
