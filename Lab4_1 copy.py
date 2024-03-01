'''Exercise 1
Given the following list: numbers = [9, -3, 7, 2, 1, 2, 9, 9, 8, 2, 0, 0, 9, 2], ask user to enter
a number. Pass list along with the number entered into function myFind() and find any oc-
currences of the number in the list. Append the index/indices of the number found into list
listIndex. Return listIndex in main program and print list'''
def myFind(numbers,userNum):
    listIndex=[]
    for i in range(len(numbers)):
        if userNum==numbers[i]:
            listIndex.append(i)
    return listIndex
numbers = [9, -3, 7, 2, 1, 2, 9, 9, 8, 2, 0, 0, 9, 2]
userNum = int(input("Enter a number: "))
listIndex=myFind(numbers,userNum)
print(listIndex)