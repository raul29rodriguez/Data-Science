'''Exercise 2
Given the following list: li=[10, ’Hi’, 20, ’Hello’, 30, ’World’, 40] and, using only map, filter,
and lambda, multiply the integers in the list by 2. Your code (with the exception of list definition
above) should be a one-line code
Note: You can use the following statement to check if an element is an integer: type(x)==int'''
li=[10, 'Hi', 20, 'Hello', 30, 'World', 40]
print(list(map(lambda x: x*2, filter(lambda x: type(x)==int ,li))))