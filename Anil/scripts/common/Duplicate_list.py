"""
Write a function to find all duplicates in the list.
"""
# 1st way
a=[1,2,2,4,3,1,6,"pavan","hareesh","pavan"]

for i in a:
    if a.count(i)>1:
        a.remove(i)
print a

# 2rd way
for i in range(0,len(a)):
    if a.count(a[i])>1:
        a.pop(i)
print a

# 3rd way
b=[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
print b