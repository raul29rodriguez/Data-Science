'''Exercise 1
Given the following dictionary:
temps = ’Mon’: [68, 89], ’Tue’: [71, 93], ’Wed’: [66, 82], ’Thu’: [75, 97], ’Fri’: [62, 79]
perform the following tasks:
• Convert the dictionary into the DataFrame named temperatures with ’Low’ and ’High’ as
the indices, then display the DataFrame
• Use the column names to select only the columns for ’Mon’ through ’Wed’
• Use the row index ’Low’ to select only the low temperatures for each day
• Set the floating-point precision to 2, then calculate the average temperature for each day
• Calculate the average low and high temperatures (you can use the mean() built-in function)'''
import pandas as pd
temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}
temperatures = pd.DataFrame(temps,index=['Low','High'])
print(temperatures)
print(temperatures.iloc[0,0:3]) #was not sure if wanted them seperate, but I did them together in one
pd.set_option('display.precision', 2)
print(temperatures.mean())
print(temperatures.mean(axis=1))