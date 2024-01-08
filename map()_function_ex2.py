# program which accepts the list of values from keyboard and convert into squares of that number using map() of function

def sqlst(v):
    return v**2

print("Enter list of values seperated by space")
lst=[int(val) for val in input().split() if int(val)>0]
sqlist=list(map(sqlst,lst))
print("The squares of given list is {}".format(sqlist))
