# Program which will accept list of numerical values and filter positive number and negative numbers seperately using filter() function.
print("Enter list of values seperated by space")
lst=[int(val) for val in input().split()]
posv=filter(lambda n:n>0,lst)
posv2=list(posv)
print("The list of positive values is:{}".format(posv2))
negv=filter(lambda n:n<0,lst)
negv2=list(negv)
print("The list of negative values:{}".format(negv2))