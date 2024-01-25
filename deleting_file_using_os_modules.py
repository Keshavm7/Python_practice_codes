#This Program removes the file name by using remove(FileName) of os module
import os
try:
    os.remove("G:\\GIT Files\\repo\\keshav\\rough code\\untitled-1.py")
    print("File is deleted!!!")
except FileNotFoundError:
    print("File doesn't exists!!!")
    