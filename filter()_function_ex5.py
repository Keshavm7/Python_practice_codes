# program which will accept list of text or words and obtain no.of alphabets,no.of special symbols,no.of digits using filter() function.
print("Enter line of text or word or sentence")
lst=[wrd for wrd in input()]
res1=list(filter(lambda n:n.isalpha(),lst))
res2=list(filter(lambda n:n.isdigit(),lst))
res3=list(filter(lambda n:not n.isalpha() and not n.isdigit(),lst))
print("The number of alphabets in given line of text is:{}".format(len(res1)))
print("The number of special symbols in given line of text is:{}".format(len(res2)))
print("The number of digits in given line of text is:{}".format(len(res3)))