# set category datatype

""">>> lst=[10,25,34,"Rossum","GUIDO",35.45]
>>> print(lst,type(lst))
[10, 25, 34, 'Rossum', 'GUIDO', 35.45] <class 'list'>
>>>
>>>
>>> lst[2]
34
>>> lst[0]
10
>>> lst[5]
35.45
>>> lst[25]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
>>>
>>> lst[0:25]
[10, 25, 34, 'Rossum', 'GUIDO', 35.45]
>>>
>>>
>>> lst[-25:-25]
[]
>>> lst[-25:-1]
[10, 25, 34, 'Rossum', 'GUIDO']
>>> lst[-25:]
[10, 25, 34, 'Rossum', 'GUIDO', 35.45]
>>>
>>>
>>> lst[0:]
[10, 25, 34, 'Rossum', 'GUIDO', 35.45]
>>>
>>>
>>> lst[0::2]
[10, 34, 'GUIDO']
>>> lst[::-1]
[35.45, 'GUIDO', 'Rossum', 34, 25, 10]
>>>
>>>
>>> lst[-1:-8:1]
[]
>>> lst[-1:-6:1]
[]
>>> lst[-6:-1]
[10, 25, 34, 'Rossum', 'GUIDO']
>>> lst[-1:-4:-1]
[35.45, 'GUIDO', 'Rossum']
>>>
>>>
>>> lst[-1:-8:-1]
[35.45, 'GUIDO', 'Rossum', 34, 25, 10]
>>> lst[0:100:1]
[10, 25, 34, 'Rossum', 'GUIDO', 35.45]
>>>
>>>
>>>
>>> lst=[10,24,"FAN",[25,34,67],"GUIDO",[1,2,3,4]]
>>>
>>> lst[0]
10
>>> lst[1]
24
>>>
>>> lst[2]
'FAN'
>>>
>>> lst[3]
[25, 34, 67]
>>>
>>> lst[3].append(255)
>>>
>>>
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', [1, 2, 3, 4]]
>>>
>>>
>>> lst[4]
'GUIDO'
>>>
>>> lst[5]
[1, 2, 3, 4]
>>> lst[5].clear()
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', []]
>>>
>>>
>>> lst[5].append(25)
>>>
>>>
>>> lst[5].append(36)
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', [25, 36]]
>>>
>>>
>>> lst.insert(6,"MAC")
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', [25, 36], 'MAC']
>>>
>>>
>>>
>>> lst[5].insert(-1,"JAMES")
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', [25, 'JAMES', 36], 'MAC']
>>>
>>>
>>> lst.append(25)
>>>
>>>
>>> lst.insert(-2,"Kinney")
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', [25, 'JAMES', 36], 'Kinney', 'MAC', 25]
>>>
>>>
>>> lst.remove(25)
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', [25, 'JAMES', 36], 'Kinney', 'MAC']
>>>
>>> lst[5]
[25, 'JAMES', 36]
>>>
>>>
>>> lst[5].remove(25)
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', ['JAMES', 36], 'Kinney', 'MAC']
>>>
>>>
>>> [].clear()
>>>
>>>
>>> [].clear()
>>>
>>> print([].clear())
None
>>>
>>>
>>> print([].remove(25))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>>
>>>
>>>
>>>
>>> lst.pop()
'MAC'
>>>
>>> print(lst)
[10, 24, 'FAN', [25, 34, 67, 255], 'GUIDO', ['JAMES', 36], 'Kinney']
>>> lst.pop()
'Kinney'
>>>
>>>
>>> lst.pop(-3)
[25, 34, 67, 255]
>>>
>>> print(lst)
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36]]
>>>
>>>
>>>
>>> lst2=lst.copy()
>>>
>>> print(lst2)
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36]]
>>>
>>>
>>> id(lst2)
1667013432960
>>>
>>>
>>> id(lst)
1667014929664
>>>
>>>
>>> lst2=lst
>>> print(lst2,id(lst2))
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36]] 1667014929664
>>> lst2.append(1)
>>>
>>> print(lst2,id(lst2))
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1] 1667014929664
>>> print(lst,id(lst))
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1] 1667014929664
>>>
>>>
>>> lst.count(1)
1
>>> lst.count(24)
1
>>>
>>>
>>> lst.index(24)
1
>>>
>>>
>>> lst.index(36)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 36 is not in list
>>> lst[4].index(36)
1
>>>
>>>
>>>
>>> lst.extend(lst2)
>>> print(lst)
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1]
>>>
>>>
>>> lst3=lst
>>>
>>> lst=lst2+lst3
>>> print(lst)
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1]
>>>
>>>
>>> lst=lst2*lst3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'list'
>>>
>>>
>>>
>>>
>>> del lst[24]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>>
>>> del lst[2]
>>>
>>> print(lst)
[10, 24, 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1]
>>>
>>>
>>> del lst[0:10]
>>> print(lst)
[1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1]
>>> del lst[0:10]
>>> print(lst)
['GUIDO', ['JAMES', 36], 1]
>>>
>>>
>>>
>>>
>>>
>>> lst.reverse()
>>> print(lst)
[1, ['JAMES', 36], 'GUIDO']
>>>
>>>
>>>
>>> lst.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'list' and 'int'
>>>
>>>
>>> lst[1].sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
>>>
>>>
>>> del lst
>>> print(lst)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lst' is not defined. Did you mean: 'lst2'?
>>>
>>>
>>>
>>> s="Python"
>>> print(s)
Python
>>>
>>>
>>> s[]0
  File "<stdin>", line 1
    s[]0
      ^
SyntaxError: invalid syntax
>>>
>>>
>>> s[0]
'P'
>>>
>>>
>>> del s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object doesn't support item deletion
>>>
>>>
>>> s.append("l")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'
>>>
>>>
>>>
>>>
>>> del s[0:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item deletion
>>>
>>>
>>>
>>> lst=lst2
>>> print(lst)
[10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1, 10, 24, 'FAN', 'GUIDO', ['JAMES', 36], 1]
>>>
>>>
>>>
>>> lst1=lst.reverse()
>>> print(lst1)
None
>>>
>>>
>>> print(lst)
[1, ['JAMES', 36], 'GUIDO', 'FAN', 24, 10, 1, ['JAMES', 36], 'GUIDO', 'FAN', 24, 10]
>>>
>>>
>>> for i,v in lst:
...
...
  File "<stdin>", line 3

    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>>
>>>
>>>
>>>
>>> print(lst)
[1, ['JAMES', 36], 'GUIDO', 'FAN', 24, 10, 1, ['JAMES', 36], 'GUIDO', 'FAN', 24, 10]
>>>
>>> for i,v in enumerate(lst):
...     print("i","---->","v")
...
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
i ----> v
>>> for i,v in enumerate(lst):
...     print(i,"--->",v)
...
0 ---> 1
1 ---> ['JAMES', 36]
2 ---> GUIDO
3 ---> FAN
4 ---> 24
5 ---> 10
6 ---> 1
7 ---> ['JAMES', 36]
8 ---> GUIDO
9 ---> FAN
10 ---> 24
11 ---> 10
>>>
>>>
>>>
>>>
>>>
>>> s="MISSISSIPPI"
>>> print(s)
MISSISSIPPI
>>>
>>> for i,v in enumerate(s:)
  File "<stdin>", line 1
    for i,v in enumerate(s:)
                          ^
SyntaxError: invalid syntax
>>> for i,v in enumerate(s):
...     if(v=="i":)
  File "<stdin>", line 2
    if(v=="i":)
             ^
SyntaxError: invalid syntax
>>> for i,v in enumerate(s):
...     if(v=="i"):
...             print(i,"  ",v)
...
>>>
>>>
>>>
>>> for i,v in enumerate(s):
...     if(v=="I"):
...             print(i,"   ",v)
...
1     I
4     I
7     I
10     I
>>>
>>>
>>> for i,v in enumerate(s):
...     if(v=="S"):
...             print(i)
...
2
3
5
6
>>> for i,v in enumerate(s):
...     if(v=="I"):
...             print(i,end="---->")
...
1---->4---->7---->10---->>>>
>>>
>>>
>>>
>>>
>>> s="PHILLIPINES"
>>> print(list(s))
['P', 'H', 'I', 'L', 'L', 'I', 'P', 'I', 'N', 'E', 'S']
>>>
>>> print(s)
PHILLIPINES
>>>
>>>
>>> s=list(s)
>>>
>>>
>>> print(s)
['P', 'H', 'I', 'L', 'L', 'I', 'P', 'I', 'N', 'E', 'S']
>>>
>>> s.count(H)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'H' is not defined
>>>
>>>
>>> s.count('H')
1
>>>
>>>
>>> s.count('I')
3
>>>
>>>
>>>
>>> s="This is python world"
>>>
>>> s=list(s)
>>>
>>> print(s)
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'w', 'o', 'r', 'l', 'd']
>>>
>>>
>>> s.count(' ')
3
>>>
>>>
>>> s="123456"
>>> print(s)
123456
>>>
>>>
>>> s=list(s)
>>>
>>>
>>> print(s)
['1', '2', '3', '4', '5', '6']
>>>
>>>
>>> s.count(1)
0
>>>
>>>
>>> s.count('4')
1
>>>
>>>
>>> s.count(5)
0
>>>
>>>
>>> [].count(0)
0
>>>
>>>
>>> [].count(100)
0
>>>
>>>
>>>
>>> s=100
>>> print(s,type(s))
100 <class 'int'>
>>>
>>>
>>> s=(100)
>>> print(s,type(s))
100 <class 'int'>
>>>
>>>
>>> s=(100,)
>>> print(s,type(s))
(100,) <class 'tuple'>
>>>
>>>
>>>
>>> s="Pyhton"
>>> print(tuple(s))
('P', 'y', 'h', 't', 'o', 'n')
>>>
>>>
>>>
>>> s=("Python")
>>> print(s,type(s))
Python <class 'str'>
>>>
>>>
>>> s=("LG",)
>>> print(s,type(s))
('LG',) <class 'tuple'>
>>>
>>>
>>>
>>>
>>> >>> t1=(10,"Rossum",[17,16,18],[77,78,66],"OUCET")
  File "<stdin>", line 1
    >>> t1=(10,"Rossum",[17,16,18],[77,78,66],"OUCET")
    ^^
SyntaxError: invalid syntax
>>>
>>>
>>> t1=(10,"Rossum",[17,16,18],[77,78,66],"OUCET")
>>> print(t1)
(10, 'Rossum', [17, 16, 18], [77, 78, 66], 'OUCET')
>>>
>>>
>>>
>>> t1.append(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>>
>>>
>>> t1[2].append(25)
>>>
>>>
>>> print(t1)
(10, 'Rossum', [17, 16, 18, 25], [77, 78, 66], 'OUCET')
>>>
>>>
>>> t1[3].insert(1,355)
>>> print(t1)
(10, 'Rossum', [17, 16, 18, 25], [77, 355, 78, 66], 'OUCET')
>>>
>>>
>>>
>>> t1.count(10)
1
>>>
>>>
>>> t1.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'
>>>
>>>
>>>
>>>
>>> t2=sorted(t1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> t2=sorted(t1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>>
>>> t1=(25,654,-25)
>>> t2=sorted(t1)
>>> print(t2)
[-25, 25, 654]
>>>
>>>
>>> print(t1)
(25, 654, -25)
>>> t1=tuple(t2)
>>> print(t1)
(-25, 25, 654)
>>>
>>>
>>>
>>> s={10,20,39,"Python","25.34","Odd"}
>>> print(s)
{'Python', 20, 39, '25.34', 10, 'Odd'}
>>>
>>> s[0]="Prn"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support item assignment
>>>
>>>
>>>
>>>
>>> s.add(25)
>>>
>>> print(s)
{'Python', 20, 39, '25.34', 25, 10, 'Odd'}
>>>
>>>
>>>
>>> s="Python"
>>> s2=set(s)
>>> print(s2)
{'t', 'o', 'h', 'P', 'n', 'y'}
>>>
>>>
>>> s[0:]
'Python'
>>>
>>> s={25,45,39,47,48,"ADD","SUB"}
>>> print(s)
{48, 'SUB', 39, 'ADD', 25, 45, 47}
>>>
>>>
>>> s[::]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>>
>>>
>>> s[0:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>>
>>>
>>>
>>> s[::-1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>>
>>>
>>>
>>>
>>>
>>>
>>> s={}
>>> s.add(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'add'
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> s=set()
>>> s.add(20)
>>> s.add("DAM")
>>> s.add('25.34')
>>> print(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> print(s)
{'25.34', 20, 'DAM'}
>>>
>>>
>>>
>>> s={25,36.54,"IRN","2+3j",2+5j}
>>> print(s)
{(2+5j), 36.54, 'IRN', '2+3j', 25}
>>>
>>>
>>> s.add(25)
>>>
>>>
>>> s[2]="ION"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support item assignment
>>>
>>>
>>>
>>> set().add(25)
>>> print(set().add(25,45))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set.add() takes exactly one argument (2 given)
>>>
>>>
>>> print(set().add(20))
None
>>>
>>>
>>>
>>>
>>>
>>> s=set().clear
>>> s.clear()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'clear'
>>>
>>>
>>>
>>> s={25,34,"Rossum","James","Wright"}
>>> s.clear()
>>> print(s)
set()
>>> s.clear()
>>> print(s.clear())
None
>>>
>>>
>>>
>>>  s={25,34,"Rossum","James","Wright"}
  File "<stdin>", line 1
    s={25,34,"Rossum","James","Wright"}
IndentationError: unexpected indent
>>>  s={25,34,"Rossum","James","Wright"}
  File "<stdin>", line 1
    s={25,34,"Rossum","James","Wright"}
IndentationError: unexpected indent
>>> s={25,34,"Rossum","James","Wright"}
>>>
>>> print(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> print(s)
{34, 'Wright', 'Rossum', 25, 'James'}
>>>
>>>
>>>
>>>
>>> s.remove(25)
>>> print(s)
{34, 'Wright', 'Rossum', 'James'}
>>>
>>>
>>>
>>> s.remove(25)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 25
>>>
>>>
>>>
>>> s.remove(34)
>>>
>>>
>>> print(s)
{'Wright', 'Rossum', 'James'}
>>>
>>>
>>>
>>>
>>> s={25,34,98,87,"MAC","KINNEY"}
>>> print(s)
{'KINNEY', 34, 98, 87, 25, 'MAC'}
>>>
>>>
>>>
>>> s.discard()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set.discard() takes exactly one argument (0 given)
>>>
>>>
>>>
>>> s.discard()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set.discard() takes exactly one argument (0 given)
>>>
>>>
>>> set.discard(25)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'discard' for 'set' objects doesn't apply to a 'int' object
>>> s.discard(25)
>>> print(s)
{'KINNEY', 34, 98, 87, 'MAC'}
>>>
>>>
>>> s.discard(34)
>>> print(s)
{'KINNEY', 98, 87, 'MAC'}
>>>
>>>
>>> s.discard(100)
>>> s.discard(655)
>>>
>>>
>>> s.remove(254)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 254
>>>
>>>
>>>
>>> print(s)
{'KINNEY', 98, 87, 'MAC'}
>>>
>>>
>>>
>>> s.pop()
'KINNEY'
>>> s.pop()
98
>>> s.pop()
87
>>> s.pop()
'MAC'
>>> s.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
>>>
>>>
>>> s.opo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'opo'
>>>
>>> s.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
>>>
>>>
>>>
>>>
>>> s1={254,365,456,"HINT","GOsling"}
>>>
>>> s1.pop()
456
>>> s1.pop()
'HINT'
>>> print(s1)
{'GOsling', 365, 254}
>>>
>>>
>>> s1.pop()
'GOsling'
>>> s1.pop()
365
>>> s1.pop()
254
>>>
>>>
>>> s1={10,20,30,40}
>>> s2={10,15,25}
>>> s3={15,25,35}
>>>
>>> s1.isdisjoint(s2)
False
>>> s1.isdisjoint(s3)
True
>>>
>>>
>>> s3.isdisjoint(s1)
True
>>>
>>>
>>> s3.isdisjoint(s2)
False
>>>
>>>
>>> s2.isdisjoint(s2)
False
>>>
>>>
>>>
>>> s1.issuperset(s2)
False
>>>
>>> s1={10,20,30,15,25,65,45}
>>> s1={10,20,65}
>>> s1={10,20,30,15,25,65,45}
>>> s2={10,30,65}
>>> s3={15,25,45}
>>>
>>>
>>> s1.issuperset(s2)
True
>>>
>>> s1.issuperset(s3)
True
>>>
>>>
>>> s1.issuperset(s1)
True
>>>
>>> s2.issuperset(s1)
False
>>>
>>>
>>> s2.issubset(s3)
False
>>>
>>>
>>> s2.issubset(s1)
True
>>>
>>>
>>> s3.issubset(s1)
True
>>>
>>>
>>> s1.union(s2)
{65, 10, 45, 15, 20, 25, 30}
>>> s2.union(s3)
{65, 25, 10, 45, 30, 15}
>>>
>>> s3.union(s1)
{65, 10, 45, 15, 20, 25, 30}
>>>
>>>
>>> s4=s1.intersection(s2)
>>> print(s4)
{65, 10, 30}
>>>
>>> s4=s2.union(s3)
>>>
>>> print(s4)
{65, 25, 10, 45, 30, 15}
>>>
>>>
>>>
>>>
>>> s4=s2.difference(s3)
>>> print(s4)
{65, 10, 30}
>>>
>>> s4=s3.difference(s1)
>>> print(s4)
set()
>>>
>>>
>>>
>>> s4=s3.symmetric_difference(s1)
>>> print(s4)
{65, 20, 10, 30}
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> s={10,20,30}
>>> s1={"Van",'Guido',"Ross"}
>>>
>>> s3=s.update(s1)
>>> print(s3)
None
>>>
>>> print(s)
{'Ross', 'Guido', 20, 'Van', 10, 30}
>>>
>>>
>>>
>>> s3=s.symmetric_difference_update(s1)
>>>
>>> print(s3)
None
>>>
>>> print(s)
{20, 10, 30}
>>>
>>>
>>>
>>> s=[25,64,94,34,"JASEN","SAM"]
>>> f=frozenset(s)
>>> print(f)
frozenset({64, 'SAM', 34, 'JASEN', 25, 94})
>>>
>>> s={24,34,64,14,"YEAR","GUIDO"}
>>> f=frozenset(s)
>>> print(f)
frozenset({64, 34, 'GUIDO', 24, 'YEAR', 14})
>>>
>>>
>>> s=(10,34,97,"UID","KIM")
>>> print(frozenset(s))
frozenset({97, 34, 10, 'KIM', 'UID'})
>>> f[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'frozenset' object is not subscriptable
>>>
>>>
>>>
>>> del f[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'frozenset' object doesn't support item deletion
>>>
>>>
>>>
>>> del f
>>> print(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'f' is not defined
>>>
>>>
>>>
>>>
>>> s=[10,25,45,"Science","DATA"]
>>> fs=frozenset(s)
>>> print(fs)
frozenset({'Science', 'DATA', 10, 45, 25})
>>>
>>>
>>> fs2=fs.copy()
>>> print(fs2)
frozenset({'Science', 'DATA', 10, 45, 25})
>>>
>>>
>>>
>>>
>>> id(fs2)
1667014211424
>>>
>>>
>>>
>>> id(fs)
1667014211424
>>>
>>>
>>>
>>>
>>> fs3=fs2.isdisjoint(fs)
>>> print(fs3)
False
>>>
>>>
>>>
>>>
>>> fs2.issubset(fs)
True
>>>
>>>
>>>
>>> fs2.issuperset(fs)
True
>>>
>>>
>>>
>>> fs.union(fs2)
frozenset({'Science', 'DATA', 10, 45, 25})
>>>
>>>
>>>
>>>
>>> fs.intersection(fs2)
frozenset({'Science', 'DATA', 10, 45, 25})
>>>
>>>
>>> fs.difference(fs2)
frozenset()
>>>
>>>
>>>
>>> fs2.difference(fs)
frozenset()
>>>
>>>
>>> fs2.symmetric_difference(fs)
frozenset()
>>>
>>>
>>>
"""