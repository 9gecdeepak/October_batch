from __future__ import print_function
"""
Write a program to print the pyramid.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
rows=input("Enter the rows :")
for  i in range(1,rows+1):
  for j in  range(i):
      print(i,end="")
  print("\r")

