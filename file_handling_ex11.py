#Program for Reading The Data from the file


try:
    with open("stud_data","r") as rp:
        read_data=rp.read()
        print("*"*50)
        print("Content of the file")
        print("*"*50)
        print(read_data)
except FileNotFoundError:
    print("File doesn't exist")