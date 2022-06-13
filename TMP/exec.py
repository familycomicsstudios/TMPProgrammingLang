import tmp
lines = ["println hello", "println world"]
fileToExec = input("enter filename: ")
in_file = open(fileToExec,"r")
lines = in_file.readlines()
in_file.close()
line_no = 0
while line_no <= len(lines):
    if line_no < len(lines):
        heck = tmp.interpetCode(lines[line_no])
    if heck == "letestoftestiness":
        line_no = tmp.line_no
    else:
        line_no += 1
