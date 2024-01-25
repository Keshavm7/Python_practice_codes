#Program for Demonstrating How to open the file

try:
    fp=open("file_handling","r")
except FileNotFoundError:
    print("File Doesn't Exist")
    
else:
    print("File is opened successfully!!!")
    print("{}".format(type(fp)))
    
