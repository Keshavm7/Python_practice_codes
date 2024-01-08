# There is given line of mixedcharacters filter uppercase alphabets and sort them in Ascending order,filter uppercase alphabets and sort them in Ascending order.
# filter even digits sort them in Descending order,filter odd digits sort them in Ascending order.
def check1(p):
    res=True
    for i in p:
        if((i.isdigit()==True)) and (i%2==0))
            return res
         
            
"""def check2(p):
    if(p.isdigit()==True):
        if(p%2!=0):
            return True"""
    

str=("String4378ForMat95")
lst=list(str)
print(lst)
res1=list(filter(lambda w:w.isupper(),lst))
res2=list(filter(lambda w:w.islower(),lst))
res3=list(filter(lambda w:check1(w),lst))
""""res4=list(filter(lambda w:check2,lst))"""
print("The list of uppercase letters is {}".format(res1))
print("The list of lower letters is {}".format(res2))
print("The list of Even numbers is {}".format(res3))
# print("The list of odd numbers letters is {}".format(res1.sort()))
