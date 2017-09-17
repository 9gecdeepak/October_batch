# coding=utf-8
'''
Consider the dictionary mentioned below:
dic={‘a’:’act’,’b’:’battle’,’c’:’cart’,’d’:’diction’}
Write a program to print values of dic in different lines.

'''
from  __future__ import print_function
dic={"a":"act","b":"battle","c":"cart","d":"diction"}
for key in dic:
    print(key,"-----",dic[key],end="\n")

