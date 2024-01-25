import pickle
def  searchrecord():
    with open("emp_data","rb") as fp:
        print("--------------------------------------------------")
        records=[]
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break

        eno=int(input("Enter Emp Number for getting Other details:"))
        res=False
        for record in records:
           if(eno==record[0]):
               res=True
               break
        if(res):
            print("*" * 50)
            print("Employee Name:{}".format(record[1]))
            print("Employee Salary:{}".format(record[2]))
            print("Employee Designation:{}".format(record[3]))
            print("*" * 50)
        else:
            print("Employee Number does not exist")

#main program
searchrecord()