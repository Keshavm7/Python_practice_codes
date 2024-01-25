#Program for Demonstrating How to open the file

try:
    with open("file_handling_2","a") as fp:
        print("The file has been created successfully!!!!!")
        print("{}".format(type(fp)))
        print("is file closed:",fp.closed)
    print("pvm comes out of indentation")
    print("is file closed:",fp.closed)
except FileExistsError:
    print("File already exists")