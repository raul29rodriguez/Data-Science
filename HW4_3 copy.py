'''Exercise 3
Given the following list: numbers = [23, 2, 9, 7, 14, 18, 3, 24, 16, 5, 8, 97], use the filter()
function to filter out non-prime numbers, i.e., your output list should contain Prime numbers
only
Note 1: A Prime number is a number that is divisible by 1 and by itself only, e.g., 2, 3, 5, 7, 11
Note 2: Do not manually hardcode any list that contains some of the Prime numbers and use
it for comparison against the numbers list'''
def primeNumbers(n):
    if n%2==0:
        return n==2
    for i in range(3,int(n**.5)+1,2):
        if n % i == 0:
            return False
    return True
numbers = [23, 2, 9, 7, 14, 18, 3, 24, 16, 5, 8, 97]
check = filter(primeNumbers,numbers)
print(list(check))