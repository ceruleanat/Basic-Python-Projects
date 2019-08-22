import os

fName = 'Text1.txt'

fPath = 'C:\\python_projects\\'

abPath = os.path.join(fPath, fName)
print(abPath)

listdir = os.listdir(fPath)
print(listdir)

getmtime = os.path.getmtime(fPath)
print(getmtime)

