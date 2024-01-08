# Write a python program which will accept list of words and find there lengths  and find highest length word.
def readwords():
    n=int(input("Enter how many words you want to insert in object: "))
    if(n<=0):
        print("Invalid Input!!!!")
    else:
        lst=[]
        for i in range(1,n+1):
            wrd=input("Enter {} word: ".format(i))
            lst.append(wrd)
        return lst
def lenwrd(lst):
    d={}
    for w in lst:
        d[w]=len(w)
    return d

def lngstwrd(d):
    print("*"*80)
    print("\t\tWORD\tLENGTH")
    print("*"*80)
    for word in d:
        print("\t\t{}\t{}".format(word,d.get(word)))
    print("*"*80)
    num=[]
    for l in d.values():
        num.append(l)  
        print("{}".format(num))   
        return num
        mx=num[0]
        for v in num:
            if v>mx:
                mx=v
        return mx
    maxlenwrd=[]
    for words,length in d.items():
        if(mx==length):
            maxlenwrd.append(words)
        else:
            print("MAXLENGTHWORD")
            print("{}".format(maxlenwrd))
    

    

l=readwords()
print("{}".format(l))
k=lenwrd(l)
print("{}".format(k))
lngstwrd(k)
