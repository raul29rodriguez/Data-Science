def upperCaseCharacter(myStr):
    num = 0
    for i in myStr:
        if ord(i)<=90 and ord(i)>=65:
            print(i)
            num = num+1
    return num
myStr = input("Enter a String ")
num = upperCaseCharacter(myStr)
print(num)


