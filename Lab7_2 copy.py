'''Exercise 2
Create a 2D list with 3 rows and 2 columns and various values in it. Ask user which element
of the array they wish to modify given the row and column numbers as well as the new value of
the element; print list'''
a=[[5,2],[3,4],[7,9]]
print(a)
row=int(input("Enter row of value you want to modify: "))
col=int(input("Enter column of number you want to modify: "))
num=int(input("Enter new value"))
a[row][col]=num
print(a)