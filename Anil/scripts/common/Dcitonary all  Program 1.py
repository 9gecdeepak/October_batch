# coding=utf-8
# Write a program to find all the subsets of the set x={1,2,3,4}
from __future__ import print_function
import itertools

x = {1, 2, 3, 4}
for key in range(len(x)):
    for j in itertools.combinations(x, key):
        print(j)

# Consider a tuple, x=(‘s’,’y’,’e’) and a dictionary, d={‘a’:’act’,’b’:’battle’,’y’:’cart’,’s’:’diction’}.
# Write a program to find number of tuple values that are keys in dictionary.
d = {'a': 'act', 'b': 'battle', 'y': 'cart', 's': 'diction'}
x = {"s", "y", "e"}
count = 0
for p in x:
    if p in d:
        print("present key {}".format(p))
        count = count + 1
print("total count is {}".format(count))

#Write a program to find number of keys in a dictionary.
d = {'a': 'act', 'b': 'battle', 'y': 'cart', 's': 'diction'}
count=0
for k in d:
    count=count+1
    print("keys is:{}".format(k))
print ("total keysis {}".format(count))

#Write a program to find a value in a given Dictionary:
dict={"a":"a","b":"b","c":"c","d":"d"}
p=raw_input("inter the characters is [a-z]or {A-Z]:").lower()

if p in dict.values():
    print("value is present")
else:
    print ("value is not present")