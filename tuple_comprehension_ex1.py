#reading the values from KBD by using List Comprehension
print("Enter List of Values Separated  Space:")
x= ( int(num)    for num in input().split() )
# Here x is an object of <class,'generator>
tpl=tuple(x) # we are type casting an of generator to tuple
print("Tuple of Values:{} and whose type is {}".format(tpl,type(tpl)))