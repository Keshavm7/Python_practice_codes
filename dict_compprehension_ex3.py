# Program for Reading words from Keyboard and accepting only the words whose length is in between 3 to 5
print("Enter List of Words Separated space:")
dobj={ word:len(word)    for word in input().split()   if len(word) in range(3,6) }
for w,wl in dobj.items():
    print("\t{}--->{}".format(w,wl))