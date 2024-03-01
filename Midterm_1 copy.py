HWname=[]
HWgrade=[]
n=int(input("How many grades do you wish to enter?: "))
for i in range(n):
    name=input("Enter name: ")
    HWname.append(name)
    grade=int(input("Enter grade: "))
    HWgrade.append(grade)
gradesDictionary={}
for i in range(n):
    gradesDictionary[HWname[i]]=HWgrade[i]
print(gradesDictionary)