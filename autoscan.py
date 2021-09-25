#!/usr/bin/python

import sys
import os

print ('Searching for documents...')


if len(sys.argv) > 1:
    fileName = sys.argv[1]
    if os.path.isfile('./'+fileName):
        print("Found file")
    else:
        print("Could not find file")
else:
    print("Please specify name of file to parse")