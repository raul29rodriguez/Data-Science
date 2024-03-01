'''Exercise 1
Read the entire dataset: auto-mpg.csv as a DataFrame and print the numbers of rows and
columns. Find in the dataset all the entries with a ? and replace them with a np.nan. Drop all
rows that do not contain a value. Print again the numbers of rows and columns in the DataFrame
Note: Do not use any loops in the program. You may wish to read slides 257-263'''
import numpy as np
import pandas as pd
import csv
df=pd.read_csv('auto-mpg.csv')
print("rows=",len(df))
print("columns=",len(df.columns))
df=df.replace('?',np.nan)
df=df.dropna()
print(df)
print("rows=",len(df))
print("columns=",len(df.columns))