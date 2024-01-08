# program which will accept list of numbers,Words,Alphanumeric words and filter them Seperately using filter() function.
print("Enter list of numbers,Words,Alphanumeric words seperated by space ")
lst=[val for val in input().split()]
num=list(filter(lambda n:n.isdigit(),lst))
words=list(filter(lambda w:w.isalpha(),lst))
alp=list(filter(lambda a:not a.isalpha() and not a.isdigit(),lst))
print("The list of numbers is:{}".format(num))
print("The list of alphabets is:{}".format(words))
print("The list of alnum is :{}".format(alp))