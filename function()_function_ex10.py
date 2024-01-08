# program which will obtain the reverse of words without using string slicing using filter() function.
def revs(p):
    for i in range(len(p)-1,-1,-1):
        wd=""
        wd=wd+p[i]
    return wd

print("Enter list of words seperated by space")
lst=[word[::-1] for word in input().split()]
rev=list(filter(lambda w:revs(w),lst))
print("The palindrome list of given word list is:{}".format(rev))