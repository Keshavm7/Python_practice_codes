# Program for Reading words from Keyboard and accepting only the words whose length is in between 3 to 5
print("Enter list of values seperated by space")
lst=[word for word in input().split() if len(word) in range(3,6)]
print("The list of words is:{}".format(lst))
