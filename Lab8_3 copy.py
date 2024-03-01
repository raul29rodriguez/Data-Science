'''Exercise 3
Create a 2 ×4 Numpy array filled with zeros. Using a nested for loop enter integer grade
values to the elements of the array (assume the first row is Fall Semester and the second row
is Spring Semester). Create a Series using a dictionary. For keys use ’Fall’ and ’Spring’ and for
values use the first and second rows from Numpy array, respectively (use slicing to get the proper
rows). Ask user which semester they wish to plot (e.g., Fall), what linewidth and color they wish
to use (the color should be case insensitive). Add title, xlabel, ylabel to your plot'''
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
gradesSeries = pd.Series({'Fall':grades[0,:],'Spring':grades[1,:]})
print(gradesSeries)
sem=int(input("Enter 0=Fall or 1=Spring: "))
lw=int(input("Enter linewidth: "))
c=input("Enter color: ")
plt.plot(gradesSeries[sem],linewidth=lw,color=c.lower())
if sem==0:
    semName="Fall"
elif sem==1:
    semName="Spring"
plt.xlabel(semName)
plt.ylabel("Grades")
plt.title("Semester Grades")
plt.show()