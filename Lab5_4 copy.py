'''Exercise 4
Given the list from Ex. 2, use reduce, lambda, and filter to sum the integers in the list. Use a
single line of code (with the exception of list definition and the reduce() import)'''
from functools import reduce
li=[10, 'Hi', 20, 'Hello', 30, 'World', 40]
print(reduce(lambda x,y:x+y ,filter(lambda x:type(x)==int,li)))