# coding=utf-8
'''
Input the string any string. Write a script to split the string at every occurrence of
the  any letter .

'''
str1=raw_input("Enter the String:").lower()
occ_letter=raw_input("Enter any Occurrence Letter:")
str1_split=str1.split(occ_letter)
print str1_split

"""
Input the string “Successor”. Write a script to partition the string at the occurrence
of the letter s
"""
str1=raw_input("Enter the String:").lower()
occ_letter=raw_input("Enter any Occurrence Letter:")
str1_partit=str1.partition(occ_letter)
print str1_partit
"""
Explain the difference between the function split( ) and
partition()
"""
#--------------split--------------
#split return list
#split any occurrence of latter

#------------------partition----------------
# partition return tuple
# partition first occurrence letter split
