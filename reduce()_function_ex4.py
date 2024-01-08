# program which accepts list of words and convert it into line of text using reduce() function.
import functools
print("Enter list of words seperated by space")
lst=[word for word in input().split()]
line=functools.reduce(lambda w,y:w+" "+y,lst)
print("The line of text is :{}".format(line))