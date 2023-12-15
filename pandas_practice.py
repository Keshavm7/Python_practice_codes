import numpy as np
import pandas as pd
a=pd.Series()

Warning (from warnings module):
  File "<pyshell#2>", line 1
FutureWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
print(a)
Series([], dtype: float64)
s=pd.Series([10,20,30,40],dtype=float64)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s=pd.Series([10,20,30,40],dtype=float64)
NameError: name 'float64' is not defined. Did you mean: 'float'?
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
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexes\base.py", line 3802, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 165, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 2263, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 2273, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(s[0])
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 981, in __getitem__
    return self._get_value(key)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 1089, in _get_value
    loc = self.index.get_loc(label)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexes\base.py", line 3804, in get_loc
    raise KeyError(key) from err
KeyError: 0
print(s[10])
Maths
print(s[10,20])
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(s[10,20])
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 1007, in __getitem__
    return self._get_with(key)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 1022, in _get_with
    return self._get_values_tuple(key)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 1060, in _get_values_tuple
    raise KeyError("key of type tuple not found and not a MultiIndex")
KeyError: 'key of type tuple not found and not a MultiIndex'
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
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexes\base.py", line 3802, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 146, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index_class_helper.pxi", line 49, in pandas._libs.index.Int64Engine._check_type
KeyError: (10, 20)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 1105, in __setitem__
    self._set_with_engine(key, value)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 1175, in _set_with_engine
    loc = self.index.get_loc(key)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexes\base.py", line 3804, in get_loc
    raise KeyError(key) from err
KeyError: (10, 20)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s[10,20]="Economy","Zoology"
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\series.py", line 1127, in __setitem__
    self.loc[key] = value
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexing.py", line 814, in __setitem__
    indexer = self._get_setitem_indexer(key)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexing.py", line 703, in _get_setitem_indexer
    return self._convert_to_indexer(key, axis=0)
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python311\Lib\site-packages\pandas\core\indexing.py", line 1359, in _convert_to_indexer
    raise IndexingError("Too many indexers")
pandas.errors.IndexingError: Too many indexers



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
