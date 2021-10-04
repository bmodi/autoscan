#!/usr/local/bin/python3

import sys
import os
import pdfplumber

def getInput():
    userInput = sys.argv[1]
    print("User input is " + userInput)
    if len(sys.argv) == 1:
        print("Please specify name of file to parse.")
    elif len(sys.argv) > 2:
        print("Too many arguments. Please specify name of file to parse.")
    return userInput

def printFilesInDirectory(directoryName):
    listOfFiles = os.listdir(directoryName)
    directoryContainsPDF = False
    for file in listOfFiles:
        if file.endswith('pdf'):
            print(file)
            directoryContainsPDF = True
    if directoryContainsPDF == False:
        print("Directory contains no PDFs")

input = getInput()

if os.path.isdir(input):
    printFilesInDirectory(input)
elif os.path.isfile(input):
    print("Parsing " + input)
    with pdfplumber.open(input) as pdf:
        first_page = pdf.pages[0]
        print(first_page.extract_text())
else:
    print("Could not find file or directory  " + input)