'''Exercise 2
Ask user to enter min, max and step values for the x-axis. Use the np.arange() function with
the three values the user entered in order to create an array named x. For the y array use the
eval() function and ask user to enter an expression (see Notes below), e.g., ’abs(x)’ or ’x**2’. Plot
(x, y) and add label, xlabel, ylabel, title, legend to your plot
Note 1: eval() is a powerful function that can parse a string and convert it into an expression,
that is, eval(expression) where expression = ’x**2’ will raise all x values to the power of 2
Note 2: For more examples with the eval() function you may check the online tutorials on
programiz and geeksforgeeks'''
from matplotlib import pyplot as plt
import numpy as np
min= int(input("Enter minimum: "))
max= int(input("Enter maximum: "))
step= int(input("Enter step: "))
x = np.arange(min,max,step)
y = eval(input("Enter your expression: "))
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x)")
plt.legend()
plt.show()