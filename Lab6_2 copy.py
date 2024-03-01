'''Exercise 2
Using a single loop, ask user to enter values to 3 different lists, the first one should contain
the names of 3 people, the second one should contain the heights of 3 people, and the third one
should contain the weights of 3 people. Use the zip function to zip all three lists at the same
time; print list'''
li=[]
li2=[]
li3=[]
for i in range(3):
    name=input("Enter name: ")
    li.append(name)
    height=input("Enter height of person: ")
    li2.append(height)
    weight=input("Enter the weight of person: ")
    li3.append(weight)
joinList=zip(li,li2,li3)
print(list(joinList))