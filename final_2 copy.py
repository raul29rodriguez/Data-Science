import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
x=np.array([3.00,3.25,3.50])
y=np.array([4500,3750,3300])
model1=(-2600*x)+12300.0
model2=(-2400*x)+11650.0
w1=((np.mean(x*y))-(np.mean(x)*np.mean(y)))/((np.mean(x**2))-(np.mean(x)**2))
w0=np.mean(y)-(w1*np.mean(x))
print("intercept",w0,"slope",w1)
print("Given the equation we did to find the slope and intercept of the data, we can see that model 2 best fits the data given that it has the same slope and intercept as what the equation returns.")
plt.scatter(x,y)
plt.plot(x,model1)
plt.plot(x,model2)
plt.show()