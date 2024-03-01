'''Exercise 3
Given the following string: str1 = ’Computer Science’, use a filter to filter out any lower case
characters, i.e., your output list should contain any upper case characters only
'''
def myFunction(str1):
    for i in range(len(str1)):
        if ord(str1[i])>=97 and ord(str1[i])<=122:
            return True
str1='Computer Science'
result=filter(myFunction,str1)
print(list(result))