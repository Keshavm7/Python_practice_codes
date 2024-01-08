# program for generating numbers from n to 1 where n is positive using while...loop
n=int(input("Enter how many numbers want to generate: ")) 
if(n<=0):
    print("invalid input!!!!")
else:
    i=n
    while(i>0):
        print("\t{}".format(i))
        i=i-1
