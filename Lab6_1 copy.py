'''Exercise 1
Given the 2D list from slide 112, convert all values to 255 if they are above a threshold or to 0
if they are below. The threshold value is given as input by the user. This is an example of how a
grayscale image is converted to a binary (black & white)'''
a = [[77,68,86,73],[96,87,89,81],[70,90,86,81]]
threshold = int(input("Enter the threshold: "))
for row in range(len(a)):
    for col in range(len(a[row])):
        if a[row][col]>threshold:
           a[row][col]=255
        else:
            a[row][col]=0
print(a)