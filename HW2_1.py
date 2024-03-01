'''
Exercise 1
Implement Newton’s algorithm for computing the square root of a positive integer given by
the user. Use a precision (threshold) value of 0.00000001
Note: See slide 56 for Newton’s algorithm
'''
num1 = int(input("Enter a number to find the square root of "))
root = num1
while True:
    precision = root
    root = (root+(num1/root))/2
    if (precision - root) >= .00000001 :
        continue
    else:
        break
print("The root of input number is",root)
    