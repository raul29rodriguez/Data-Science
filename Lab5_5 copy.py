'''Exercise 5
Similarly to Ex. 4, and using the same functions as above, find the minimum integer in the
list without using the built-in min() function'''
from functools import reduce
li=[10, 'Hi', 20, 'Hello', 30, 'World', 40]
print(reduce(lambda x,y:x if x<y else y ,filter(lambda x:type(x)==int,li)))