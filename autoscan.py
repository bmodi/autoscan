#!/usr/local/bin/python3

import sys
import os
import pdfplumber

cars = ["2001 Oldsmobile Alero", "2007 Honda Odyssey"]

def getInput():
    if len(sys.argv) == 1:
        print("Please specify name of file to parse.")
    elif len(sys.argv) == 2:
        userInput = sys.argv[1]
        return userInput
    else:
        print("Too many arguments. Please specify name of file to parse.")

def scanPDFSInDirectory(directoryName):
    listOfFiles = os.listdir(directoryName)
    listOfPDFs = []
    directoryContainsPDF = False
    for file in listOfFiles:
        shortName = file
        file = input + "/" + file
        if file.endswith('pdf'):
            listOfPDFs.append(file)
            directoryContainsPDF = True
            scanPDF(file, combineAllPages(file), shortName)
    if directoryContainsPDF == False:
        print("Directory contains no PDFs")
    return listOfPDFs

def getMakeModel(file):
    with pdfplumber.open(file) as pdf:
        firstPage = pdf.pages[0]
        for car in cars:
            if car in firstPage.extract_text():
                return car
    file.close()

def getDate(file):
    with pdfplumber.open(file) as pdf:
        firstPage = pdf.pages[0]
        dateIndex = firstPage.extract_text().find("Date  :") + 7
        date = firstPage.extract_text()[dateIndex:dateIndex+10]
        return f"{date[6:]}-{date[0:2]}-{date[3:5]}"
    file.close()

def getTraveledKMs(file):
    with pdfplumber.open(file) as pdf:
        firstPage = pdf.pages[0]
        traveledKMsIndexStart = firstPage.extract_text().find("ODO   :") + 8
        traveledKMsIndexEnd = firstPage.extract_text().find(" ", traveledKMsIndexStart)
        return firstPage.extract_text()[traveledKMsIndexStart:traveledKMsIndexEnd].replace(",", "")
    file.close()

def combineAllPages(file):
    allText = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            allText += page.extract_text()
    return allText.upper()

def getModelDateKMs(file):
    makeModel = getMakeModel(file)
    date = getDate(file)
    traveledKMs = getTraveledKMs(file)
    return f"{makeModel}, {date}, {traveledKMs}"

def searchForPhrases(pages, file):
    phrasesFile = open("phrases.txt", "r")
    for phrase in phrasesFile:
        if phrase.upper().strip() in pages:
            print(f"{modelDateKMs}, {phrase.strip()}, {file}")
    phrasesFile.close()

def scanPDF(fileName, text, shortName):
    global modelDateKMs
    modelDateKMs = getModelDateKMs(fileName)
    # allPages = combineAllPages(text)
    searchForPhrases(text, shortName)

input = getInput()

if input:
    if os.path.isdir(input):
        scanPDFSInDirectory(input)
    elif os.path.isfile(input):
        if input.endswith('pdf'):
            # modelDateKMs = getModelDateKMs(input)
            allPages = combineAllPages(input)
            # searchForPhrases(allPages, input)
            scanPDF(input, allPages, input)
        else:
            print('Please enter the name of a PDF file.')
    else:
        print("Could not find file or directory  " + input)