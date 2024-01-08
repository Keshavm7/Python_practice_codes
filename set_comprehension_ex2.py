# reading the values from KBD by using set Comprehension
print("Enter list of values sepersted by space ")
st={val for val in input().split() }
print("The list of values is :{}".format(st))
