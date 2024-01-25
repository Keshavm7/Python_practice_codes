# Fundamental Category Data types

 a=10
 print(a)
10
>>> type(a)
<class 'int'>
>>> id(a)
140734865750744
>>> b=10
>>> id(b)
140734865750744
>>> c=10
>>>
>>> id(c)
140734865750744
>>>
>>> a=10
>>> b=20
>>> c=a+b
>>> print(c)
30
>>> print(c,type(c),id(c))
30 <class 'int'> 140734865751384
>>> print(a,b,c)
10 20 30
>>>
>>>
>>> a=ob1101
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ob1101' is not defined
>>> a=ob1101
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ob1101' is not defined
>>> a=0b1101
>>> print(a,type(a))
13 <class 'int'>
>>>
>>>
>>> a=0B1101
>>> print(a,type(a))
13 <class 'int'>
>>>
>>>
>>> a=0b10111
>>> print(a,type(a),id(a))
23 <class 'int'> 140734865751160
>>>
>>>
>>> a=254
>>> print(bin(a))
0b11111110
>>>
>>>
>>> print(bin(25))
0b11001
>>>
>>>
>>> print(bin(1))
0b1
>>>
>>>
>>> print(bin(100))
0b1100100
>>>
>>> a=0o127
>>> print(a)
87
>>> type(a)
<class 'int'>
>>>
>>> a=0o2546
>>> print(a)
1382
>>>
>>>
>>> a=0O1254
>>> print(a)
684
>>>
>>> a=8754
>>> print(oct(a))
0o21062
>>>
>>>
>>> a=987654
>>> print(oct(a))
0o3611006
>>>
>>> b=0x124
>>> print(b,type(b),id(b))
292 <class 'int'> 2542951971696
>>>
>>>
>>> a=0XABF1254
>>> print(a,type()a)
  File "<stdin>", line 1
    print(a,type()a)
                  ^
SyntaxError: invalid syntax
>>> print()a,type(a))
  File "<stdin>", line 1
    print()a,type(a))
           ^
SyntaxError: invalid syntax
>>> print(a,type(a))
180294228 <class 'int'>
>>>
>>>
>>> a=0xFace
>>> print(a)
64206
>>>
>>> a=0xanf
  File "<stdin>", line 1
    a=0xanf
        ^
SyntaxError: invalid hexadecimal literal
>>>
>>>
>>> a=12548
>>> print(hex(a))
0x3104
>>>
>>>
>>> a=01254
  File "<stdin>", line 1
    a=01254
      ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a=25468
>>> print(hex(a))
0x637c
>>>
>>>
>>> a=10
>>> print(bin(a))
0b1010
>>>
>>> print(oct(a))
0o12
>>>
>>> print(hex(a))
0xa
>>>
>>> a=0xF
>>> print(bin(a))
0b1111
>>>
>>>
>>> print(oct(a))
0o17
>>>
>>> print(a)
15
>>>
>>> a=0o1267
>>> print(a)
695
>>>
>>> print(bin(a))
0b1010110111
>>>
>>>
>>> print(hex(a))
0x2b7
>>>
>>>
>>> a=10.0
>>> print(a,type(a))
10.0 <class 'float'>
>>>
>>> b=15.20
>>> print(b,type(b))
15.2 <class 'float'>
>>>
>>> print(id(b))
2542951961968
>>>
>>> a=12.5
>>> b=14.5
>>>
>>> c=a+b
>>> print(c)
27.0
>>>
>>> print(c,type(c))
27.0 <class 'float'>
>>>
>>>
>>> a=10e3
>>> print(a,type(a))
10000.0 <class 'float'>
>>>
>>>
>>>
>>> b=5e-3
>>>
>>> print(b,type(b))
0.005 <class 'float'>
>>>
>>>
>>> c=10e5
>>> print(c,type(c),id(c))
1000000.0 <class 'float'> 2542951957264
>>>
>>>
>>> a=0.00000000000000000000000000035
>>> print(a,type(a))
3.5e-28 <class 'float'>
>>>
>>>
>>> True=10
  File "<stdin>", line 1
    True=10
    ^^^^
SyntaxError: cannot assign to True
>>>
>>>
>>> False=5
  File "<stdin>", line 1
    False=5
    ^^^^^
SyntaxError: cannot assign to False
>>>
>>> a=True
>>> print(a,type(a))
True <class 'bool'>
>>>
>>>
>>> a=true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>>
>>>
>>> a=True
>>> print(int(a),type(a))
1 <class 'bool'>
>>>
>>>
>>> b=False
>>>
>>> print(b)
False
>>>
>>> b=False
>>> print(b,int(b),type(b))
False 0 <class 'bool'>
>>>
>>>
>>>
>>> print(3+True*25)
28
>>>
>>>
>>> print(False*1254)
0
>>>
>>>
>>> print(True+False)
1
>>>
>>> print(True*True)
1
>>>
>>> a=2+3j
>>> print()a
  File "<stdin>", line 1
    print()a
           ^
SyntaxError: invalid syntax
>>>
>>> print(a)
(2+3j)
>>>
>>> print(a.real)
2.0
>>>
>>>
>>> a=-2-3j
>>>
>>> print(a,type(a))
(-2-3j) <class 'complex'>
>>>
>>>
>>>
>>> a=-2+10j
>>>
>>> a.real
-2.0
>>> a.imag
10.0
>>>
>>> print(a,type(a))
(-2+10j) <class 'complex'>
>>>
>>> a=2+5j
>>> b=5+2j
>>> print(a+b)
(7+7j)
>>>
>>> print(a*b)
29j
>>>
>>>