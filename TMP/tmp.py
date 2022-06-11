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
    args = args.replace('\\t', '\t')
    return args

#Variables and other preprocesses here
def preprocess(args):
    global variables
    for arg in range(len(args)):
        if args[int(arg)][0] == "$":
            try:
                args[int(arg)] = variables[args[int(arg)][1:]]
            except:
                print("Error: variable nonexistent")
    return args

#Interpret code from text input
def interpetCode(plainInput):
    global variables
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


#Main loop for programming here

#Define variables in dictionary
variables = {"test": "1"}

if __name__ == "__main__":
    while True:
        plainInput = input("tmp>")
        interpetCode(plainInput)
    ##    stringLiteral = handleControl(plainInput)
    ##    args = plainInput.split()
    ##    finalArgs = preprocess(args)
    ##    fullStringLiteral = " ".join(args)
    ##    if (finalArgs[0] == "println"):
    ##        print(fullStringLiteral[8:])
    ##    if (finalArgs[0] == "print"):
    ##        print(fullStringLiteral[6:], end='')
    ##    if (finalArgs[0] == "setvar"):
    ##        variables[str(finalArgs[1])] = finalArgs[2]
    




