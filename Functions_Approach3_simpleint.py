# python program for calculating simple interest and total amount to pay by using function approach_3
def simpleint(p,n,r):
    si=p*n*r
    total=p+si
    print("The interest amount to pay is {} and total amount to pay is {}".format(si,total))
p=int(input("Enter principle amount: "))
n=int(input("Enter time: "))
r=int(input("Enter rate of interest: "))
simpleint(p,n,r)
    