sum = 4
numerator = 4
denominator = 3
for i in range(5200):
    if i%2:
        sum = sum+(numerator/denominator)
    else:
        sum = sum-(numerator/denominator)
    denominator=denominator+2
    print(sum)