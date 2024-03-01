'''Exercise 2
Based on Ex. 1, find the Least Squares Regression Line using the Matrix Algebra method.
Verify whether you get the same regression line parameters as in Ex. 1. Plot the data points, after
noise addition, along with the regression line
Note: You can use the transpose(), np.matmul(), and np.linalg.inv() functions to get the transpose,
multiply matrices, and get the inverse of a matrix, respectively'''
import numpy as np
from matplotlib import pyplot as plt
x = np.array([250, 500, 1000, 2000, 3000, 4000] )
y = np.array([50000, 100000, 200000, 400000, 600000, 800000])
randomNumbers = np.random.normal(0.0, 1.0, 6)
noise=randomNumbers*30000
y2=y+noise
n=len(x)
x1=np.ones((n),dtype=int).reshape(n,1)
x2=np.array(x).reshape(n,1)
xArr=np.hstack((x1,x2))
yArr=np.array(y2).reshape(n,1)
xArrT=xArr.transpose()
yArrT=yArr.transpose()
xMul=np.matmul(xArrT,xArr)
xyMul=np.matmul(xArrT,yArr)
xMulInv=np.linalg.inv(xMul)
A=np.matmul(xMulInv,xyMul)
print(A)
b=A[0]
m=A[1]
noisemodel=b+(m*x2)
plt.scatter(x,y2)
plt.scatter(x,y)
plt.plot(x,noisemodel)
plt.plot(x,y)
plt.show()