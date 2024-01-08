# program which will accept the list of values and return maximum value among the list values using reduce() function.
import functools
print("Enter list of values seperated by space")
lst=[int(val) for val in input().split()]
res=functools.reduce(lambda x,y:x if x>y else y,lst)
print("The max value in list is :{}".format(res))