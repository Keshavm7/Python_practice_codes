# program which will compute sum of two list elements whose length is different using map() function
print("Enter list of values in following object")
lst1=[int(val) for val in input().split()]

print("Enter list of values in following list object")
lst2=[int(val2) for val2 in input().split()]
print("The list 1={}".format(lst1))
print("The list 2={}".format(lst2))
if(len(lst1)<len(lst2)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
elif(len(lst1)>len(lst2)):
    for j in range(len(lst1)-len(lst2)):
        lst2.append(0)


lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("The sum of two list is:{}".format(lst3))

for p,q,r in zip(lst1,lst2,lst3):
    print("\t\t{}\t\t{}\t\t{}".format(p,q,r))