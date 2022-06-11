import tmp
lines = ["println hello", "println world"]
fileToExec = input("enter filename: ")
in_file = open(fileToExec,"r")
lines = in_file.readlines()
in_file.close()
for item in lines:
    tmp.interpetCode(item)
