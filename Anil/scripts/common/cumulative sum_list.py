"""
Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the its element is the sum of the first i+1 elements from the
original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
"""
a=[1,2,4,56,12,4]
b=[]
for i in range(0,len(a)):
    b.append(sum(a[0:i+1]))
print b
"""
Write a function to find product of the element of a list.
"""
a=[1,2,3,5,6,77]
product=1
for i in a:
    product=product*i
print product