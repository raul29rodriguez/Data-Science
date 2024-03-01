def factorialFunction(denominator,factorial):
    while factorial>0:
        factorial-=1
        if factorial==0:
            denominator*=factorial+1        
        else:
            denominator*=factorial
    return denominator
sum = 1
numerator = 1
for i in range(1,11):
    denominator=i
    factorial = denominator
    denominator = factorialFunction(denominator,factorial)
    sum = sum+(numerator/denominator)
    print("sum",sum)
   #print(sum)