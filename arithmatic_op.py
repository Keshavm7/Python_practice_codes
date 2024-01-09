def addop():
    a=int(input("Enter value for a:"))
    b=int(input("Enter value of b: "))
    print("The sum of two numbers is {}".format(a+b))

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("The factorial of {} is {}".format(n,f))

def natsum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    print("The sum of first {} numbers is {}".format(n,s))

def table(t):
    for i in range(1,11):
        print("{}*{}={}".format(t,i,t*i))
    