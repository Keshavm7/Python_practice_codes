#This Program will rename the Folder by using rename() of os module
import os
try:
    os.rename("G:\\GIT Files\\repo\\python.py","G:\\GIT Files\\repo\\newfile.py")
    print("Folder Renamed...verify!!!!")
except FileNotFoundError:
    print("File doesn't Exists!!")