#program for generating odd numbers from n to 1 where n is positive using while..loop
n=int(input("Enter how many number you  want to generate: "))
if(n<=0):
    print("Invalid Input!!!!!!")
else:
    if(n%2==0):
        n=n-1
    i=n
    while(i>0):
        print("\t{}".format(i))
        i=i-2
            
        