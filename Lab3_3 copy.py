'''Exercise 3
Given the following tuple, tu1 = (9, 3, 0, -4, 8, 7, 10, -1, 5) create your own count and index
functions where count counts the elements passed as argument and index return the first index
of the parameter passed. Your algorithm should work for any tuple irrespective of its size'''

def countFunctionElements(tu1):
    count = len(tu1)
    print("number of elements is",count)

def indexFunction(tu1):
    return tu1[0]

tu1 = (9, 3, 0, -4, 8, 7, 10, -1, 5)
countFunctionElements(tu1)
firstIndex=indexFunction(tu1)
print("element in first index is",firstIndex)