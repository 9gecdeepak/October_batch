'''
Write a program to find the sum of all items in a list.
'''
a=[1,2,4,5,7,12]
sum1=0
for i in range(0,len(a)):
    sum1=sum1+a[i]
print sum1

#2rd way

print sum(a)

#3rd way

sum2=0
for i in a:
    sum2=sum2+i
print sum2