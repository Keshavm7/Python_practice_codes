# python program for calculating simple interest and total amount to pay by using function approach_2
def simpleint():
    p=int(input("Enter principle amount: "))
    n=int(input("Enter time: "))
    r=int(input("Enter rate of interest: "))
    si=p*n*r/100
    total=si+p
    print("The interest amount to pay is {} and total amount is {}".format(si,total))
simpleint()