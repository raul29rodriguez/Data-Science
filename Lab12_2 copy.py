'''Exercise 2
In continuation of Ex. 1, assign the columns weight and mpg into x and y numpy arrays,
respectively. Perform Linear Regression using the Ordinary Least Squares method (you can use
built-in functions, if you wish). Make predictions for the values: 1500 to 5000 with a step of 500,
that is, 8 x values. Plot the data points along with the regression line and the predicted values,
and print: slope, y-intercept, r, using f-strings, on the plot title, as shown in the Figure in the next
page.
Note: You can insert text into the plot using: plt.text(xCoord, yCoord, ’Linear Regression line’)'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
import csv
import math
df=pd.read_csv('auto-mpg.csv')
df=df.replace('?',np.nan)
df=df.dropna()
x=np.array(df['weight'])
y=np.array(df['mpg'])
#w0=y-intercept, w1=slope
w1=((np.mean(x*y))-(np.mean(x)*np.mean(y)))/((np.mean(x**2))-(np.mean(x)**2))
w0=np.mean(y)-(w1*np.mean(x))
r=(sum((x-np.mean(x))*(y-np.mean(y))))/math.sqrt(sum((x-np.mean(x))**2)*sum((y-np.mean(y))**2))
#slope,intercept,r,p,std_err=stats.linregress(x,y)
print(r)
myModel=w0+(w1*x)
p=np.arange(1500,5500,500)
prediction=w0+(w1*p)
print("prediction=",prediction)
#plt.scatter(x,y)
plt.plot(x,myModel)
plt.plot(p,prediction)
plt.title(f'slope{w1},y-intercept{w0},r{r}')
plt.show()
