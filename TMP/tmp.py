"""
TMP Programming Language
v0.1.0
Build 06102022
"""

#import re
import re

#Newline handling
def handleControl(args):
    args = args.replace('\\n', '\n')
    return args

#Variables and other preprocesses here
def preprocess(args):
    global variables
    for arg in range(len(args)):
        if args[int(arg)][0] == "$":
            try:
                args[int(arg)] = variables[args[int(arg)][1:]]
            except:
                raise Exception('Variable nonexistent')
    return args

#Main loop for programming

#Define variables in dictionary
variables = {"test": "1"}

while True:
    plainInput = input("tmp>")
    stringLiteral = handleControl(plainInput)
    args = plainInput.split()
    finalArgs = preprocess(args)
    fullStringLiteral = " ".join(args)
    if (finalArgs[0] == "println"):
        print(fullStringLiteral[8:])
    if (finalArgs[0] == "print"):
        print(fullStringLiteral[6:], end='')
    if (finalArgs[0] == "setvar"):
        variables[str(finalArgs[1])] = finalArgs[2]
    




