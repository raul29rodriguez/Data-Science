import numpy as np
from matplotlib import pyplot as plt
x=np.array([3.00,3.25,3.50])
y=np.array([4500,3750,3300])
w1=((np.mean(x*y))-(np.mean(x)*np.mean(y)))/((np.mean(x**2))-(np.mean(x)**2))
w0=np.mean(y)-(w1*np.mean(x))
Ymodel=w0+(w1*x)
#prediction
p=np.linspace(3.30,3.45,num=4)
#print(p)
prediction=w0+(w1*p)
print(prediction)
plt.scatter(x,y)
plt.plot(x,Ymodel)
plt.show()