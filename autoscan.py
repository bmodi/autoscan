#!/usr/local/bin/python3

import sys
import os

userInput = sys.argv[1]

print ('Searching for documents...')

if len(sys.argv) == 1:
    print("Please specify name of file to parse.")
elif len(sys.argv) > 2:
    print("Too many arguments. Please specify name of file to parse.")
elif os.path.isdir(userInput):
    print(os.listdir(userInput))
else:
    if os.path.isfile(userInput):
        print("Parsing " + userInput)
    else:
        print("Could not find file or directory  " + userInput)