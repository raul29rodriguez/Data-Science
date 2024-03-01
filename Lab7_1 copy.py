'''Exercise 1
Create a list of numbers from 10 to 20 and out of the list create two sets where the first set, set
A, contains the numbers 10 to 20 (inclusive) and the second set, set B, contains the odd numbers
of the list (use set comprehension). Ask the user whether they wish to add, remove, perform
union, intersection, difference, symmetric difference, or disjoint between the two sets. For
adding or removing elements, ask user on which set they wish to carry out the operation. Use
functions for all seven operations'''
def addFunction(sett):
    num=int(input("Enter the number you want to add to the set: "))
    sett.add(num)
    print(sett)
def removeFunction(sett):
    num=int(input("Enter the number you want to add to the set: "))
    sett.remove(num)
    print(sett)
def unionFunction(set1,oddSet):
    print(set1 | oddSet)
def intersectFunction(set1,oddSet):
    print(set1 & oddSet)
def differenceFunction(set1,oddSet):
    print(set1 - oddSet)
def symmetricDiffFunction(set1,oddSet):
    print(set1 ^ oddSet)
def disjointFunction(set1,oddSet):
    print(set1.isdisjoint(oddSet))
li=[10,11,12,13,14,15,16,17,18,19,20]
set1=set(li)
oddSet={item for item in li if item %2 !=0}
print(set1)
print(oddSet)
print("Choose your operation on the provided sets: ")
choice=int(input("1=add, 2=remove, 3=union, 4=intersection, 5=difference, 6=symmetric difference, or 7=disjoint: "))
if choice==1:
    choice2=int(input("Would you like to perform operation on original set, or odd set? 1=original, 2=odd: "))
    if choice2==1:
        addFunction(set1)
    elif choice2==2:
        addFunction(oddSet)
elif choice==2:
    choice2=int(input("Would you like to perform operation on original set, or odd set? 1=original, 2=odd: "))
    if choice2==1:
        removeFunction(set1)
    elif choice2==2:
        removeFunction(oddSet)
elif choice==3:
    unionFunction(set1,oddSet)
elif choice==4:
    intersectFunction(set1,oddSet)
elif choice==5:
    differenceFunction(set1,oddSet)
elif choice==6:
    symmetricDiffFunction(set1,oddSet)
elif choice==7:
    disjointFunction(set1,oddSet)