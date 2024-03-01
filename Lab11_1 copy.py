'''Exercise 1
Given the dataset: (-5, -10), (-1, -3), (3, 5), (7, 8), (5, 7), (9, 9), find the regression line using
Matrix Algebra Least Squares (slides 323-325). Find the parameters of the line (slope and y-
intercept) and plot the data points along with the regression line
Note 1: You can use the x.transpose() method to transpose a matrix, the np.matmul(x, y)
method to multiply matrices x and y, and the np.linalg.inv(x) to find the inverse of a matrix
Note 2: Your algorithm should be able to work with any dataset not just a dataset of 5 data
points'''
import numpy as np
from matplotlib import pyplot as plt
x = [-5, -1, 3, 7, 5, 9] 
y = [-10, -3, 5, 8, 7, 9]
n=len(x)
x1=np.ones((n),dtype=int).reshape(n,1)
x2=np.array(x).reshape(n,1)
xArr=np.hstack((x1,x2))
yArr=np.array(y).reshape(n,1)
xArrT=xArr.transpose()
yArrT=yArr.transpose()
xMul=np.matmul(xArrT,xArr)
xyMul=np.matmul(xArrT,yArr)
xMulInv=np.linalg.inv(xMul)
A=np.matmul(xMulInv,xyMul)
print(A)
b=A[0]
m=A[1]
Ymodel=b+(m*x2)
plt.scatter(x2,yArr)
plt.plot(x2,Ymodel,color='r')
plt.title("Least Squares Regression Line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()