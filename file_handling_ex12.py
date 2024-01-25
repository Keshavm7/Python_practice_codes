#Program for Reading The Data from the file


try:
    filename=input("Enter file name: ")
    with open(filename,"r") as fp:
        data=fp.read()
        print("*"*50)
        print("Content of the file")
        print("*"*50)
        print(data)
except FileNotFoundError:
    print("File Doesn't exist!!!!")
        