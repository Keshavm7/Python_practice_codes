#Program for Creating CSV File

import  csv
hname=["eno","ename","esalary","edesignation"]
data=[[100,"Mukesh",45000,"Analyst"],
      [200,"Anil",65000,"AWS"],
      [300,"Dinesh",44000,"Software Engineer"],
      [400,"Mukund",24000,"Support Engineer"],
      [500,"Jack",35000,"Tech support"]]

with open("G:\\GIT Files\\repo\\keshav\\CSV\\employee_data.csv","a") as fp:
    record=csv.writer(fp)
    record.writerow(hname)
    record.writerows(data)
    print("Data added to csv file successfully!!!!!")