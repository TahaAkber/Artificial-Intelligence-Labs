Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
1+1
2
2*3
6
1==0
False
not(1==0)
True
(2==2) and (2==3)
False
(2==2) or (2==3)
True
#Type "help", "copyright", "credits" or "license()" for more information.
#strings
'artificial'+'intelligence'
'artificialintelligence'
'artificial'.upper()
'ARTIFICIAL'
'HELP'.lower()
'help'
len('help')
4
s = "helloworld"
print(s)
helloworld
s.upper()
'HELLOWORLD'
len(s.upper())
10
num = 8.0
num+=25
print(num)
33.0

#list
fruits = ['apple','orange','pear','banana']
fruits[0]
'apple'
other_fruits=['kiwi','strawberry']
fruits+other_fruits
['apple', 'orange', 'pear', 'banana', 'kiwi', 'strawberry']
fruits[-2]
'pear'
fruits.pop()
'banana'
fruits.append["cake"]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    fruits.append["cake"]
TypeError: 'builtin_function_or_method' object is not subscriptable
fruits.append("cake")
fruits
['apple', 'orange', 'pear', 'cake']
fruits[0:2]
['apple', 'orange']
fruits[:3]
['apple', 'orange', 'pear']
fruits[1:]
['orange', 'pear', 'cake']
len(fruits())
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    len(fruits())
TypeError: 'list' object is not callable
len(fruits)
4

#tuples
pair = (3,4)
pair[0]
3
x,y = pair
x
3
y
4

pair[1]
4
#SETS

shapes = ['circle','square','triangle','circle']
setofshapes

{'circle', 'square', 'triangle'}
>>> setofshapes = {'circle','square','triangle'}
>>> set(['circle','square','triangle'])
{'circle', 'square', 'triangle'}
>>> setofshapes.add("polygon")

{'circle', 'square', 'polygon', 'triangle'}
>>> 'circle' in setofshapes
True
>>> 'rhombus' in setofshapes
False
>>> 
>>> #dictionary
>>> studentsid = {'knuth':42.0,'turing':56.0,'nash':92.0}
>>> 56.0
56.0
>>> studentsid['turing']
56.0
>>> studentsid['nash']="ninetytwo"
>>> print(studentsid)
{'knuth': 42.0, 'turing': 56.0, 'nash': 'ninetytwo'}
>>> studentsid.keys()
dict_keys(['knuth', 'turing', 'nash'])
>>> studentsid.values()
dict_values([42.0, 56.0, 'ninetytwo'])
>>> studentsid.items()
dict_items([('knuth', 42.0), ('turing', 56.0), ('nash', 'ninetytwo')])
>>> len(studentsid)
3
