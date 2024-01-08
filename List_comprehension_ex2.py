# Program for Returning  List of Values an Obtain their Squares
print("enter list of values sepersted by space") 
res=[int(val)**2 for val in input().split() if int(val)>0 ]
print("The list of values and its squares is = {}".format(res))