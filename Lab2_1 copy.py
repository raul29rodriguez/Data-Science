import myFunctions
a = float(input("Enter a number "))
b = float(input("Enter a number "))
while True:
    choice = input("choose what operation you would like to perform ")
    if choice=='+':
        myFunctions.addition(a,b)
    elif choice=='-':
        myFunctions.subtraction(a,b)
    elif choice=='*':
        myFunctions.multiplication(a,b)
    elif choice=='/':
        myFunctions.division(a,b)
    else:
        continue

