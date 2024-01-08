# program for checking whether given number is magic number or not 
def magicnum():
    n=int(input("Enter any number you want: "))
    sq=n**2
    res="magic number" if(str(n)==str(sq)[-len(str(n)):]) else "Not Magic number"
    print("{} is {}".format(n,res))
magicnum()
        
