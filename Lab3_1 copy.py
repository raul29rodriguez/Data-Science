'''Exercise 1
Ask user to enter a string, e.g., Computer Science and pass string to function myToUpper.
Inside the function, convert any lower case characters to upper case and print string
Note 1: Do not convert string to a list. Use string concatenation as in Ex. 1 from Exercises to
practice
Note: Use the ord() function, e.g., ord(’C’) to get the ASCII value of a single character and the
chr() function, e.g., chr(67) to get the character given the ASCII value'''
def mytoUpper(str1):
    str2 = ''
    for i in range(len(str1)):
        if ord(str1[i])>=97 and ord(str1[i])<=122:
            str2 += (chr(ord(str1[i])-32)) 
        else:
            str2 += str1[i]
    print(str2)
            
str1 = input("Enter a string ")
mytoUpper(str1)