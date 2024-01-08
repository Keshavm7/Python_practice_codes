# python  program  which will accept list of numerical values and find its sum and average
def readvalues():
    n=int(input("Enter how many values you want to give as input:"))
    if(n<=0):
        return []
    else:
        lst=[]
        for i in range(1,n+1):
            val=int(input("Enter {} value: ".format(i)))
            lst.append(val)
        return lst
def sumop(lst):
    s=0
    for p in lst:
        s=s+p
    return s
def avgop(lst):
    a=sumop(lst)/len(lst)
    return a
d=readvalues()
sumop(d)
print("The sum of given list values is {}".format(sumop(d)))
avgop(d)
print("The avg of given list of values is {}".format(avgop(d)))
    