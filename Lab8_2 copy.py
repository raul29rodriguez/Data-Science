'''Exercise 2
Similarly to Ex.1, create a Numpy array with 120 elements and values that range from −1 to
+10. Plot the tan trigonometric function using the np.tan() built-in function'''
from matplotlib import pyplot as plt
import numpy as np
x=np.linspace(-1, 10, num=120)
y=np.tan(x)
plt.plot(x,y)
plt.show()