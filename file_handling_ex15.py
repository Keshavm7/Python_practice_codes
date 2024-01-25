#Program for reading employee details and save them as Record in Emploiyee File

import pickle


def saveempdata():
    with open("emp_data","ab") as emp:
        empdata=[]
        print("*"*50)
        print("Enter all information about employees")
        empno=int(input("Enter employee number: "))
        empname=input("Enter employee name: ")
        empsal=float(input("Enter employee salary: "))
        empdesig=input("Enter employee designation: ")
        print("*"*50)
        empdata.append(empno)
        empdata.append(empname)
        empdata.append(empsal)
        empdata.append(empdesig)
        print("{}".format(empdata))
        pickle.dump(empdata,emp)
        print("Data added to the file....verify!!!!")
    
# main program
saveempdata()

    
    
    