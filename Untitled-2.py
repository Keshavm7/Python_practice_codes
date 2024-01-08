# program which will accept list of numbers,Words,Alphanumeric words and filter them Seperately using filter() function.
print("Enter list of numbers,Words,Alphanumeric words seperated by space ")
lst=[val for val in input().split()]
num=list(filter(lambda n:int(n).isdigit(),lst))
words=list(filter(lambda w:w.isalpha(),lst))
alp=list(filter(lambda a:a.isalnum(),lst))