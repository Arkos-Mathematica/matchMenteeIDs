import numpy as np
import csv
from sys import argv
import os
#TODO add in help 
#TODO we somehow have more names unmatched now than before (it's not spacing). It seems like we were previously matching things that we shouldn't have
#TODO shorten

#inputs: the relative path of the short file, the relative path of the long file, directory of output
if len(argv)<4:
    print('Please indicate the appropraite path or directory. Both relative and absolute paths are accepted.')
    short_path = input('The name (with extension) of the csv with mentee names (include the relative path if in a different folder): ')
    while os.path.exists(short_path) != True or not(short_path.endswith(".csv")):
        short_path= input ('Sorry, that isn\'t a valid path and name of a csv file. Please input one: ')
    long_path = input('The name (with extension) of the csv with student IDs (include the relative path if in a different folder): ')
    while os.path.exists(long_path) != True or not(long_path.endswith(".csv")):
        long_path= input ('Sorry, that isn\'t a valid path and name of a csv file. Please input one: ')
    output_dir = input('The path to the folder where you want the output to go: ')
    while not(os.path.isdir(output_dir)):
        output_dir = input ('Sorry, that isn\'t a valid path to a directory. Please input one: ')
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


match=[x for x in short if x in long_matchable]

#file of unmatched names
with open(output_dir+"/Unmatched.csv", "w", newline = "", encoding = "UTF8") as f:
    writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL) 
    writer.writerow(["Last","First","Class",f"Unmatched: {len(short_set-long_set)}"])
    for i in (list(short_set-long_set)):
        writer.writerow(i.split(','))




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
