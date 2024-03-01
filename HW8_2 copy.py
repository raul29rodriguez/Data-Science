'''Exercise 2
Given the DataFrame from slide 217, write your own describe function that produces the
same 8 statistical results, for each one of the columns, that the built-in describe() function does.
Slide 264 shows how to get the number of rows and columns of a DataFrame
Note 1: Use the sample standard deviation formula (that is, the denominator is: N-1)
Note 2: Your algorithm should work for any number of columns not just for 5
Note 3: You can use the np.percentile() for the 25% and 75% percentile as well as the sort()
built-in functions
Note 4: For a review of quartiles refer to:
https://www.mathsisfun.com/data/quartiles.html'''
import pandas as pd
import numpy as np
from statistics import stdev
def myDescribe(li):
    sumVar = 0
    minValue = li[0]
    maxValue = li[0]
    for c in range(len(li)):
        sumVar = sumVar + li[c]
        if minValue > li[c]:
            minValue = li[c]
        if maxValue < li[c]:
            maxValue = li[c]
    average = sumVar / len(li)
    count = len(li)
    quartile1=np.percentile(sorted(li),25)
    quartile2=np.percentile(sorted(li),50)
    quartile3=np.percentile(sorted(li),75)
    stDev=stdev(li)
    print(f'count: {count}\t mean: {round(average)}\t min: {minValue}\t max: {maxValue}\t 25%: {quartile1}\t 50%: {quartile2}\t 75%: {quartile3}\t stdev: {round(stDev)}')
grades_dict = {'Wally' : [87, 96, 70], 'Eva' : [100, 87, 90], 
              'Sam' : [94, 77, 90], 'Katie' : [100, 81, 82], 
              'Bob' : [83, 65, 85]}
grades = pd.DataFrame(grades_dict) #customize indices
grades.index = ['Test 1', 'Test 2', 'Test 3']
print(grades)
rows = len(grades)
columns = len(grades.columns)
for c in range(columns):
    col = list(grades.iloc[:, c])
    myDescribe(col)