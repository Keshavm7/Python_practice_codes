# Write a python program which will accept list of words and get palindrome words and also find highest length palindrome word.
def readwords():
    lst=[]
    print("Enter as many words you want and press # to stop")
    while(True):
        word=input()
        if(word=="#"):
            break
        lst.append(word)
    return lst

def palindromewrd(lst):
    lst2={}
    for words in lst:
        if(words==words[::-1]):
            lst2[words]=len(words)
            
    return lst2
def lngstwrd(lst2):
    print("*"*80)
    print("\t\tWORD\tLENGTH")
    print("*"*80)
    for pword in lst2:
        print("\t\t{}\t{}".format(pword,lst2.get(pword)))
    mxlen=max(lst2.values())
    d=[]
    for w,l in lst2.items():
        if(mxlen==l):
            d.append(w)
        
    else:
        print("*"*50)
        for j in d:
            print("The longest palindrome word is {}".format(j))
        print("*"*50)
        


            
            
    

s=readwords()
print("{}".format(s))
r=palindromewrd(s)
print("{}".format(palindromewrd(s)))
lngstwrd(r)
