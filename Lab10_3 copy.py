'''Exercise 3
Given the following two lists: x = [1, 2, 3, 4, 5] and y = [1, 2, 4, 4, 6] create a scatter plot of the
data as well as the best-fit line using the equation from slide 323, see Figure in the next page
Note 1: First, create two numpy arrays out of the two lists. You can use the x.transpose()
method to transpose a matrix, the np.matmul(x, y) method to multiply matrices x and y, and the
np.linalg.inv(x) to inverse a matrix
Note 2: Equation from slide 323 should yield the y-intercept, b, and the slope, m, of the line.
Plot the best-fit line using the equation of the line: y = mx + b. See the last 5 lines of code from
slide 328 on how to plot the line given the equation of the line
Note 3: Your algorithm should be able to work for any number of data points not just for 5'''
import numpy as np
from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5] 
y = [1, 2, 4, 4, 6]
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