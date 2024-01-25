#program for Demonstrating writing the Data to the file

sno=25
sname="Mukesh"
marks=95
with open("stud_data","a") as dp:
    dp.write(str(sno)+"\t")
    dp.write(sname+"\t")
    dp.write(str(marks)+"\n")
print("student data added successfully!!!!")
