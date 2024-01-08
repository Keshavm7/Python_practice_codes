# program which will accept list of words and convert all words to uppercase using map() function.
print("Enter list of words seperated by space")
wrd=[ word for word in input().split()]
upwrd=list(map(lambda w:w.upper(),wrd))
print("The uppercase list of words:{}".format(upwrd))
print("*"*50)
for i,j in zip(wrd,upwrd):
    print("\t\t{}\t\t{}".format(i,j))
print("*"*50)