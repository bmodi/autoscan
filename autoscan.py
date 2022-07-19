#!/usr/local/bin/python3

import sys
import os
import pdfplumber
import re

cars = ["2001 Oldsmobile Alero", "2007 Honda Odyssey"]

def getInput():
    if len(sys.argv) == 1:
        print("Please specify name of file to parse.")
    elif len(sys.argv) == 2:
        userInput = sys.argv[1]
        return userInput
    else:
        print("Too many arguments. Please specify name of file to parse.")

def combineAllPages(file):
    allText = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            allText += page.extract_text()
    return allText.upper()

def getMakeModel(text):
    for car in cars:
        if car.upper() in text:
            return car

def getDate(text):
    dateIndex = text.find("DATE  :") + 7
    date = text[dateIndex:dateIndex+10]
    return f"{date[6:]}-{date[0:2]}-{date[3:5]}"

def getTraveledKMs(text):
    traveledKMsIndexStart = text.find("ODO   :") + 8
    traveledKMsIndexEnd = text.find(" ", traveledKMsIndexStart)
    return text[traveledKMsIndexStart:traveledKMsIndexEnd].replace(",", "")

def searchForPhrases(text):
    phrasesFile = open("phrases.txt", "r")
    phrasesFound = []
    for phrase in phrasesFile:
        expression = re.search(phrase.strip().upper(), text)
        if expression:
            phrasesFound.append(expression.group())
    return phrasesFound

def getDirectoryFiles(directory):
    listOfFiles = os.listdir(directory)
    listOfPDFs = []
    directoryContainsPDF = False
    for file in listOfFiles:
        if file.endswith('pdf'):
            listOfPDFs.append(file)
            directoryContainsPDF = True
    if directoryContainsPDF == False:
        print("Directory contains no PDFs")
    return listOfPDFs

input = getInput()

if input:
    if os.path.isdir(input):
        directoryFiles = getDirectoryFiles(input)
        print("Car, Date, Odometer, Work, Invoice")
        for file in directoryFiles:
            text = combineAllPages(input + "/" + file)
            makeModel = getMakeModel(text)
            date = getDate(text)
            traveledKMs = getTraveledKMs(text)
            phrasesFound = searchForPhrases(text)
            for phrase in phrasesFound:
                print(f"{makeModel}, {date}, {traveledKMs}, {phrase}, {file}")
    elif os.path.isfile(input):
        if input.endswith('pdf'):
            print("Car, Date, Odometer, Work, Invoice")
            text = combineAllPages(input)
            makeModel = getMakeModel(text)
            date = getDate(text)
            traveledKMs = getTraveledKMs(text)
            phrasesFound = searchForPhrases(text)
            for phrase in phrasesFound:
                print(f"{makeModel}, {date}, {traveledKMs}, {phrase}, {input}")
        else:
            print('Please enter the name of a PDF file.')
    else:
        print("Could not find file or directory  " + input)