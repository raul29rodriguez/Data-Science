'''Exercise 1
Create two tuples containing 3 numbers each. Using a map and a lambda, add the respective
elements of the tuples and print the result'''
t1 = (2,3,4)
t2 = (5,6,7)

numAdd = map(lambda x,y: x+y,t1,t2)
print(tuple(numAdd))