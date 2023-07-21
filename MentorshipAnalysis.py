'''
This is an attache project for the NCSSM Foundation. The goal was to match the names of former mentees to their residential student IDs. 
Mentee names as well as class years are held in one spreadsheed and another contains the names of former residential students, 
their class years, and residential IDs. This code works by:

1: taking user input to find the input CSV files and the desired output directory;

2: generating a list and set for each input file, containing the name and year of each student in the same format;

3: using the sets to rapidly generate a csv containing the names of mentees which the program cannot identify in the list of all students; and

4: generating a csv containing all of the matchable mentees and their associated IDs, using the indexed nature of the lists and the .index() 
method.
'''

import csv # to handle CSV input
from sys import argv # to handle user input from command line
import os # to confirm file existence
from tkinter import * # likely redundant, more testing necessary
from tkinter import filedialog # to enable users to select files via a familiar file-selection gui

#TODO add in help 
#TODO shorten

def main():
    ''' Validates that all required inputs for generation are present, asks user for them if absent

    short_path: the path of the file containing mentorship students to match to an ID list (should be first command line argument after python file name)
    long_path: the path of the file containing student IDs (should be second command line argument after python file name)
    output_dir: the output location (should be third command line argument after python file name)
    '''

    #check if expected number of arguments are present (this file's name, the two paths, and one directory)
    if len(argv)<4:
        #get short_path; keep asking if not valid selection
        short_path = filedialog.askopenfilename(initialdir=".", title="Select the CSV of Students to Match")
        while os.path.exists(short_path) != True or not(short_path.endswith(".csv")):
            short_path = filedialog.askopenfilename(initialdir=".", title="Select the CSV of Students to Match")
        
        #get long_path; keep asking if not valid selection
        long_path = filedialog.askopenfilename(initialdir=".", title="Select the CSV of Students and Their IDs")
        while os.path.exists(long_path) != True or not(long_path.endswith(".csv")):
            long_path= filedialog.askopenfilename(initialdir=".", title="Select the CSV of Students and Their IDs")
        
        #get output_dir; keep asking if not valid selection
        output_dir = filedialog.askdirectory(initialdir=".", title="Select the Output Directory")
        while not(os.path.isdir(output_dir)):
            output_dir = filedialog.askdirectory(initialdir=".", title="Select the Output Directory")
    else:
        short_path = argv[1]
        long_path = argv[2]
        output_dir = argv[3]

    #pass arguments on to generator   
    generate(short_path, long_path, output_dir)

def generate(short_path, long_path, output_dir):
    '''Generates two CSV files: one with the merged file and one with all entries that were unable to be merged
    
    short_path: the path of the file containing mentorship students to match to an ID list
    long_path: the path of the file containing student IDs
    output_dir: the output location

    Outputs are the two files mentioned above and the word "done" printed to the command line.
    Duplicates (first name, last name, and class year) are included in matched file, but only the ID of the first entry 
    to appear in the file containing IDs will be suggested.

    '''
    #inputs: the relative path of the short file, the relative path of the long file, directory of output
    with open(short_path, "r") as short_csv:
        #create list where each item corresponds to a row in the short_path file, formatted to be comparable to the information in the long_path file
        short = [f"{string.split(',')[1].strip()},{string.split(',')[2].strip()},{string.split(',')[0][-2:].strip()}" for string in short_csv.readlines()]
        #converts to a set for subtraction later and elimination of duplicates (first line from CSV, containing column names, is excluded)
        short_set = set(short[1:])

    with open(long_path, "r") as long_csv:
        #create list of lines in long_csv (will use multiple times, so done once and assigned to a variable)
        long_lines = long_csv.readlines()
        #create list where each item corresponds to a row in the long_path file, formatted to be comparable to the information in the short_path file
        long_matchable = [f"{string.split(',')[2].strip()},{string.split(',')[1].strip()},{string.split(',')[0].strip()}" for string in long_lines]
        #convert to set, for reasons stated above
        long_set = set(long_matchable)
        #get list of IDs
        IDs = [string.split(',')[4].strip() for string in long_lines]


    #file of unmatched names: create it and call it Unmatched.csv if it does not exist
    with open(output_dir+"/Unmatched.csv", "w", newline = "", encoding = "UTF8") as f:
        writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL) 
        writer.writerow(["Last","First","Class",f"Unmatched: {len(short_set-long_set)}"])
        #use set subtraction to identify all names in short_path that will not be able to be matched with those in long_path
        for i in (list(short_set-long_set)):
            writer.writerow(i.split(',')) #add line to csv


    match=[x for x in short if x in long_matchable] # creates all matches, duplicates will fall through the cracks

    #create and open the file of names with IDSs
    with open(output_dir+f'/{len(match)/(len(short)-1)}_percent_mentees_with_ids.csv', 'w', newline="", encoding='UTF8') as f:
        #create the csv writer
        writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        #write a header row to the csv file 
        writer.writerow(["Last","First","Class","ID"])
        #create a row for each matched line, adding in the corresponding ID
        for i in (match):
            row=i.split(',')
            row.append(IDs[long_matchable.index(i)])
            writer.writerow(row)
    
    #command-line feedback
    print("done")

#if called from another file, then do not run
if __name__ == "__main__":
    main()
