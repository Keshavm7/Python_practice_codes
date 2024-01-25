#Program for Creating a Folder
import os
try:
    os.mkdir("G:\\GIT Files\\repo\\keshav\\OS_operation")
    print("File created sucessfully!!!")
except FileExistsError:
    print("File already exist!!!")
except OSError:
    print("once again check file path!!!")