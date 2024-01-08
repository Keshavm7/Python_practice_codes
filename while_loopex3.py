# program for generating odd numbers from 1 to n where n is positive using while.....loop
n=int(input("Enter how many odd numbers want to generate: "))
if(n<=0):
    print("Invalid Input!!!!!!!!")
else:
    i=1
    while(i<=n):
        if(n%2==0):
            n-=1
        else:
            print("\t{}".format(i))
            i+=2