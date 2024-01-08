# program for list which acccepts range of values and find the max() and min(),using min() and  max()  math function in the list.
# Method_3

def readvalues():
    n=int(input("Enter how many values you want to give as input: "))
    if(n<=0):
        return[] 
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("Enter {} value: ".format(i)))
            lst.append(val)
        return lst
def maxn(lst):
    m=max(lst)
    return m
def minn(lst):
    n=min(lst)
    return n
num=readvalues()
maxn(num)
print("The biggest number is {}".format(maxn(num)))
minn(num)
print("The smallest number is {}".format(minn(num)))
