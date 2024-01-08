#program for Reading and List of +ve Values and get sqrts
print("Enter list of values seperated by space")
dct={int(val):round(int(val)**0.5,2) for val in input().split() if float(val)>0}
print("The list of given values is: {}".format(dct))