Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
b="Shravani"
type(b)
<class 'str'>
c=34.44
type(c)
<class 'float'>
d=567.34441
type(d)
<class 'float'>
t=(1,2,3,4)
type(t)
<class 'tuple'>
l=[3,5,6]
type(l)
<class 'list'>
bool=True
type(bool)
<class 'bool'>
dict1={1:1}
type(dict)
<class 'type'>
dict1={"a":11}
type(dict1)
<class 'dict'>
byte1="kop""we"
type(byte1)
<class 'str'>
n=None
type(n)
<class 'NoneType'>
byte1=1"kop"
SyntaxError: invalid syntax
byte1=b"kop"
type(byte1)
<class 'bytes'>
x=memoryview(byte1)
type(x)
<class 'memoryview'>
set2={1,2,3}
type(set2)
<class 'set'>
a=30
b=10
print(a+b)
40
print(a-b)
20
print(a*b)
300
print(a/b)
3.0
a%b
0
a//b
3
a**b
590490000000000
x=88
y=37
x>y
True
x<y
False
x==y
False
x<=y
False
x>=y
True
x!=y
True
x===y
SyntaxError: invalid syntax
c=20
d=20
c+=d
c
40
c-=d
c
20
e=30
e*=d
e
600
e/=d
e
30.0
e%=d
e
10.0
c**=d
c
104857600000000000000000000
e//=d
e
0.0
a=45
b=67
c=31
if a>b and b>c:
    print(a)


if a>b and b>c:
    print(a)

    
if a>b or b>c:
    print(a)

    
45
23>11 or 11>21
True
22>11 not:
    
SyntaxError: invalid syntax
l=[1,2,3,4]
l
[1, 2, 3, 4]
l.append(5)
l
[1, 2, 3, 4, 5]
t=(2,3,4)
t
(2, 3, 4)
t.append(5)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    t.append(5)
AttributeError: 'tuple' object has no attribute 'append'
t.insert(22)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    t.insert(22)
AttributeError: 'tuple' object has no attribute 'insert'
l[4]
5
t[2]
4
set1={12,34,56,67}
set1
{56, 34, 67, 12}
set1.append(22)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    set1.append(22)
AttributeError: 'set' object has no attribute 'append'
set1.add(11)
set1
{34, 67, 11, 12, 56}
set1[1]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    set1[1]
TypeError: 'set' object is not subscriptable
dict1={"name":"Shravani","age"=20}
SyntaxError: ':' expected after dictionary key
dict1={"name":"Shravani","age":20}
dict1
{'name': 'Shravani', 'age': 20}
dict1.insert("rollno":124)
SyntaxError: invalid syntax
dict1["name"]
'Shravani'
dict1["rollno"]=124
dict1
{'name': 'Shravani', 'age': 20, 'rollno': 124}
keys
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    keys
NameError: name 'keys' is not defined
print(keys)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    print(keys)
NameError: name 'keys' is not defined
dict1.keys()
dict_keys(['name', 'age', 'rollno'])
dict1.values()
dict_values(['Shravani', 20, 124])
l.insert(3,88)
l
[1, 2, 3, 88, 4, 5]
l.pop()
5
l.remove(2)
l
[1, 3, 88, 4]
l.popitem(2,3)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    l.popitem(2,3)
AttributeError: 'list' object has no attribute 'popitem'
>>> l.extends(12,34,45)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    l.extends(12,34,45)
AttributeError: 'list' object has no attribute 'extends'. Did you mean: 'extend'?
>>> l.extend(12,34,45)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    l.extend(12,34,45)
TypeError: list.extend() takes exactly one argument (3 given)
>>> l.extend(2)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    l.extend(2)
TypeError: 'int' object is not iterable
>>> l2=[23,56,78]
>>> l1=extend(l2)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    l1=extend(l2)
NameError: name 'extend' is not defined
>>> l1.extend(l2)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    l1.extend(l2)
NameError: name 'l1' is not defined. Did you mean: 'l'?
>>> l.extend(l2)
>>> l
[1, 3, 88, 4, 23, 56, 78]
