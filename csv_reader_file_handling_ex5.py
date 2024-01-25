#Program for Reading the Data from CSV File with csv Module

import csv
with open("G:\\GIT Files\\repo\\keshav\\CSV\\employee_data.csv","r") as fp:
    data=csv.reader(fp)
    for val in data:
            print("-"*50)
            print("{}".format(val),end=" ")
            print()
    print("-"*50)
        