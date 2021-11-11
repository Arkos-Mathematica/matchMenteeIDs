# matchMenteeIDs
This is an attache project for NCSSM Foundation. The goal was to match the names of former mentees to their residential student IDs. Menee names as well as class years are held in one spreadsheed and another contains the names of former residential students, their class years, and residential IDs.
This code works by:

  1: taking user input to find the input CSV files and the desired output directory
  
  2: generating a list and set for each input file, containing the name and year of each student in the same format
  
  3: using the sets to rapidly generate a csv containing the names of mentees which the program cannot identify in the list of all students
  
  4: generating a csv containing all of the matchable mentees and their associated IDs, using the indexed nature of the lists and the .index() method

  
