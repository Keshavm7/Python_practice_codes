import numpy as np
import pandas as pd
a=pd.Series()

s=pd.Series([10,20,30,40],dtype="float64")
print(s)
0    10.0
1    20.0
2    30.0
3    40.0
dtype: float64
s=pd.Series([10,20,30,40],dtype="int32")
print(s)
0    10
1    20
2    30
3    40
dtype: int32
s=pd.Series([10,20,30,40],dtype="int64")
print(s)
0    10
1    20
2    30
3    40
dtype: int64
a=np.array([100,200,300,400])
s=pd.Series(a)
print(s)
0    100
1    200
2    300
3    400
dtype: int32
lst=[10,"GMR","PYTHON","NTUIT"]
p=pd.Series(lst)
print(p)
0        10
1       GMR
2    PYTHON
3     NTUIT
dtype: object
p=pd.Series(lst,index=["Roll no.","Name","Subject","College"])
print(p)
Roll no.        10
Name           GMR
Subject     PYTHON
College      NTUIT
dtype: object
s=pd.Series(["Karan","Karishma","Kiran","Kavya","Danish"],index=["100","200","300","400","500"])
print(s)
100       Karan
200    Karishma
300       Kiran
400       Kavya
500      Danish
dtype: object
d={100:"Karan",200:"Karishma",300:"Kiran",400:"Kavya",500:"Danish"}
s=pd.Series(d)
print(s)
100       Karan
200    Karishma
300       Kiran
400       Kavya
500      Danish
dtype: object


c=pd.Series(["Maths","Science","History","Polity","Geography"],[1,2,3,4,5])
print(c)
1        Maths
2      Science
3      History
4       Polity
5    Geography
dtype: object
s=pd.Series([1,2,3,4,5],['a','b','c','d','e'])
print(s)
a    1
b    2
c    3
d    4
e    5
dtype: int64
Print(s[0])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Print(s[0])
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(s[0])
1
print(s[4])
5
print(s[0:4])
a    1
b    2
c    3
d    4
dtype: int64
print(s[::2])
a    1
c    3
e    5
dtype: int64
print(s[1:4:2])
b    2
d    4
dtype: int64
d={10:"Maths",20:"Science",30:"History",40:"Geography",50:"Marathi"}
print(d)
{10: 'Maths', 20: 'Science', 30: 'History', 40: 'Geography', 50: 'Marathi'}
s=pd.Series(d)
print(s)
10        Maths
20      Science
30      History
40    Geography
50      Marathi
dtype: object
print(s[0])

print(s[[10,20]])
10      Maths
20    Science
dtype: object
print(10)
10
print(s[50])
Marathi
s[10]="Polity"
print(s)
10       Polity
20      Science
30      History
40    Geography
50      Marathi
dtype: object
s[10,20]="Economy","Zoology"


l=[10,20,30,40]
print(l)
[10, 20, 30, 40]
df=pd.DataFrame(l)
print(df)
    0
0  10
1  20
2  30
3  40
l=pd.DataFrame([10,20,30,40,50],['King','Queen','Minister','Soldier','Servent'])
print(l)
           0
King      10
Queen     20
Minister  30
Soldier   40
Servent   50


l=pd.DataFrame([10,20,30,40,50],column=['King','Queen','Minister','Soldier','Servent'])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l=pd.DataFrame([10,20,30,40,50],column=['King','Queen','Minister','Soldier','Servent'])
TypeError: DataFrame.__init__() got an unexpected keyword argument 'column'
