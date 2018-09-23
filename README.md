<h1 align="center">
CCA Allocation for Singapore Schools
</h1>

A CCA allocation program coded in **Python**. 
Made by Gerald Nyeo And Noah "dafatskin" Lim.

## Introduction
This project is commissioned by Raffles Institution, Singapore, first for grading for our Computer Elective Program(CEP) and hopefully for proper use in the school's allocation system.

The current build status of this project is: 
### FINISHED 

## Features
- Relatively quick runtime that can deal with any amount of data.
- Easy usage and simple interface.
- Reduces time and effort needed to finish this task.

## Installation
This program uses a .py file to run so [Python](https://www.python.org/downloads/) should be downloaded to access and run the file.

Open up Windows Powershell or Command Prompt and enter the following:
1. python -m pip install -U matplotlib
2. pip install python-docx

Click on the button shown and download the entire repository.
![Download](https://github.com/dafatskin/CEP_FinalProject_2018/blob/master/Screenshots/Download.PNG?raw=true)

The necessary programs should be installed and are ready to be used.

## How to Use?
Paste your excel sheet into the folder. Make sure that all spaces in the name of the file is replaced with an underscore (i.e "_")
Ensure that your file is saved in the .xlsx format

### Configure excel sheet
Download draft.xlsx and follow the format given in the excel sheet. 

### Edit config_file.txt
config_file.txt has four parts to edit based on the configuration of the excel file.-

1. The first part is in "file names". It will be in the format: unallocated:(FileName).
Change the (FileName) to the name of your excel sheet.
E.g if your excel sheet is named: "an excel sheet", it would look like this:
unallocated:an_excel_sheet

2. The second part is in "data formats". It consists of multiple elements in the format: 
(TabName):(Top Left-most cell)-(Bottom Right-most cell)-(Name of Header for Student ID)
Change the values accordingly.

**Example**
This is the top left hand column.(Circled)
![Top Left](https://github.com/dafatskin/CEP_FinalProject_2018/blob/master/Screenshots/Snip1.PNG?raw=true)

This is the bottom right column.(Circled)
![Bottom Right](https://github.com/dafatskin/CEP_FinalProject_2018/blob/master/Screenshots/snip2.PNG?raw=true)

As such, the formatting for that tab would be:
classlist:A1-I399-NAME

3. The third part is in "scoring details". Scoring is a function in our code that relies on the psychomotor values in the excel sheet as a factor to allocate the students. Please edit the elements accordingly or change the Status to "on" or "off".

It consists of multiple elements in the format:
(CCAName):(Score below criteria value)-(Score above criteria value)-(Criteria)-(Status)

### Run the code
Click the file called "start.py". You should receive:
1. "final_report.docx" regarding the efficiency of the code and how the code performed.
2. "allocated.xlsx" which is the original file but with the allocations filled up.
3. Multiple excel sheets with the name of each class, the students in the class and the allocations assigned to them in a folder called "Class Allocations"
4. Multiple excel sheets with the name of each CCA and the students allocated to the CCA in a folder called "CCA Allocations"


## Allocation of work
**This section is for grading purposes only.**
Gerald did most of the main assigment code after brainstorming with Noah who provided the basic framework and logic behind the code. Noah did most of the admin with Gerald helping us to formulate and organize our README. Noah also contributed most of the presentation code, helped slightly by Gerald.

## Credits
I would like to thank Mrs Neo for guiding us through this project giving us advice and support.
Thanks to our classmates who also helped us with giving advice.




