'''Exercise 1
Ask user to enter a line of text as a string, tokenize the string with the split() method, and
output the tokens in reverse order using the reversed() and join() functions (see slides 278-280).
For example, the input: hello world, how are you? should produce the output: you? are how world,
hello. Use space characters as delimiters'''
userInput=input("Enter a string: ")
uI=userInput.split()
print(' '.join(reversed(uI)))