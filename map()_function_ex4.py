# program which accepts the list of salaries of employees from keyboard and give 50% hike to the old salaries of employees and get the new salary list using map() of function
def newsal(s):
    s=s+s*0.5
    return s
print("Enter the list of salary of all employees")
oldsal=[float(sal)for sal in input().split() if float(sal)>0]
print("The old salary list is : {}".format(oldsal))
newsalist=list(map(newsal,oldsal))
print("*"*50)
print("The list of new salary is {}".format(newsalist))
print("*"*50)
for olds,new in zip(oldsal,newsalist):
    print("\t\t{}\t\t{}".format(olds,new))