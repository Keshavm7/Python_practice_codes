#program for Reading and List of  Words and find its length
print("Enter List of Words Separated space:")
dobj={ word:len(word)   for word in input().split() }  
for word,wordlen in dobj.items():
    print("\t{}--->{}".format(word,wordlen))
