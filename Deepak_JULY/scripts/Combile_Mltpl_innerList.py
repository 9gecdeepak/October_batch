"""
Combine multiple inner list to 1 target list

"""
import itertools
a=[[1,2,3],[4,5,6],[12,13,15]]

b = list(itertools.chain.from_iterable(a))
print b
