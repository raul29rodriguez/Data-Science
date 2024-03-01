'''Exercise 1
Create a Numpy array with values from −1 to +10 and a step of 0.1. Plot the cos trigonometric
function, using the np.cos() built-in function'''
from matplotlib import pyplot as plt
import numpy as np
x=np.arange(-1,10,.1)
y=np.cos(x)
plt.plot(x,y)
plt.show()