"""
Write a function group of list (list, size) that takes a list and splits into smaller list
of given size.
"""

a=[1, 2, 3, 4, 5, 6, 7, 8, 9,11]
b=[]
size=input("size of list:")
for i in range(0,len(a),size):
     b.append(a[i:i+size])
print b

