'''Exercise 4
Create a function named greetingFunction that takes in two arguments, the name of the user
and a greeting, and prints out the greeting along with user’s name; both arguments are given as
user input. Re-write the the functionality of the greetingFunction using a lambda expression'''
def greetingFuction(name,greeting):
    print(greeting+name)
name = ' '+input("Enter your name: ")
greeting = input("Enter a greeting: ")
greetingFuction(name,greeting)

result = lambda name,greeting: greeting+name
print(result(name,greeting))