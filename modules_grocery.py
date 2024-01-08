# displaying groceries list using modules concept with varying price in 10 sec
import grocery,time,importlib
def dispgrocery(d):
    print("*"*50)
    print("\t\tName\t\Total Price")
    print("*"*50)
    for g,t in d.items():
        print("\t\t{}\t\t{}".format(g,t))
    print("*"*50)

d=grocery.grocerylist()
dispgrocery(d)
time.sleep(10)
importlib.reload(grocery)
d=grocery.grocerylist()
dispgrocery(d)