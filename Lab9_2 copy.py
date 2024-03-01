'''Exercise 2
Similarly to Ex.1, use the sort_values() method and ask user to enter values for all its three
arguments
Note: If you sort by rows, i.e., axis=0, the by argument has to be followed by the name of a
student; if you sort by columns, i.e., axis=1, the by argument has to be followed by the name of
the assignment'''
import pandas as pd
grades_dict={'Wally':[87,96,70],'Eva':[100,97,90],
'Sam':[94,77,90],'Katie':[100,81,82],
'Bob':[83,65,85]}
grades = pd.DataFrame(grades_dict)
grades.index=[input("Enter name for row: ")for i in range(len(grades))]
print(grades.sort_values(axis=int(input("0 for row sorting, 1 for column sorting: ")),
ascending=bool(input("Enter True for ascending order, leave blank for descending order: ")),
by=input("Enter name if axis=0, enter assignment if axis=1: ")))
