'''Exercise 2
Ask user to enter a string, e.g., Computer Science; then ask user to enter a single character,
e.g., e. Pass both strings to function myFind and print the index at which the character appears
in the string. In addition, print the number of occurrences of the character in the string'''
def myFind(str1,char):
    sum=0
    for i in range(len(str1)):
        if char==str1[i]:
            print("character",char,"found at index ",i)
            sum+=1
    print("character",char,"found ",sum,"times in the string")
str1 = input("enter a string ")
char = input("enter a character to find in string ")
myFind(str1,char)