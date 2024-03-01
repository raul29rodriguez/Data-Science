from functools import reduce
myList=[2,3,-1,4,8,9]
print(reduce(lambda a,b: a if a<b else b,myList))