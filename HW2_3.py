'''
Exercise 3
Ask user to enter a string, e.g., Computer Science is an amazing field of study. Pass string
to function countWords and return to the main program the number of words in the string
'''
def countWords(str1):
    count = 1
    for i in str1:
        if i==' ':
            count+=1
    return count
str1 = input("Enter a complete sentence ending with '.' ")
count = countWords(str1)
print("total number of words is",count)