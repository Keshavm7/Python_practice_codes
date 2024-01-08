def rev(r):
    p= lambda r:r[::-1]
    return p
print("Enter list of words seperated by space")
lst=[word[::-1] for word in input().split()]
rev=list(filter(lambda w:rev(w),lst))
print("The reverse order of given list of words:{}".format(rev))