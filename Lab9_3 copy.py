'''Exercise 3
Using the same DataFrame from Ex. 1, plot 5 box plots one for each student within a single
graph (see Figure in the next page). Your algorithm should produce boxplots for any number of
columns not just 5
Note: Rename the x-axis data to students’ names using: plt.xticks([1, 2, 3, 4 ,5], [’Student
Name 1’, ’Student Name 2’, ’Student Name 3’, ’Student Name 4’, ’Student Name 5’]), see Figure
in the next page. The values in these two arguments should be retrieved automatically and
should work for any number of students not just 5'''
import pandas as pd
import matplotlib.pyplot as plt
grades_dict={'Wally':[87,96,70],'Eva':[100,97,90],
'Sam':[94,77,90],'Katie':[100,81,82],
'Bob':[83,65,85]}
grades = pd.DataFrame(grades_dict)
n=[(i+1) for i in range(len(grades.keys()))]
print(n)
plt.boxplot(grades)
plt.xticks(n,grades.keys())
plt.title("Student grades")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.show()