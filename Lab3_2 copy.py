'''Exercise 2
Given the following list, li = [9, 3, 0, -4, 8, 7, 10, -1, 5], ask user to give you the following three
indices, start, stop, step. Print list based on the indices user has given'''
li = [9, 3, 0, -4, 8, 7, 10, -1, 5]
start = int(input("Enter start of slice: "))
stop = int(input("Enter where to stop slice: "))
step = int(input("Enter step of slice: "))
print(li[start:stop:step])