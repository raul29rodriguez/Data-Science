'''Exercise 3
Similarly to Ex. 2, convert 1. Fahrenheit->Celsius or 2. Celsius->Fahrenheit with a lambda'''
choice = int(input("Input 1 forFahrenheit->Celsius or input 2 for Celsius->Fahrenheit "))
while(choice!=1 and choice !=2):
    choice = int(input("Input 1 for Fahrenheit->Celsius or input 2 for Celsius->Fahrenheit "))
temp=float(input("Enter the temperature you want to convert: "))
conversion = lambda choice,temp: temp-32*(5/9)  if choice==1 else temp*1.8+32
print(conversion(choice,temp))