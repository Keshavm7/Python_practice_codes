#Program for  adding new record to  the CSV File

import  csv
row=[600,"Sunil",55000,"Manager"]
with open("G:\\GIT Files\\repo\\keshav\\CSV\\employee_data.csv","a") as fp:
    record=csv.writer(fp)
    record.writerow(row)
    print("new row added successfully!!!")
    
    