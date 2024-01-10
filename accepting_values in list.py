lst=[]
n=int(input("Enter how many values you want to give as input: "))
for i in range(1,n):
    val=int(input("Enter {} value:".format(i)))
    lst.append(val)
    
print("The given values of list is:{}".format(lst))