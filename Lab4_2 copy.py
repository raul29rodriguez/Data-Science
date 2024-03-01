'''Exercise 2
Given the following string: str1 = ’Computer Science’, use a filter to filter out consonants, i.e.,
your output list should contain any vowels found'''
def myFunction(str1):
    for i in range(len(str1)):
        if str1[i]=='a' or str1[i]=='e' or str1[i]=='i' or str1[i]=='o' or str1[i]=='u':
            return True
str1='Computer Science'
result=filter(myFunction,str1)
print(list(result))