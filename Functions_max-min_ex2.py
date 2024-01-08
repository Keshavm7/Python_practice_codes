# program for list which acccepts range of values and find the max() and min() without using min() or max() function in the list
# Method_1 using for loop 
def readvalues():
    n=int(input("Enter as many no. of values you want: "))
    if(n<=0):
        return[]
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("Enter {} value: ".format(i)))
            lst.append(val)
        return lst
def maxnum(lst):
    max=lst[0]
    for p in lst:
        if p>max:
            max=p
    return max
def minnum(lst):
    min=lst[0]
    for m in lst:
        if m<min:
            min=m
    return min 


nums=readvalues()
maxnum(nums)
print("the biggest number is {}".format(maxnum(nums)))
minnum(nums)
print("the smallest number is {}".format(minnum(nums)))