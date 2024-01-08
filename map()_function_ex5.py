# program which will compute sum of two list elements using map() function
lst1=[10,20,30,40]
lst2=[100,200,300,400]
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("{}".format(lst3))