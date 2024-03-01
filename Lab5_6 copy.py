'''Exercise 6
Given the list from Ex. 2, use map, lambda, and filter to print the string elements of the list
in upper case. You may use the built-in function upper()'''
li=[10, 'Hi', 20, 'Hello', 30, 'World', 40]
print(list(map(lambda x: x.upper(), filter(lambda x: type(x)!=int ,li))))