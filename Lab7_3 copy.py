'''Exercise 3
Ask user to enter the min and max values of a function (use int), e.g., -10 to 10. Create a
range of numbers from min to max and assign it to a variable named x. Compute the absolute
value of the range using a list comprehension using the format: [expression1 if condition else
expression2 for item in iterable] and assign it to variable named y. Plot x, y and add a title to
your plot as well as labels for x and y axes'''
from matplotlib import pyplot as plt
min=int(input("Enter minimum of range: "))
max=int(input("Enter maximum of range: "))
x=range(min,max+1)
print(list(x))
y=[c if c>0 else -c for c in x]
print(y)
plt.plot(x,y)
plt.xlabel('x-asis')
plt.ylabel('y-axis')
plt.title("Graph of |x|")
plt.show()