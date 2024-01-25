# Sequence category datatype


""">>> s="Python"
>>> print(s,type(s))
Python <class 'str'>
>>>  s="HYD10"
  File "<stdin>", line 1
    s="HYD10"
IndentationError: unexpected indent
>>> s="HYD10"
>>> print(s,type(s))
HYD10 <class 'str'>
>>>
>>>
>>> d='ground'
>>> print(d)
ground
>>>
>>> s="Python"
>>> print(s,type(s))
Python <class 'str'>
>>>
>>> d="""FIRE"""
>>> print(d,type(d),id(d))
FIRE <class 'str'> 2238745017200
>>>
>>>
>>> d='''PYTHON'''
>>> print(d,type(d))
PYTHON <class 'str'>
>>>
>>>
>>> d="""This is Python world
... welcome to this new world
... lets code"""
>>> print(d)
This is Python world
welcome to this new world
lets code
>>>
>>> type(d)
<class 'str'>
>>>
>>>
>>> d="This is pyhton world"
>>> print(d)
This is pyhton world
>>>
>>>
>>>
>>> d="Python3.12"
>>> d[0]
'P'
>>> d[1]
'y'
>>> for i in range(0,len(d)+1):
... print(d[i])
  File "<stdin>", line 2
    print(d[i])
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in range(0,len(d)+1):
...     print(d[i])
...
P
y
t
h
o
n
3
.
1
2
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: string index out of range
>>> for i in range(0,len(d)+1):
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>>
>>>
>>>
>>> for i in range(0,len(d)):
...     print(d[i])
...
P
y
t
h
o
n
3
.
1
2
>>>
>>>
>>> d="This is Python world"
>>> d[10]
't'
>>> d[-10]
't'
>>> d[5]
'i'
>>> d[4]
' '
>>> d.split()
['This', 'is', 'Python', 'world']
>>> "".join(d.split())
'ThisisPythonworld'
>>>
>>>
>>>
>>> d='CRICKET IS POPULAR SPORTS IN INDIA'
>>> print(d,type(d))
CRICKET IS POPULAR SPORTS IN INDIA <class 'str'>
>>>
>>> d[::]
'CRICKET IS POPULAR SPORTS IN INDIA'
>>> d[1:]
'RICKET IS POPULAR SPORTS IN INDIA'
>>> d[0:]
'CRICKET IS POPULAR SPORTS IN INDIA'
>>> d[:]
'CRICKET IS POPULAR SPORTS IN INDIA'
>>> d[::-1]
'AIDNI NI STROPS RALUPOP SI TEKCIRC'
>>> d[0:4]
'CRIC'
>>> d[1:-1]
'RICKET IS POPULAR SPORTS IN INDI'
>>> d[1:0]
''
>>> d[0:0]
''
>>> d[2:5]
'ICK'
>>> d[-6:-1]
' INDI'
>>> d[-6:]
' INDIA'
>>> d[-1:-8]
''
>>> d[0:15:2]
'CIKTI OU'
>>> d[-1:-8:-2]
'ADIN'
>>> d[-1:-6:2]
''
>>> d[:len(d)]
'CRICKET IS POPULAR SPORTS IN INDIA'
>>>
>>>
>>>
>>> d[-100:-1]
'CRICKET IS POPULAR SPORTS IN INDI'
>>> d[0:-1]
'CRICKET IS POPULAR SPORTS IN INDI'
>>> d[-2500:]
'CRICKET IS POPULAR SPORTS IN INDIA'
>>> d[0:2500]
'CRICKET IS POPULAR SPORTS IN INDIA'
>>> d[-2500:2500]
'CRICKET IS POPULAR SPORTS IN INDIA'
>>>
>>>
>>> d[0:8:2]
'CIKT'
>>> d[-10:-1:-2]
''
>>> d[-1:-10:-2]
'ADIN '
>>> len(d)
34
>>> d[-1:-34:-2]
'ADIN TOSRLPPS ECR'
>>> d[-1:-34]
''
>>> d[-34:-1]
'CRICKET IS POPULAR SPORTS IN INDI'
>>> d[-1:-20:-1]
'AIDNI NI STROPS RAL'
>>> d[-1:-34:-1]
'AIDNI NI STROPS RALUPOP SI TEKCIR'
>>> d[0:-34:-1]
''
>>> d[::-1]
'AIDNI NI STROPS RALUPOP SI TEKCIRC'
>>> d[::-2]
'ADIN TOSRLPPS ECR'
>>>
>>>
>>>
>>>
>>> s=12.5
>>> print(s)
12.5
>>> d=int(s)
>>> print(d)
12
>>>
>>> s=True
>>> print(s)
True
>>> d=int(s)
>>> print(d)
1
>>>
>>>
>>>
>>> s=False
>>> print(s)
False
>>> print(int(s))
0
>>>
>>>
>>> s=2+3j
>>> print(int(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> s='2+3j'
>>> print(int(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2+3j'
>>>
>>>
>>> s='10'
>>> print(int(s))
10
>>>
>>>
>>> s=10.25
>>> print(int(s))
10
>>>
>>>
>>> s='25.00'
>>> print(int(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '25.00'
>>>
>>>
>>> s='True'
>>> print(int(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'True'
>>>
>>>
>>> s='2+3j'
>>> print(int(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2+3j'
>>>
>>>
>>>
>>> s="UTU"
>>> print(int(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'UTU'
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> s=float(int/bool/complex/str)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'type' and 'type'
>>>
>>>
>>>
>>>
>>> s=25
>>> prnt(float(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'prnt' is not defined. Did you mean: 'print'?
>>> print(int(s))
25
>>>
>>>
>>>
>>> print(float(s))
25.0
>>>
>>>
>>>
>>>
>>> s=True
>>> print(float(s))
1.0
>>>
>>>
>>>
>>> s=False
>>> print(float(s))
0.0
>>>
>>>
>>>
>>> s=2+3j
>>> print(float(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string or a real number, not 'complex'
>>>
>>>
>>>
>>>
>>>
>>> s=
  File "<stdin>", line 1
    s=
      ^
SyntaxError: invalid syntax
>>>
>>>
>>>
>>>
>>>
>>>
>>> s="25"
>>> print(float(s))
25.0
>>>
>>>
>>> s="25.35"
>>>
>>> print(float(s))
25.35
>>>
>>>
>>> s="35.65.54"
>>>
>>> print(float(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '35.65.54'
>>>
>>>
>>>
>>> s="True"
>>> print(s)
True
>>>
>>>
>>> print(float(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'True'
>>>
>>>
>>>
>>>
>>> s='False'
>>> print(float(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'False'
>>>
>>>
>>>
>>>
>>> s=False
>>> print(float(s))
0.0
>>>
>>>
>>>
>>> s=5+9j
>>>
>>> print(str(float(s)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string or a real number, not 'complex'
>>>
>>>
>>>
>>> print(float(str(s)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '(5+9j)'
>>>
>>>
>>>
>>> s='Python'
>>> print(float(s))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'Python'
>>>
>>>
>>>
>>>
>>> a=True
>>> print(int(a))
1
>>>
>>>
>>> a=False
>>> print(int(a))
0
>>>
>>>
>>> a=100
>>> print(bool(a))
True
>>>
>>>
>>> a
100
>>> a=258455
>>> print(bool(a))
True
>>>
>>>
>>> a=-3654855
>>> print(bool(a))
True
>>>
>>>
>>>
>>> a=0
>>> print(float(a))
0.0
>>>
>>>
>>>
>>> a=125.4
>>> print(bool(a))
True
>>>
>>>
>>> a=0.0
>>> print(bool(a))
False
>>>
>>>
>>> a=0.0000001
>>> print(bool(a))
True
>>>
>>>
>>>
>>> a=2+9k
  File "<stdin>", line 1
    a=2+9k
        ^
SyntaxError: invalid decimal literal
>>> 2+5j
(2+5j)
>>> a=2+5j
>>> print(bool(a))
True
>>>
>>>
>>> a=2-9j
>>> print(bool(a))
True
>>>
>>>
>>>
>>> a=0+0j
>>> print(bool(a))
False
>>>
>>> a=0+1j
>>> print(bool(a))
True
>>>
>>>
>>> a="254"
>>> print(bool(a))
True
>>>
>>>
>>>
>>> a="25.54"
>>> print(bool(a))
True
>>>
>>>
>>>
>>>
>>> a="
  File "<stdin>", line 1
    a="
      ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a=''
>>> print(bool(a))
False
>>>
>>>
>>> a="False"
>>> print(a)
False
>>>
>>>
>>>
>>> print(bool(a))
True
>>>
>>>
>>>
>>> a="True"
>>> print(bool(a))
True
>>>
>>> a="False"
>>> print(bool(a))
True
>>>
>>>
>>> a="254"
>>> print(bool(a))
True
>>>
>>>
>>>
>>> a="2+5j"
>>>
>>> print(bool(a))
True
>>>
>>>
>>>
>>>
>>> a=100
>>> print(complex(a))
(100+0j)
>>>
>>>
>>>
>>> a=125.4
>>> print(complex(a))
(125.4+0j)
>>>
>>>
>>> a=True
>>> print(a,type(a))
True <class 'bool'>
>>>
>>>
>>> print(complex(a))
(1+0j)
>>>
>>>
>>>
>>> a=false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> a=False
>>>
>>> print(complex(a))
0j
>>>
>>>
>>> a="10"
>>> print(complex(a))
(10+0j)
>>>
>>>
>>> a="25.45"
>>> print(complex(a))
(25.45+0j)
>>>
>>>
>>>
>>> a="True"
>>> print(complex(a))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: complex() arg is a malformed string
>>>
>>>
>>>
>>> a="Python"
>>>
>>> print(complex(a))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: complex() arg is a malformed string
>>>
>>>
>>>
>>> a="2+5j"
>>> print(complex(a))
(2+5j)
>>>
>>>
>>> a=100
>>> print(str(a))
100
>>>
>>>
>>> a=25.45
>>> print(str(a))
25.45
>>>
>>>
>>> a=python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python' is not defined
>>> a=2+5j
>>> print(str(a))
(2+5j)
>>>
>>>
>>>
>>> a="25.4"
>>> print(complex(a))
(25.4+0j)
>>>
>>> lst=[10,25,35,4,255,154,45,0]
>>> print(lst,type(lst))
[10, 25, 35, 4, 255, 154, 45, 0] <class 'list'>
>>>
>>> s=bytes(lst)
>>> print(s)
b'\n\x19#\x04\xff\x9a-\x00'
>>>
>>> for i in s:
...     print(i)
...
10
25
35
4
255
154
45
0
>>>
>>> s[2]
35
>>> s[-6:-1]
b'#\x04\xff\x9a-'
>>> s[2:5]
b'#\x04\xff'
>>> for i in s[-6:-1]:
...     print(i)
...
35
4
255
154
45
>>>
>>> for val in s[-1:-7:-2]
  File "<stdin>", line 1
    for val in s[-1:-7:-2]
                          ^
SyntaxError: expected ':'
>>> s[2]=25
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
>>>
>>>
>>>
>>>
>>> s=[125,25,0,65,78,95,65,67,34]
>>> print(s,type(s))
[125, 25, 0, 65, 78, 95, 65, 67, 34] <class 'list'>
>>>
>>>
>>>
>>> s[]2
  File "<stdin>", line 1
    s[]2
      ^
SyntaxError: invalid syntax
>>> s[2]
0
>>>
>>> s[2:5]
[0, 65, 78]
>>> l=[24]
>>>
>>>
>>> l=[24,34,37,97,67,65,34,14]
>>> print(l,type(l))
[24, 34, 37, 97, 67, 65, 34, 14] <class 'list'>
>>>
>>> lst=bytearray(l)
>>> print(lst)
bytearray(b'\x18"%aCA"\x0e')
>>>
>>> lst[2]
37
>>> lst[2:5]
bytearray(b'%aC')
>>>
>>>
>>> for i in lst[2:8]:
...     print(i)
...
37
97
67
65
34
14
>>> lst[2]=255
>>> print(lst)
bytearray(b'\x18"\xffaCA"\x0e')
>>> for val in lst:
...     print(val)
...
24
34
255
97
67
65
34
14
>>>
>>>
>>>
>>>
>>>
>>> r=range(10)
>>>
>>>
>>> print(r)
range(0, 10)
>>> for val in r:
...     print(r)
... print(val)
  File "<stdin>", line 3
    print(val)
    ^^^^^
SyntaxError: invalid syntax
>>>
>>> for val in r:
...     print(val)
...
0
1
2
3
4
5
6
7
8
9
>>>
>>> l=range(101)
>>> for i in l:
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
>>>
>>>
>>> l[50:]
range(50, 101)
>>>
>>> for val in l[50:]:
...     print(val)
...
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
>>>
>>>
>>>
>>>
>>>
>>> r=range(15,26)
>>> for i in r:
...     print(i)
...
15
16
17
18
19
20
21
22
23
24
25
>>> for i in r:
...     print(i,end="-->")
...
15-->16-->17-->18-->19-->20-->21-->22-->23-->24-->25-->>>>
>>>
>>>
>>> r=range(-10)
>>> for i in r:
...     print(i)
...
>>>
>>>
>>>
>>>
>>> r=range(100,-100,-1)
>>> for i in r:
...     print(i)
...
100
99
98
97
96
95
94
93
92
91
90
89
88
87
86
85
84
83
82
81
80
79
78
77
76
75
74
73
72
71
70
69
68
67
66
65
64
63
62
61
60
59
58
57
56
55
54
53
52
51
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
-11
-12
-13
-14
-15
-16
-17
-18
-19
-20
-21
-22
-23
-24
-25
-26
-27
-28
-29
-30
-31
-32
-33
-34
-35
-36
-37
-38
-39
-40
-41
-42
-43
-44
-45
-46
-47
-48
-49
-50
-51
-52
-53
-54
-55
-56
-57
-58
-59
-60
-61
-62
-63
-64
-65
-66
-67
-68
-69
-70
-71
-72
-73
-74
-75
-76
-77
-78
-79
-80
-81
-82
-83
-84
-85
-86
-87
-88
-89
-90
-91
-92
-93
-94
-95
-96
-97
-98
-99
>>> for i in r:
...     print(i,end=" ")
...
100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25 -26 -27 -28 -29 -30 -31 -32 -33 -34 -35 -36 -37 -38 -39 -40 -41 -42 -43 -44 -45 -46 -47 -48 -49 -50 -51 -52 -53 -54 -55 -56 -57 -58 -59 -60 -61 -62 -63 -64 -65 -66 -67 -68 -69 -70 -71 -72 -73 -74 -75 -76 -77 -78 -79 -80 -81 -82 -83 -84 -85 -86 -87 -88 -89 -90 -91 -92 -93 -94 -95 -96 -97 -98 -99 >>>
>>>
>>>
>>> r=range(0,100,2)
>>> for i in r:
...     print(i,end="")
...
02468101214161820222426283032343638404244464850525456586062646668707274767880828486889092949698>>>
>>>
>>> for i in r:
... )
  File "<stdin>", line 2
    )
    ^
SyntaxError: unmatched ')'
>>>
>>>
>>> for i in r[::-1]:
...     print(i)
...
98
96
94
92
90
88
86
84
82
80
78
76
74
72
70
68
66
64
62
60
58
56
54
52
50
48
46
44
42
40
38
36
34
32
30
28
26
24
22
20
18
16
14
12
10
8

"""