# program for list which acccepts range of values and find the max() and min() without using min() or max() function in the list
# Method_2 using sort()
def readvalues():
    n=int(input("Enter how many numbers you want to give: "))
    if(n<=0):
        return[]
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("enter {} value: ".format(i)))
            lst.append(val)
        return lst
def maxn(lst):
    lst.sort(reverse=True)
    return lst[0]
def minn(lst):
    lst.sort()
    return lst[0]
num=readvalues()
print("given_list={}".format(num))
maxn(num)
print("The biggest number is {}".format(maxn(num)))
minn(num)
print("The smallest number is {}".format(minn(num)))
    