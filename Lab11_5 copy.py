'''Exercise 5
Given the grades.csv file, where the first column is hours studied and the second column is
grades, read its data and place them into two numpy arrays. Find the regression line using the
built-in linregress() method (slides 331-334). Plot the data points along with the regression line
and print: slope, y-intercept, r (correlation coefficient), p-value, standard error. Predict a student's
grade given 10.5 hours of study'''
import numpy as np
from scipy import stats
import pandas as pd
from matplotlib import pyplot as plt
import csv
xLi=[]
yLi=[]
with open('grades.csv', 'r', newline='') as grades:
    reader = csv.reader(grades)
    for record in reader:
        hours,grades=record
        xLi.append(float (hours))
        yLi.append(float (grades))
print(xLi)
print(yLi)
x=np.array(xLi)
y=np.array(yLi)
slope,intercept,r,p,std_err=stats.linregress(x,y)
print('Slope: ',slope,'y-intercept: ',intercept,'Correlation(r): ',r,'p-value: ',p,'Standard Error: ',std_err)
myModel=(slope*x)+intercept
p=(slope*10.5)+intercept
print(f'predicted grade is {p}')
plt.scatter(x,y)
plt.plot(x,myModel)
plt.show()