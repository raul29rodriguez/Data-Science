import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
TemperatureTexas=np.array([32.4,38.0,45.2,51.3,62.4,70.2,80.5,85.3,94.3,99.2])
TemperatureLuxembourg=np.array([70.3,54.2,63.5,81.2,88.3,74.5,90.2,58.2,72.5,80.2])
sales=np.array([450,430,420,380,350,317,280,228,183,143])
slope,intercept,r,p,std_err=stats.linregress(TemperatureTexas,sales)
print('positive correlation coefficient for Texas is',r*-1)
slope,intercept,r,p,std_err=stats.linregress(TemperatureLuxembourg,sales)
print('positive correlation coefficient for Luxembourg is',r*-1)
print("since Texas correlation coefficient is closer to 1 it means that its data points will better predict future outputs using its model.")