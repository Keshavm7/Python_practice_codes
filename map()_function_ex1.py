# program which accepts the list of values from keyboard and convert into squares of that number using map() of function
print("Enter list of values sepersted by space")
lst=[int(val) for val in input().split() if int(val)>0]
sqlst=list(map(lambda v:v**2,lst))
print("The squares of given values list is:{}".format(sqlst))