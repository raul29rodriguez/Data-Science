def myFactorialWIthForLoop(a):
    factorial=1
    for i in range(1,a):
        factorial*=(a)
        a=a-1
        print(factorial)
    print("factorial of input number using for loop is ",factorial)
def myFactorialWIthWhileLoop(a):
    factorial=1
    while True:
        if(a==0):
            break
        factorial*=(a)
        a=a-1
        print(factorial)
    print("factorial of input number using while loop is ",factorial)
a=int(input("Enter a number"))
myFactorialWIthForLoop(a)
myFactorialWIthWhileLoop(a)
        