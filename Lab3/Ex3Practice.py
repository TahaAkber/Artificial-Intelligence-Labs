Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import math

help(math)

math.sqrt(9)
3.0
math.tan(60)
0.3200403893795629

from math import sqrt
sqrt(9)
3.0
import math as maths
maths.sqrt(25)
5.0
from maths import sqrt as squareroot
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    from maths import sqrt as squareroot
ModuleNotFoundError: No module named 'maths'
squareroot(9_
           
SyntaxError: invalid decimal literal
squareroot(9)
           
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    squareroot(9)
NameError: name 'squareroot' is not defined
import time
time.time()
1677508091.200681
time.ctime()
'Mon Feb 27 19:28:14 2023'
current_time = time.ctime()
>>> current_time
'Mon Feb 27 19:28:46 2023'
>>> time.sleep(5)
>>> import glob
>>> glob.glob("file.py")
[]
>>> glob.glob("*.py)
...           
SyntaxError: incomplete input
>>> glob.glob("*.py")
...           
['Examplesoflab1.py', 'help.py']
>>> glob.glob(*)
...           
SyntaxError: incomplete input
>>> glob.glob("*")
...           
['ALL work', 'Examplesoflab1.py', 'Adobe', 'ENGLISH', 'help.py', 'Themes']
>>> import random
>>> random.randint(1,10)
7
>>> random.random()
0.8382285553991092
>>> x = [2,4,6,8,10]
>>> random.shuffle(x)
>>> print(x)
[8, 4, 2, 10, 6]
>>> random.sample()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    random.sample()
TypeError: Random.sample() missing 2 required positional arguments: 'population' and 'k'
>>> random.sample(x,4)
[6, 4, 10, 8]
>>> random.sample(x,2)
[8, 10]
>>> random.sample(x,3)
[2, 4, 8]
