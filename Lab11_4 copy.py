'''Exercise 4
Based on the dataset from Ex. 1, compute the: SST, SSR, SSE (slide 336) and the: r, R2 (slide
337). You can use the sum() and mean() built-in functions'''
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
x = np.array([-5, -1, 3, 7, 5, 9])
y = np.array([-10, -3, 5, 8, 7, 9])
slope,intercept,r,p,std_err=stats.linregress(x,y)
mymodel=(slope*x)+intercept
SST=sum((y-np.mean(y))**2)
print(SST)
SSR=sum((mymodel-np.mean(y))**2)
print(SSR)
SSE=sum((mymodel-y)**2)
print(SSE)
R2=1-(SSE/SST)
r=R2**(1.0/2)
print(r)
print(R2)