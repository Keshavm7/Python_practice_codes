# program which accepts the list of salaries of employees from keyboard and give 50% hike to the old salaries of employees and get the new salary list using map() of function
print("Enter old salary list of employees seperated by space")
oldsal=[float(sal) for sal in input().split() if float(sal)>0 ]
newsal=list(map(lambda s:s+s*0.5,oldsal))
print("The new salary list is {}".format(newsal))