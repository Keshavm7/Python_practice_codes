#program for Demonstrating writing the Data to the file

with open("stud_data","a") as fp:
    print("Enter data and press @ to stop")
    while(True):
        data=input()
        if(data!= "@"):
            fp.write(data+"\n")
        else:
            print("Data added successfully!!!....verify")
            break