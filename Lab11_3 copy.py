'''Exercise 3
Based on the dataset from Ex. 1, find the regression line using the built-in linregress()
method (slides 331-334). Plot the data points along with the regression line and print: slope,
y-intercept, r (correlation coefficient), p-value, standard error'''
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
x = np.array([-5, -1, 3, 7, 5, 9])
y = np.array([-10, -3, 5, 8, 7, 9])
slope,intercept,r,p,std_err=stats.linregress(x,y)
print('Slope: ',slope,'y-intercept: ',intercept,'Correlation(r): ',r,'p-value: ',p,'Standard Error: ',std_err)
mymodel=(slope*x)+intercept
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.title("Linregress")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()