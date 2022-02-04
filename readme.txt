The purpose of this program is to automate the process for checking your grade in ICS 33.

This program is intended to automatically:
  - Get the zip folder of grades from the ICS33 course website
  - Unzip it
  - Convert the xlsm grades file to csv
  - Read the CSV
  - Find a given hashed student ID
  - Return current grade information for that student

The python pandas library is required for this script to run correctly.

The saved_id.txt file is optional. 
To save time with repeated use, you can save your hashed student ID in this file,
and you will not be asked for it each time you run the program.
Otherwise, you'll be prompted for your student id each time.
