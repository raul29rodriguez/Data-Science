def myMinimum(a=8,b=2,c=10):
    if a<b and a<c:
        minimum = a
    elif b<a and b<c:
        minimum = b
    elif c<a and c<b:
        minimum = c
    return minimum
a = 4
b = 7
c = 34
minimum = myMinimum()
print(minimum)