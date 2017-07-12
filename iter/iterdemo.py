__author__ = 'xudazhou'

str1 = "abc"
i1 = iter(str1)

"""
Traceback (most recent call last):
  File "D:/_python/TestPython27/iter/iterdemo.py", line 6, in <module>
    print(i1.next())
StopIteration
a
b
c
"""
while True:
    print(i1.next())


