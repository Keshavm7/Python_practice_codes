#Program for Reading Only +Ve values from Keyboard
print("Enter list of values seperated by space ")
lst=[float(val) for val in input().split() if float(val)>0]
print("The list of positive numbers:{} ".format(lst))
print("Enter list of values seperated by space ")
lst2=[float(val) for val in input().split() if float(val)<0]
print("The list of Negative numbers:{} ".format(lst2))