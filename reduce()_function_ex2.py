# program which will accept the list of values and return sum of those values using reduce() function.
import functools
def sum(x,y):
    return x+y

print("Enter list of values seperated by space")
lst=[int(val) for val in input().split()]
res=functools.reduce(sum,lst)
print("{}".format(res))