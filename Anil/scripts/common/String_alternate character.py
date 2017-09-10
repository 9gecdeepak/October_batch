# coding=utf-8
"""
Write a program to print alternate characters in a string. Input a string of your own
choice.
"""
str1=raw_input("Enter the String:")
str2=""
for i in range(0,len(str1),2):
    str2=str2+str1[i]
print str2

"""
Input a string Python‟. Write a program to print all the letters except the letter‟y‟.

"""
str2=''
str1=raw_input("Enter the String:")
except_letter=raw_input("exact letter:")
for i in range(0,len(str1)):
    if str1[i] not in except_letter:
        str2=str2+str1[i]
print str2
