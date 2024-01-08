# program which will accept the list of values and return maximum value among the list values using reduce() function.
import functools
def maxval(x,y):
    res= x if (x>y) else y
    return res
    

print("Enter the list of values seperated by space ")
lst=[int(val) for val in input().split()]
maxv=functools.reduce(maxval,lst)
print("The maximum value is {}".format(maxv))
