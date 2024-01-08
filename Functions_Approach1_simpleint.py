# python program for calculating simple interest and total amount to pay by using function
def simpleint(p,n,r):
    si=p*n*r/100
    total=p+si
    return si,total
p=int(input("Enter principle amount: "))
n=int(input("Enter time: "))
r=int(input("Enter rate of interst: "))
res=simpleint(p,n,r)
print("The total interest amount is {}.Total amount to pay is {}".format(res[0],res[1]))