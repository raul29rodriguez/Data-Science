'''Exercise 2
Based on the dataset from Ex. 1, find the regression line using Ordinary Least Squares
(slides 326-328). You can use the mean() built-in function'''
import numpy as np
from matplotlib import pyplot as plt
x = np.array([-5, -1, 3, 7, 5, 9])
y = np.array([-10, -3, 5, 8, 7, 9])
w1=((np.mean(x*y))-(np.mean(x)*np.mean(y)))/((np.mean(x**2))-(np.mean(x)**2))
w0=np.mean(y)-(w1*np.mean(x))
Ymodel=w0+(w1*x)
plt.scatter(x,y)
plt.plot(x,Ymodel)
plt.title("Ordinary Least Sauares")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
plt.show()