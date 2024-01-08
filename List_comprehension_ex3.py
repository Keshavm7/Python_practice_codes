#Program  for returning List of Values an Obtain their Squares
print("Enter list of values seperated by space ")
lst=[float(val) for val in input().split()]
print("The list of values are: {}".format(lst))
res=[v**2 for v in lst] 
print("The list of squares of given number is: {}".format(res))