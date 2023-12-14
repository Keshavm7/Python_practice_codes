# write a python which will accept any number and check whether it is even or odd using if..else statment
n=int(input("Enter any value:"))
if(n%2==0 and n!=0):
    print("{} is Even number".format(n))
else:
    if(n%2!=0):
        print("{} is Odd number".format(n))
    else:
        if(n==0):
            print("{} is Zero".format(n))

        