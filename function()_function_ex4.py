# program which will accept list of words which contains uppercase and lowercase words and filter only uppercase words using filter() function.
print("Enter list of words seperated by space ")
lst=[ words for words in input().split(",")]
w=filter(lambda wrd:wrd.isupper(),lst)
wrds=tuple(w)
print("The list of uppercase words are:{}".format(wrds))