'''Exercise 6
Given the following list: myList = [3, 9.45, ’Robotics’, 8, 1], use any combination of lambda,
filter, and map to convert the string element of the list to upper case. Your output should be:
ROBOTICS and should be of string data type (not a list). You code should be a one-line code
with the exception of the list definition above, thus, two lines, in total
Note 1: You can use the built-in functions ord() and chr() to convert a single character to
ASCII and an ASCII to a character, respectively, but you cannot use the built-in function upper()
Note 2: You may want to use the function: ”.join() to convert a list of single characters to a
string, that is: myL = [’V’, ’i’, ’s’, ’i’, ’o’, ’n’]; myStr = ”.join(myL)
Note 3: You may wish to first try to filter out the non-string data types then pass the string
data type to a map function. You may have to use nested lambda expressions'''
myList = [3, 9.45, 'Robotics', 8, 1]
print(''.join(map(lambda c : chr(ord(c) - 32) if ord(c) > 96 and ord(c) < 123 else c, ''.join(filter(lambda x: type(x)==str ,myList)))))
