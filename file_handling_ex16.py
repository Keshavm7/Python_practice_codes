#Program for reading employee details and save them as Record in Emploiyee File

import pickle,sys

def saveemployeedata():
    while(True):
        with open("emp_data","ab") as ep:
            print("*"*50)
            print("Enter all information of Employee")
            print("*"*50)
            eno=int(input("Enter employee number: "))
            ename=input("Enter employee name: ")
            esal=float(input("Enter employee salary: "))
            edsg=input("Enter employee designation: ")
            print("*"*50)
            emp=[]
            emp.append(eno)
            emp.append(ename)
            emp.append(esal)
            emp.append(edsg)
            print("{}".format(emp))
            pickle.dump(emp,ep)
            ch=input("Do you want to enter another record (yes/No): ")
            if(ch.lower()=="no"):
                sys.exit()
        
#main Program

saveemployeedata()