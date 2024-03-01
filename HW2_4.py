'''
Exercise 4
Ask user to enter a string, e.g., Computer Science, convert it to a list using the list() function,
i.e., list(myStr), and pass the list to function myToUpper. Inside the function, convert any lower
case characters to upper case and print the entire list
Note: Use the ord() function, e.g., ord(’C’) to get the ASCII value of a single character and the
chr() function, e.g., chr(67) to get the character given the ASCII value
'''
def myToUpper(str2):
    for i in range(len(str2)):
        if ord(str2[i]) >= 97 and ord(str2[i]) <= 122:
            str2[i]=chr(ord(str2[i])-32)
    print(str2)        
str1 = input("Enter a string ")
str2 = list(str1)
myToUpper(str2)

