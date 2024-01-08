#program for generating 1 to n where n is positive using while loop
n= int(input("Enter how many numbers want to generate: "))
if(n<=0):
    print("invalid input!!!!!")
else:
    i=1
    while(i<=n):
        print("\t{}".format(i))
        i=i+1