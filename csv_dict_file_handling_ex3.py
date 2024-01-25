#Program for Creating CSV File

import csv
hname=["Prcode","prname","price"]
record=[{"Prcode":101,"prname":"Kaccha Mango","price":100},
        {"Prcode":102,"prname":"Biscuits","price":500},
        {"Prcode":103,"prname":"Choclate","price":250},
        {"Prcode":104,"prname":"Happy","price":450},
        {"Prcode":105,"prname":"Maggi","price":65}]

with open("G:\\GIT Files\\repo\\keshav\\CSV\\products_data.csv","a") as dp:
    records=csv.DictWriter(dp,fieldnames=hname)
    records.writeheader()
    records.writerows(records)
    print("Data Added successfully!!!!")