# dict category datatypes

""" s=["Apple","Orange","grapes","Mango"]
>>> print(s,type(s))
['Apple', 'Orange', 'grapes', 'Mango'] <class 'list'>
>>>
>>>
>>> d=dict(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>> s=["Apple","Orange","grapes","Mango"]
>>> print(dict(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>>
>>> l=["a1","a2","a3","a4"]
>>> print(l)
['a1', 'a2', 'a3', 'a4']
>>>
>>> d=dict(l)
>>> print(d)
{'a': '4'}
>>>
>>>
>>> d={254,45}
>>> print(d,type(d))
{45, 254} <class 'set'>
>>>
>>>
>>>
>>> d=("STR")
>>> print(d,type(d))
STR <class 'str'>
>>>
>>>
>>>
>>>
>>> d=("STR",)
>>> print(d,type(d))
('STR',) <class 'tuple'>
>>>
>>>
>>>
>>> d={}
>>> print(type(d))
<class 'dict'>
>>>
>>>
>>> d={10}
>>> print(type(d))
<class 'set'>
>>>
>>>
>>>
>>> d={10:}
  File "<stdin>", line 1
    d={10:}
         ^
SyntaxError: expression expected after dictionary key and ':'
>>> d={1:sno}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sno' is not defined
>>> d={1:"sno"}
>>> print(type(d))
<class 'dict'>
>>>
>>>
>>>
>>> d={10:25.4,20:45.4,30:4.12,40:54.4}
>>> print(d,type(d))
{10: 25.4, 20: 45.4, 30: 4.12, 40: 54.4} <class 'dict'>
>>>
>>>
>>>
>>> d=
  File "<stdin>", line 1
    d=
      ^
SyntaxError: invalid syntax
>>> cls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cls' is not defined
>>>
>>>
>>>
>>>
>>> d={1:"MH",2:"JK",3:"KV",4:"RV"}
>>> print(d,type(d))
{1: 'MH', 2: 'JK', 3: 'KV', 4: 'RV'} <class 'dict'>
>>>
>>>
>>> d={10:kl}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'kl' is not defined. Did you mean: 'l'?
>>>
>>>
>>> d={KL:14}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'KL' is not defined
>>>
>>>
>>>
>>> d={"MS":"Wk/Bat","VK":"Bat","RA":"Bl","KL":"Bat"}
>>> print(d,type(d))
{'MS': 'Wk/Bat', 'VK': 'Bat', 'RA': 'Bl', 'KL': 'Bat'} <class 'dict'>
>>>
>>>
>>> for i in d:
...     print(i)
...
MS
VK
RA
KL
>>>
>>> for v in d:
...     print(v)
...
MS
VK
RA
KL
>>> for i,v in d:
...     print(i,v)
...
M S
V K
R A
K L
>>> for i,v in d.items():
...     print(i,v)
...
MS Wk/Bat
VK Bat
RA Bl
KL Bat
>>>
>>>
>>> for i,v in d:
...     print(i,d.get(i))
...
M None
V None
R None
K None
>>>
>>>
>>> d[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 10
>>>
>>>
>>> d[KL]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'KL' is not defined
>>>
>>> d["KL"]
'Bat'
>>>
>>>
>>>
>>> d["MS"]
'Wk/Bat'
>>>
>>>
>>>
>>>
>>> d[MS]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'MS' is not defined
>>>
>>>
>>>
>>> d["MS"]
'Wk/Bat'
>>>
>>>
>>>
>>>
>>> d["RA"]
'Bl'
>>>
>>>
>>>
>>>
>>> d={}
>>> d[10]="ST"
>>> print(d)
{10: 'ST'}
>>>
>>>
>>>
>>> d[10]="MS"
>>>
>>> print(d)
{10: 'MS'}
>>>
>>>
>>> d[10]=MS
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'MS' is not defined
>>>
>>>
>>>
>>> d[10]="ST"
>>> d[7]="MS"
>>> d[18]="VK"
>>> d[8]="RJ"
>>>
>>>
>>> print(d)
{10: 'ST', 7: 'MS', 18: 'VK', 8: 'RJ'}
>>>
>>>
>>> for i,v in d.items():
...     print(i,v,end=" ")
...
10 ST 7 MS 18 VK 8 RJ >>>
>>>
>>> for i,v in d.items():
...     print(i,"---->",v)
...
10 ----> ST
7 ----> MS
18 ----> VK
8 ----> RJ
>>>
>>>
>>>
>>> len(d)
4
>>>
>>>
>>>
>>> d=dict()
>>> print(len(d))
0
>>>
>>>
>>> d={}
>>> len(d)
0
>>>
>>>
>>>
>>>
>>>
>>> d={10:"Python",20:"JAVA",30:"AWS",40:"SQL"}
>>> d1={1:"POWERbi",2:"TABLEAU",3:"EXCEL","MATPLOTLIB"}
  File "<stdin>", line 1
    d1={1:"POWERbi",2:"TABLEAU",3:"EXCEL","MATPLOTLIB"}
                                                     ^
SyntaxError: ':' expected after dictionary key
>>> d1={1:"POWERbi",2:"TABLEAU",3:"EXCEL",4:"MATPLOTLIB"}
>>>
>>>
>>> d2={10:"MK",20:"GK"}
>>>
>>> print(d2,type(d2))
{10: 'MK', 20: 'GK'} <class 'dict'>
>>>
>>> d2.clear()
>>>
>>> print(d2)
{}
>>>
>>> len(d2)
0
>>>
>>>
>>> d2.clear()
>>>
>>>
>>> print(d2.clear())
None
>>>
>>> print(d)
{10: 'Python', 20: 'JAVA', 30: 'AWS', 40: 'SQL'}
>>> print(d1)
{1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOTLIB'}
>>>
>>>
>>>
>>> d.pop(10)
'Python'
>>>
>>> d.pop()20
  File "<stdin>", line 1
    d.pop()20
           ^^
SyntaxError: invalid syntax
>>> d.pop(250)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 250
>>>
>>>
>>> print(d)
{20: 'JAVA', 30: 'AWS', 40: 'SQL'}
>>>
>>>
>>>
>>> d[10]="PYTHON"
>>>
>>> print(d)
{20: 'JAVA', 30: 'AWS', 40: 'SQL', 10: 'PYTHON'}
>>>
>>>
>>> d.popitem()
(10, 'PYTHON')
>>>
>>>
>>> d.popitem()
(40, 'SQL')
>>>
>>>
>>> print(d)
{20: 'JAVA', 30: 'AWS'}
>>>
>>>
>>>
>>> d[10]="PYTHON"
>>> d[40]="SQL"
>>>
>>> print(d)
{20: 'JAVA', 30: 'AWS', 10: 'PYTHON', 40: 'SQL'}
>>>
>>>
>>>
>>> d.get(10)
'PYTHON'
>>> d.get(20)
'JAVA'
>>> for i in d.items():
...     print(d.get(i))
...
None
None
None
None
>>> for i in d.items():
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>>
>>>
>>>
>>> for i in d:
...     print(i)
...
20
30
10
40
>>> for i in d:
...     print(d.get(i))
...
JAVA
AWS
PYTHON
SQL
>>>
>>>
>>> for i,v in d.items():
...     print(i,v)
...
20 JAVA
30 AWS
10 PYTHON
40 SQL
>>>
>>>
>>> print(d)
{20: 'JAVA', 30: 'AWS', 10: 'PYTHON', 40: 'SQL'}
>>> print(d1)
{1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOTLIB'}
>>>
>>>
>>> d3=d1.copy()
>>> print(d3)
{1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOTLIB'}
>>>
>>>
>>>
>>> d3[4]="MATPLOT"
>>>
>>> print(d3)
{1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOT'}
>>>
>>>
>>> d1[5]="PANDAS"
>>> print(d1)
{1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOTLIB', 5: 'PANDAS'}
>>>
>>>
>>> v=d.keys()
>>> print(v)
dict_keys([20, 30, 10, 40])
>>>
>>> type(v)
<class 'dict_keys'>
>>>
>>>
>>> l=d1.keys()
>>> print(l)
dict_keys([1, 2, 3, 4, 5])
>>>
>>>
>>> type(l)
<class 'dict_keys'>
>>>
>>> d.values()
dict_values(['JAVA', 'AWS', 'PYTHON', 'SQL'])
>>> d.keys()
dict_keys([20, 30, 10, 40])
>>>
>>>
>>> d1.values()
dict_values(['POWERbi', 'TABLEAU', 'EXCEL', 'MATPLOTLIB', 'PANDAS'])
>>>
>>>
>>> d1.keys()
dict_keys([1, 2, 3, 4, 5])
>>>
>>>
>>> d1.items()
dict_items([(1, 'POWERbi'), (2, 'TABLEAU'), (3, 'EXCEL'), (4, 'MATPLOTLIB'), (5, 'PANDAS')])
>>>
>>>
>>> print(d)
{20: 'JAVA', 30: 'AWS', 10: 'PYTHON', 40: 'SQL'}
>>>
>>> print(d1)
{1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOTLIB', 5: 'PANDAS'}
>>>
>>>
>>> d1[10]="EXCEL"
>>> d1[20]="PANDAS"
>>> print(d1)
{1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOTLIB', 5: 'PANDAS', 10: 'EXCEL', 20: 'PANDAS'}
>>>
>>>
>>>
>>>
>>> d.update(d1)
>>>
>>> print(d)
{20: 'PANDAS', 30: 'AWS', 10: 'EXCEL', 40: 'SQL', 1: 'POWERbi', 2: 'TABLEAU', 3: 'EXCEL', 4: 'MATPLOTLIB', 5: 'PANDAS'}
>>>
>>>
>>> df={10:"ST",7:"MS",8:"RJ","Young":{1:"SG",2:"YJ",3:"RS",4:"AS"},99:"LM"}
>>> print(df,type(df))
{10: 'ST', 7: 'MS', 8: 'RJ', 'Young': {1: 'SG', 2: 'YJ', 3: 'RS', 4: 'AS'}, 99: 'LM'} <class 'dict'>
>>>
>>>
>>> for i,v in df.items():
...     print(i,v)
...
10 ST
7 MS
8 RJ
Young {1: 'SG', 2: 'YJ', 3: 'RS', 4: 'AS'}
99 LM
>>>
>>> for r in df.keys():
...     print(r)
...
10
7
8
Young
99
>>> for n,name in df:
...     print(n,"--->",name)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot unpack non-iterable int object
>>>
>>>
>>> for n,name in df:
...     print(n,"--->",df.get(n))
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot unpack non-iterable int object
>>>
>>>
>>>
>>>
>>>
>>>
>>> for n in df:
...     print(n,"---->",df.get(n))
...
10 ----> ST
7 ----> MS
8 ----> RJ
Young ----> {1: 'SG', 2: 'YJ', 3: 'RS', 4: 'AS'}
99 ----> LM
>>>
>>>
>>>
>>> df["Young"][1]="Shubman"
>>> print(df)
{10: 'ST', 7: 'MS', 8: 'RJ', 'Young': {1: 'Shubman', 2: 'YJ', 3: 'RS', 4: 'AS'}, 99: 'LM'}
>>>
>>>
>>>
>>>
>>> df.pop("Young")
{1: 'Shubman', 2: 'YJ', 3: 'RS', 4: 'AS'}
>>>
>>> print(df)
{10: 'ST', 7: 'MS', 8: 'RJ', 99: 'LM'}
>>>
>>> df["Young"]={10,20,30}
>>> print(df)
{10: 'ST', 7: 'MS', 8: 'RJ', 99: 'LM', 'Young': {10, 20, 30}}
>>>
>>>
>>>
>>> df["young"].add(25)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'young'
>>>
>>>
>>> print(df)
{10: 'ST', 7: 'MS', 8: 'RJ', 99: 'LM', 'Young': {10, 20, 30}}
>>>
>>>
>>> df['Young'].add(40)
>>>
>>> df["Young"].add(50)
>>>
>>> print(df)
{10: 'ST', 7: 'MS', 8: 'RJ', 99: 'LM', 'Young': {40, 10, 50, 20, 30}}
>>>
>>>
>>>
>>> df["run"]=(100,145,354)
>>> print(df)
{10: 'ST', 7: 'MS', 8: 'RJ', 99: 'LM', 'Young': {40, 10, 50, 20, 30}, 'run': (100, 145, 354)}
>>>
>>>
>>> for i in df:
...     print(i,"--->",df.get(i))
...
10 ---> ST
7 ---> MS
8 ---> RJ
99 ---> LM
Young ---> {40, 10, 50, 20, 30}
run ---> (100, 145, 354)
>>>
>>>
>>>
>>>
>>>
>>> df=[21,"Steve",{10:"PYT",20:"JAVA"},(25,45)]
>>> print(df)
[21, 'Steve', {10: 'PYT', 20: 'JAVA'}, (25, 45)]
>>>
>>>
>>> df[2][40]="AWS"
>>> df.insert(-1,{-1,-2,-4})
>>> print(df)
[21, 'Steve', {10: 'PYT', 20: 'JAVA', 40: 'AWS'}, {-4, -1, -2}, (25, 45)]
>>>
>>>
>>> df.pop()
(25, 45)
>>> df.pop(0)
21
>>>
>>>
>>>
>>> l1=["a1","b2","c3"]
>>> l=dict(l1)
>>> print(l)
{'a': '1', 'b': '2', 'c': '3'}
>>>
>>> d1=["1a","2a","3a","4a"]
>>> l=dict(d1)
>>> print(l)
{'1': 'a', '2': 'a', '3': 'a', '4': 'a'}
>>>
>>>
>>> d1=["a4","a3","a2","a1"]
>>> j=dict(d1)
>>>
>>> print(j)
{'a': '1'}"""