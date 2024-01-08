# python program which accepts list of words and find their lengths and find highest length word.
def readwords():
    n=int(input("Enter how many words you want to give: "))
    if(n<=0):
        return []
    else:
        lst=[]
        for i in range(1,n+1):
            wrd=input("Enter {} word: ".format(i))
            lst.append(wrd)
        return lst
def lengthwrd(lst):
    d={}
    for l in lst:
        d[l]=len(l)
    return d
def lgstwrd(dobj):
    print("*"*50)
    print("\tWORD\t\t\t\tLENGTH\t")
    print("*"*50)
    for wrd in dobj:
        print("\t{}\t\t\t\t{}\t".format(wrd,dobj.get(wrd)))
    lrstwrd=max(dobj.values())
    o=[]
    for w,lr in dobj.items():
        if(lrstwrd==lr):
            o.append(w)
    for words in o:
        print("\t{}".format(words))
            
       
w=readwords()
c=lengthwrd(w)
lgstwrd(c)
print("Maximum lenght word is {}".format(lgstwrd(c)))

        
    