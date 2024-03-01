'''Exercise 3
Given the DataFrame from slide 217, create three plots in the same graph as shown in the
Figure below. The following link describes how to use different line styles, colors, and markers:
https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html'''
import pandas as pd
from matplotlib import pyplot as plt
grades_dict={'Wally':[87,96,70],'Eva':[100,97,90],
'Sam':[94,77,90],'Katie':[100,81,82],
'Bob':[83,65,85]}
grades = pd.DataFrame(grades_dict,index=['Test1','Test2','Test3'])
plt.plot(grades.iloc[0],'--''r''*',label='Test1')
plt.plot(grades.iloc[1],'-.''g''*',label='Test2')
plt.plot(grades.iloc[2],'-''b''*',label='Test3')
plt.legend()
plt.ylim(0,100)
plt.title("Student Grades")
plt.xlabel("Student names")
plt.ylabel("Grades")
plt.show()