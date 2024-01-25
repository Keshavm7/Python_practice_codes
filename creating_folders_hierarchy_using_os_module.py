#Program for cerating Folders Hierarchy(Root Folder-->Sub Folder-->Sub Sub Folder-->etc
import os
try:
    os.makedirs("G:\\GIT Files\\repo\\keshav\\OS_operation\\Python\\folder_hierarchy\\final")
    print("Folder hierarchy created successfully!!!")
except FileExistsError:
    print("Folder already exists!!!!")
except OSError:
    print("Check folder path!!")