'''Exercise 2
Ask user to enter a line of text as a string, tokenize the string using space characters as
delimiters and output only those words ending with the letters ’ed’ (see slides 275-276). For
example, the input: It ended as intended should produce the output: ended and intended'''
uI=input("Enter a string: ")
uI=uI.split(' ')
for word in uI:
    if word.endswith('ed'):
        print(word, end=' ')