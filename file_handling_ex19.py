#Program for Creating CSV File

import csv
hname=["prcode","prname","price"]
records=[{"prcode":1001,"prname":"Biscuit_G","price":5},
         {"prcode":1002,"prname":"Toffy","price":10},
         {"prcode":1003,"prname":"Good Day","price":25},
         {"prcode":1004,"prname":"Milk_g","price":15},
         {"prcode":1005,"prname":"Paste","price":50}]

with open("G:\\GIT Files\\repo\\keshav\\CSV\\product.csv","a") as fp:
    data=csv.DictWriter(fp,fieldnames=hname)
    data.writeheader()
    data.writerows(records)
    print("Data added successfully!!!!....verify")