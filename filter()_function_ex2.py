# Program which will accept list of numerical values and filter positive number and negative numbers seperately using filter() function.

def pos(n):
    if (n>0):
        return n

def neg(n):
    if(n<0):
        return n

print("Enter list of values seperated by space ")
lst=[int(val) for val in input().split()]
posv=filter(pos,lst)
p=list(posv)
print("The list of positive values:{} ".format(p))
negv=filter(neg,lst)
n=list(negv)
print("The list of negative values :{}".format(n))