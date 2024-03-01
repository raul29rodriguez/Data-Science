'''Exercise 1
Given the following house square feet: 250, 500, 1000, 2000, 3000, 4000 and the following house
prices: 50000, 100000, 200000, 400000, 600000, 800000. Create noise derived from a standard nor-
mal (Gaussian) distribution function (i.e., one with 0 mean and 1 standard deviation). Multiply
the noise derived by 30000 and then add it to the dependent variable. Use Ordinary Least
Squares to find the regression line parameters, estimate the SSE (Sum of Squared Error), and
find the Correlation Coefficient. Plot the data points with and without noise, along with the
regression lines with and without noise, and predict house prices for the following square feet:
200, 1250, 2710, 5100
Note 1: The following line of code produces 6 numbers from a normal distribution with 0
mean and 1 standard deviation: randomNumbers = np.random.normal(0.0, 1.0, 6)
Note 2: Declare your arrays as: np.float64() instead of np.array or use e.g., np.array([250.]) in
at least one element so as to be treated as a float array and multiplying it with an int array will
also result in a float array
Note 3: Do not use any built-in functions, apart from np.mean(), to estimate the: regression
line, SSE, correlation coefficient; you can use them, though, for verification with your own results'''
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
x = np.float64([250, 500, 1000, 2000, 3000, 4000] )
y = np.float64([50000, 100000, 200000, 400000, 600000, 800000])
randomNumbers = np.random.normal(0.0, 1.0, 6)
noise=randomNumbers*30000
y2=y+noise
#w0=y-intercept, w1=slope
w1=((np.mean(x*y2))-(np.mean(x)*np.mean(y2)))/((np.mean(x**2))-(np.mean(x)**2))
w0=np.mean(y2)-(w1*np.mean(x))
noisemodel=w0+(w1*x)
SSE=sum((noisemodel-y2)**2)
r=(sum((x-np.mean(x))*(y2-np.mean(y2))))/((sum((x-np.mean(x))**2))*(sum((y-np.mean(y))**2)))**0.5
print(SSE)
print(r)
p=np.float64([200,1250,2710,5100])
prediction=w0+(w1*p)
print("Predection price is",prediction)
plt.scatter(x,y2)
plt.scatter(x,y)
plt.plot(x,noisemodel)
plt.plot(x,y)
plt.show()