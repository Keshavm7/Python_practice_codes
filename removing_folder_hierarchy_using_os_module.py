# This Program remove a Folders Hierachy  at time
import os
try:
    os.removedirs("G:\\GIT Files\\repo\\keshav\\OS_operation\\Python\\folder_hierarchy")
    print("Folder hierarchy removed!!!!")
except FileNotFoundError:
    print("Folder not Exist!!!!")
except OSError:
    print("Folder is not empty!!")