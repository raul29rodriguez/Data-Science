'''Exercise 4
Using the original 2 ×4 Numpy array from Ex. 3 filled with Fall and Spring integer grades,
first flatten it to 1D array using deep copy. Second, create a Panda Series that consists of the
elements of the 1D array. Third, print Series and produce descriptive statistics of Series by calling
the respective built-in method'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
grades = np.zeros((2,4), dtype=int)
arrShape= grades.shape
rows=arrShape[0]
col=arrShape[1]
for r in range(rows):
    for c in range(col):
        if r ==0:
            grades[r][c]= int(input("Enter fall grade: "))
        else:
            grades[r][c]= int(input("Enter spring grade: "))
grades=grades.flatten()
print(grades)
grades=pd.Series(grades)
print(grades)
print(grades.describe())