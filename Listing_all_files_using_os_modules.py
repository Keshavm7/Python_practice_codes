#This Program will list the files in folder by using listfiles() of os module
import os
try:
    filedata=os.listdir("G:\\GIT Files\\repo\\keshav\\Python_practice_codes")
    for file in filedata:
        print("{}".format(filedata))
except FileNotFoundError:
    print("Folder doesn't exists!!!!")