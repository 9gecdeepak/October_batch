'''
Write a program to count the number of vowels.
'''
count=0
a=raw_input("enter the string find out count of vowels:")
for i in range(0,len(a)):
    if a[i] in 'aeiouAEIOU':
        count=count+1
print count