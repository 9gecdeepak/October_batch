"""
Program to check whether the string is a palindrome or not
"""

str1=raw_input("enter the string:")
string2=" "
for i in range(len(str1)-1,-1,-1):
    string2=string2+str1[i]


if str1 == string2.lstrip():
    print "the string is palindrome:",str1
else:
    print "the both {},{} are not palindrome".format(str1,string2)
