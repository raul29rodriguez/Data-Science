'''Exercise 2
Ask user to enter one of the following two options: 1. Miles->Kilometers or 2. Kilometers-
>Miles. Then, ask user to enter distance (use float instead of int). Pass these two input parameters
to a lambda and return the converted distance (use if else in your lambda expression)'''
choice = int(input("Input 1 for Miles->Kilometers or input 2 for Kilometers->Miles "))
while(choice!=1 and choice !=2):
    choice = int(input("Input 1 for Miles->Kilometers or input 2 for Kilometers->Miles"))
distance=float(input("Enter the distance you want to convert: "))
conversion = lambda choice,distance: distance*1.6  if choice==1 else distance*.62137
print(conversion(choice,distance))