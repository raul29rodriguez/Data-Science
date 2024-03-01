'''Exercise 3
Perform Polynomial Curve Fitting on the following dataset: (-2, 3), (-1, 5), (0, 1), (1, 4), (2,
10). Print the coefficients and plot the graph of the polynomial function as shown in the Figure
below
Note 1: Do not use any built-in functions such as polyfit() or polyval(). You can use the
functions np.matmul() and np.linalg.inv() to multiply matrices and get the inverse of a matrix,
respectively
Note 2: Your algorithm should be able to work with any dataset not just a dataset of 5 data
points'''
import numpy as np
from matplotlib import pyplot as plt
x=[-2,-1,0,1,2]
y=[3,5,1,4,10]
n=len(x)
xArr=np.ones((n,n),dtype=float)
for row in range(xArr.shape[0]):
    for col in range(xArr.shape[1]):
        if col==0:
            xArr[row][col]=1
        else:
            xArr[row][col]=x[row]**col
xArrInv=np.linalg.inv(xArr)
c=np.matmul(xArrInv,y)
print(c)
plt.scatter(x,y)
plt.plot(x,y)
plt.ylim(-2,12)
plt.xlim(-3,3)
plt.show()