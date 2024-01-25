#program for Demonstrating writing the Data to the file

sno=int(input("Enter student roll number: "))
sname=input("Enter student name: ")
marks=int(input("Enter student marks: "))

with open("stud_data","a") as dp:
    dp.write(str(sno)+"\t")
    dp.write(sname+"\t")
    dp.write(str(marks)+"\n")
print("Student data added successfully!!!!")

