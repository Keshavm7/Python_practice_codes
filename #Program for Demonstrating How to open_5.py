#Program for Demonstrating How to open the file

try:
    with open("file_handling_5","x") as fp:
        print("The file has created excelusively in write mode")
        print("{}".format(type(fp)))
        print("Information about file")
        print("File Name: ",fp.name)
        print("File Mode: ",fp.mode)
        print("Is file Readable: ",fp.readable())
        print("Is file writable: ",fp.writable())
except FileExistsError:
    print("File already exists")
        
    