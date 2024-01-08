# 17 predefined functions that can be used to do operations on str object

# 1. capitalize()

s="mumbai is financial capital of india."
print(s)
p=s.capitalize()
print(p)

r="python"
print(r)
z=r.capitalize()
print(z)

line="python is easy to learn.It is high level language."
line=line.capitalize()
print(line)

line="python is OOP language."
line=line.capitalize()
print(line,type(line))


# 2. title()
s="mumbai"
s=s.capitalize()
print(s,type(s))

s="mumbai"
s=s.title()
print(s,type(s))

snt="india is beautiful country."
snt=snt.title()
pnt=snt.capitalize()
print(snt,type(snt))
print(pnt,type(pnt))

snt="a b c d e f g h "
snt=snt.title()
pnt=snt.capitalize()
print(snt,type(snt))
print(pnt,type(pnt))

# 3.index()

s="Python"
print(s.index('P'))
print(s.index('y'))
print(s.index('t'))
print(s.index('h'))
print(s.index('o'))
print(s.index('n'))

p="I am learning Python language."
print(p.index('n')) # only provides index of first occurance of value.

# 4.upper()

s="python"
print(s.upper())

s="this is vs code application."
print(s.upper())

# 5.lower()
 
s="HYDARBAD"
print(s.lower())

s="HYDERBAD IS CAPITAL OF TELANGANA STATE."
print(s.lower())

s="PYThon"
s=s.lower()
print(s)

# 6.isupper()

s="PYTHON"
s=s.isupper()
print(s)

s="Data Science"
s=s.isupper()
print(s)

s="DATA SCIENCE"
s=s.isupper()
print(s)

s="DATA123"
s=s.isupper()
print(s)  #TRUE

s="&$Science"
s=s.isupper() #FALSE
print(s)

s="&$SCIENCE"
s=s.isupper() #FALSE
print(s)

# 7.islower()

s="java"
print(s.islower())

s="java1234"
print(s.islower())

s="javA"
print(s.islower())

s="java$@&"
print(s.islower())

s="java$@&"
print(s.islower())

s="&$science"
s=s.islower() 
print(s)

s="123"
print(s.islower())

# 8.isalpha()

p="AMbigous"
print(p.isalpha())

p="AMBIGOUS"
print(p.isalpha())

p="ambigous"
print(p.isalpha())

p="ambigous1234"
print(p.isalpha())

p="ambigous%$#"
print(p.isalpha())

p="this is my practice code"
print(p.isalpha())

p="thisismypracticecode"
print(p.isalpha())

# 9.isdigit()

p="interpreter"
print(p.isdigit())

p="interpreter123"
print(p.isdigit())

p="123456"
print(p.isdigit())

p="1234#$%"
print(p.isdigit())

p="1 2 3"
print(p.isdigit())

# 10. isalnum()

p="interpreter"
print(p.isalnum())

p="interpreter123"
print(p.isalnum())

p="123456"
print(p.isalnum())

p="1234#$%"
print(p.isalnum())

p="1 2 3"
print(p.isalnum())


# 11.isspace()

s=""
print(s.isspace())

s=" "
print(s.isspace())

s="the Subject "
print(s.isspace())

s="1 2 2"
print(s.isspace())


# 12.split()

s="python is high level language."
print(s.split())

s="12-02-2025"
print(s.split('-'))

s="apple/mango-grapes/"
print(s.split('/'))

s="python supports many libraries."
p=s.split(' ')
print(p,type(p))

# 13.join()

l=["SC","IE","N","CE"]
s=""
print(s.join(l))

l=["Rossum","Developed","Python","Language"]
s=" "
print(s.join(l))

# 14.startswith()

s="GUIDO-VAN-ROSSUM"
print(s.startswith('GUIDO'))

s="GUIDO-VAN-ROSSUM"
print(s.startswith('VAN'))

s="GUIDO-VAN-ROSSUM"
print(s.startswith('GUI'))

s="GUIDO-VAN-ROSSUM"
print(s.startswith('G'))

# 15.endswith()

s="GUIDO-VAN-ROSSUM"
print(s.endswith('M'))

s="GUIDO-VAN-ROSSUM"
print(s.endswith('AVN'))

s="GUIDO-VAN-ROSSUM"
print(s.endswith('SSUM'))

s="GUIDO-VAN-ROSSUM"
print(s.endswith('GUIDO'))

s="GUIDO-VAN-ROSSUM"
print(s.startswith('GUIDO'))

s="GUIDO-VAN-ROSSUM"
print(s.startswith('VAN'))

s="GUIDO-VAN-ROSSUM"
print(s.startswith('GUI'))

s="GUIDO-VAN-ROSSUM"
print(s.endswith('m'))

# 16.swapcase()

s="pYTHon"
print(s.swapcase())

s="python"
print(s.swapcase())

s="PYTHON"
print(s.swapcase())

# 17.enumerate()

s="synopsys"
for i,v in enumerate(s):
    print("index={},value={}".format(i,v))
    
s="Python is developed by GUIDO VAN ROSSUM"
for i,v in enumerate(s):
    print("index={},value={}".format(i,v))   