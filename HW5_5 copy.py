'''Exercise 5
Similarly to Ex. 4, use a filter() along with a lambda (instead of function int_dataTypes()) to
print only the string elements of the list'''
li = [9, "Robot", 3.14, 8, "Vision"]
li = list(filter(lambda x: type(x)==str,li))
print(li)