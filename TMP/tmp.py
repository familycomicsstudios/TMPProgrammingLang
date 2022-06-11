"""
TMP Programming Language
v0.4.0
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
        if args[int(arg)][0] == "`":
            args[int(arg)] = args[int(arg)][1:]
            
    return args

#Interpret code from text input
def interpetCode(plainInput):
    global variables
    global skipNextLine
    if skipNextLine < 1:
        stringLiteral = handleControl(plainInput)
        args = plainInput.split()
        finalArgs = preprocess(args)
        fullStringLiteral = " ".join(args)
        if len(finalArgs) > 0:
            if (finalArgs[0] == "println"):
                print(fullStringLiteral[8:])
            if (finalArgs[0] == "print"):
                print(fullStringLiteral[6:], end='')
            if (finalArgs[0] == "setvar"):
                variables[str(finalArgs[1])] = fullStringLiteral[8+len(finalArgs[1]):]
            if (finalArgs[0] == "input"):
                variables[str(finalArgs[1])] = input()
            if (finalArgs[0] == "ifset"):
                if finalArgs[1] == "True":
                    variables[str(finalArgs[4])] = variables[str(finalArgs[2])]
                else:
                    variables[str(finalArgs[4])] = variables[str(finalArgs[3])]
            if (finalArgs[0] == "eval"):
                if finalArgs[2] == "=":
                    if finalArgs[1] == finalArgs[3]:
                        variables[str(finalArgs[4])] = "True"
                    else:
                        variables[str(finalArgs[4])] = "False"
            if (finalArgs[0] == "if"):
                if finalArgs[1] == "True":
                    skipNextLine = 0
                else:
                    skipNextLine = int(finalArgs[2])
        else:
            skipNextLine -= 1
                
            


#Main loop for programming here

#Define variables in dictionary
variables = {"test": "1"}
skipNextLine = 0

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
    




