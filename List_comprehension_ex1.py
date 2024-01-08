# #reading the values from Keyboard by using List Comprehension
print("Enter list of values seperated by space")
lst=[ float(val) for val in input().split()]
print("The list of values :{} ".format(lst))