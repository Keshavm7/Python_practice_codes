#This Program remove a Folder at time
import os

try:
    os.rmdir("G:\\GIT Files\\repo\\keshav\\OS_operation\\Python\\folder_hierarchy\\final")
    print("Folder removed.....verify!!!")
except FileNotFoundError:
    print("File Not found!!!!")
except OSError:
    print("Folder is not empty!!!")
    