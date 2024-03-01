'''Exercise 5
Given the following list: grades = [90, 74, 87, 80], use a lambda expression to compute the
average grade. Your algorithm should compute the average grade regardless of the length of the
list. Use only the sum and len built-in functions'''
grades = [90, 74, 87, 80]
average = lambda args: sum(args)/len(args)
print(average(grades))