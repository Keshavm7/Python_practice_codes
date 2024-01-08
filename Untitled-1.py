def  readwords():
	lst=[] # create an empty list
	print("Enter Number of Words and presss @ to stop:")
	while(True):
		word=input()
		if(word=="@"):
			break
		lst.append(word)
	return lst # this fucntion returns List object

def  findwordslength(lst):
	d={} # Create an empty dict for storing Name:length Pairs
	for word in lst:
		d[word]=len(word)
	return d # this fucntion returns dict object
	
def findhighestlengthword(dobj):
	print("="*40)
	print("\t\tWord\tLength")
	print("="*40)
	for word in dobj:
		print("\t\t{}\t{}".format(word,dobj.get(word)))
	print("="*40)
	#Code Finding Max Length Word(s)
	mlen=max(dobj.values())
	maxlenwords=[] # For Storing Max length words
	for word,length in dobj.items():
		if(mlen==length):
			maxlenwords.append(word)
	else:
		print("--------------------------------------------------------")
		print("Max Length Words")
		print("--------------------------------------------------------")
		for word in maxlenwords:
			print("\t\t{}".format(word))
		print("--------------------------------------------------------")
#main program
wordlist=readwords() # Function Call
dobj=findwordslength(wordlist) # Function Call taking list object as Parameter
findhighestlengthword(dobj)