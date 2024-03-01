'''Exercise 4
Based on Ex. 3, create two more functions where only the names of the telephone directory
are listed or only the telephone numbers'''
def addFunction(telephone_book):
    name=input("Enter name you wish to add: ")
    number=int(input("Enter number you wish to add: "))
    telephone_book[name]=number
    return telephone_book
def removeFunction(telephone_book):
    name=input("Enter name which you would like to remove: ")
    del telephone_book[name]
    return telephone_book
def modifyFunction(telephone_book):
    name=input("Enter name which you would like to modify: ")
    number=int(input("Enter modified number: "))
    telephone_book[name]=number
    return telephone_book
def searchFunction(telephone_book):
    name=input("Enter the name you would like to search: ")
    print(telephone_book[name])
    return telephone_book
def printNames(telephone_book):
    for names in telephone_book.keys():
        print(names)
def printNumbers(telephone_book):
    for values in telephone_book.values():
        print(values)
telephone_book={'Raul Rodriguez':2544853956,'John Blue':9402853789,'Garret Wilson':2594857424}
while True:
    print(telephone_book)
    print("1=add,2=remove,3=modify,4=search,5=print names,6=print numbers,7=exit")
    op=int(input("enter what operation you want to perform: "))
    if op==1:
        telephone_book=addFunction(telephone_book)
    elif op==2:
        telephone_book=removeFunction(telephone_book)
    elif op==3:
        telephone_book=modifyFunction(telephone_book)
    elif op==4:
        telephone_book=searchFunction(telephone_book)
    elif op==5:
        printNames(telephone_book)
    elif op==6:
        printNumbers(telephone_book)
    elif op==7:
        exit()