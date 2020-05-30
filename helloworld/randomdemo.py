# coding: utf-8

import random

list1 = [1, 2, 3, 4]
print random.shuffle(list1)
print list1  # [3, 1, 2, 4]
random.shuffle(list1)
print list1  # [3, 4, 1, 2]
