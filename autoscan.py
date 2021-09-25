#!/usr/local/bin/python3

import sys
import os

print ('Searching for documents...')

if len(sys.argv) == 1:
    print("Please specify name of file to parse.")
elif len(sys.argv) > 2:
    print("Too many arguments. Please specify name of file to parse.")
else:
    fileName = sys.argv[1]
    if os.path.isfile('./'+fileName):
        print("Parsing " + fileName)
    else:
        print("Could not find file " + fileName)