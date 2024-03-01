'''Exercise 3
Similarly to Ex. 2, use a list comprehension in lieu of map, filter, and lambda, that is, use
a loop and the statement in the Note above inside a list comprehension to produce the same
output. Your code (with the exception of list definition) should be a one-line code'''
li=[10, 'Hi', 20, 'Hello', 30, 'World', 40]
print(list(x*2 for  x in li if type(x)==int))