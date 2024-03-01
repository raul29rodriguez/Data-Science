'''Exercise 3
Create a 2 ×4 Numpy array filled with zeros. Using a nested for loop enter int grade values
to all elements of the array (assume the first row is Fall Semester and the second row is Spring
Semester). Change the shape of the array to 4 ×2. Using slicing, create an array that consists
of the elements of the first column of the reshaped array and a second array that consists of the
elements of the second column of the reshaped array'''
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
print(grades)
grades=grades.reshape(4,2)
print("reshaped array\n",grades)
col1=grades[:,0]
col2=grades[:,1]
print("1st column",col1)
print("2nd column",col2)