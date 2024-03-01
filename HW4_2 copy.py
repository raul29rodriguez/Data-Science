'''Exercise 2
Given the following list: words = [’Anna’, ’hELLo’, ’rotor’, ’wow’, ’CS’, ’kayAK’, ’program-
ming’], use the filter() function to filter out the non-palindrome words, i.e., your output list
should contain palindrome words only
Note 1: You can use the built-in function upper() to convert a string to uppercase or the
round() function to round a number
Note 2: Your algorithm should be able to cope with both odd as well as even length words,
e.g., ’wow’ or ’Anna’'''
def palindromeWords(words):
    if(words == words[::-1]) or words.upper()==words.upper()[::-1]:
        return True
    else:
        return False
    
words = ['Anna', 'hELLo', 'rotor', 'wow', 'CS', 'kayAK', 'programming']
check = filter(palindromeWords,words)
print(list(check))