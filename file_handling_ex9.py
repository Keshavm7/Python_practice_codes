#program for Demonstrating writing the Data to the file

lst=[30,"Shin",76]
 
with open("stud_data","a") as dp:
    dp.writelines(str(lst)+"\n")
print("Student data added successfully!!!!")


