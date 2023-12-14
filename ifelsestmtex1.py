# using if....else statment check whether number is positive,negative or zero
n=int(input("Enter any value: "))
if(n>0):
    print("{} is positive number".format(n))
else:
    if(n<0):
        print("{} is Negative number".format(n))
    else:
        print("{} is zero".format(n))
        