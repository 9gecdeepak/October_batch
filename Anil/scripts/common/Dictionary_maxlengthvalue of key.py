#!/usr/bin/env/python
'''
Consider the following,
animals = { 'a':['art'], 'b': ['balloon'], 'c': ['coat'],’d’=[’den’,’dog’,’deer’]}
write a function to find the key that has maximum values Ex:maxani(animals) output is ‘d’.

'''

animals = { 'a': ['art'], 'b': ['balloon'], 'c': ['coat'], 'd': ['den','dog','deer']}

max_value=None
result=None
for key,item in animals.items():
    if len(animals[key])>=max_value:
        result=key
        max_value=len(animals[key])
print "The max_length of key is {} and{} ".format(result,max_value)