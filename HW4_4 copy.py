'''Exercise 4
Ask user to enter a sentence, e.g., Computer Science is an amazing field of study. Pass
sentence to function str2words() and convert the string/sentenct into words; place individual
words, e.g., ’Computer’, ’Science’, etc. into a list and return list to main program (your list
should contain 8 elements if the above sentence is entered). In addition, the individual words
should not contain any whitespaces appended to the end of the word such as ’Science ’
Note: Do not use any built-in functions to convert a string to words'''
def str2words(sentence):
    li=[]
    words=''
    for i in range(len(sentence)):
        words+=sentence[i]
        if sentence[i]==' ' or sentence[i]=='.':
            words=words[:-1]
            li.append(words)
            words=''
    return li
sentence = input("Enter a sentence: ")
li = str2words(sentence)
print(li)
