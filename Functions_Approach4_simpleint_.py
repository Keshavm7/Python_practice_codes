# python program for calculating simple interest and total amount to pay by using function approach_4
def simpleint():
    p=int(input("Enter principle amount: "))
    n=int(input("Enter time: "))
    r=int(input("Enter rate of interest: "))
    si=p*n*r/100
    total=si+p
    return si,total
res=simpleint()
print("*"*100)
print("The interest amount to pay is {} \nThe total amount to pay is {}".format(res[0],res[1]))
print("*"*100)