"""
File: Project2 Crase
Author: Cale Crase
Text file program
"""

fileName = input("Enter the file name: ")
f = open(fileName, "r")
c = f.read()
f.close()
ls = []
l = ""
for sign in c:
    if sign != '\n':
        l += sign
    else:
        ls.append(l)
        l = ""
ls.append(l)
print("The File " + str(fileName) + " has " + str(len(ls)) + " lines.")
lineNumber = int(input("How many lines do you want to see: "))
if lineNumber != 0:
    print(ls[int(lineNumber) - 1])
