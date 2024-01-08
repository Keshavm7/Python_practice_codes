# Program for Reading Only +Ve values from Keyboard
print("Enter list of values sepersted by space")
lst=[float(val) for val in input().split() if float(val)>0 ]
print("The list of values is:{}".format(lst))

