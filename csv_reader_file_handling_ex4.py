#Program for Reading the Data from CSV File with csv Module

import csv
try:
    with open("G:\\GIT Files\\repo\\keshav\\CSV\\product.csv","r") as fp:
        data=csv.DictReader(fp)
       
        for values in data:
            print("*"*50)
            for i,v in values.items():
                
                print("{}---->{}".format(i,v))
                print()
        print("*"*50)
except FileNotFoundError:
    print("File ddoesn't exist!!!!")
                
            
    