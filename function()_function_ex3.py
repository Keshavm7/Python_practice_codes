# program which will accept list of numerical values and obtain only prime numbers using filter() function.
def prime(n):
    if(n<=1):
        print("Invalid input!!!")
    res=True
    for i in range(2,n):
        if(n%i==0):
            res= False
            break
    return res
            
print("Enter list of values seperated by space")
lst=[int(val) for val in input().split()]
pv=filter(lambda n:prime(n),lst)        
values=list(pv)
print("The list of  prime values:{}".format(values))