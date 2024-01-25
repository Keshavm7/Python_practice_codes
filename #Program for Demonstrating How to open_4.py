#Program for Demonstrating How to open the file


with open("file_handling_2","a+") as fp:
    print("The file has been created successfully!!!!")
    print("{}".format(type(fp)))
    print("Information about file")
    print("File Name: ",fp.name)
    print("File Mode: ",fp.mode)
    print("Is file readable: ",fp.readable())
    print("Is file writeable: ",fp.writable())
    
    