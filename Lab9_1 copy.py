'''Exercise 1
Given the DataFrame of slide 241, ask user to enter the names of the rows, i.e., indices.
You can use: len(grades) to get the number of rows of the DataFrame. In addition, using the
sort_index() method, ask user whether they wish to sort by rows or by columns and whether to
sort in ascending or descending order (do not use any if-else statements)'''
import pandas as pd
grades_dict={'Wally':[87,96,70],'Eva':[100,97,90],
'Sam':[94,77,90],'Katie':[100,81,82],
'Bob':[83,65,85]}
grades = pd.DataFrame(grades_dict)
grades.index=[input("Enter name for row: ")for i in range(len(grades))]
print(grades.sort_index(axis=int(input("Enter 0 for row sorting, enter 1 for column sorting: ")),
ascending=bool(input("Enter True for ascending order, leave blank for descending order: "))))
