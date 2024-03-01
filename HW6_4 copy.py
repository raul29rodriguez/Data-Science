'''Exercise 4
Using the original 2 ×4 Numpy array from Ex. 3 filled with Fall and Spring grades, find the
the min, max, mean, and standard deviation of each semester, using slicing, and by calling the
respective functions: min(), max(), mean(), std()'''
from statistics import fmean
import numpy as np
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
fall=grades[0,:]
spring=grades[1:]
print(fall)
print(spring)
fMin=np.min(fall)
fMax=np.max(fall)
fMean=np.mean(fall)
fStd=np.std(fall)
sMin=np.min(spring)
sMax=np.max(spring)
sMean=np.mean(spring)
sStd=np.std(spring)
print("Fall min: ",fMin," max: ",fMax," mean: ",fMean," std: ",fStd)
print("Spring min: ",sMin," max: ",sMax," mean: ",sMean," std: ",sStd)