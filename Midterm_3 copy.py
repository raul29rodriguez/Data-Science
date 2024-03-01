from matplotlib import pyplot as plt
grades ={'HW1':93,'HW2':85,'HW3':94,'HW4':90,'HW5':82}
x=list(grades.keys())
y=list(grades.values())
plt.plot(x,y)
plt.xlabel("HW name")
plt.ylabel("Grade")
plt.title("HW grades plot")
plt.ylim(0,100)
minimum=y[0]
maximum=y[0]
for i in range(len(y)):
    if y[i]<minimum:
        a=i
    if y[i]>maximum:
        b=i
plt.scatter(x[a],min(y),label='min grade',color='r')
plt.scatter(x[b],max(y),label='max grade',color='g')
plt.legend()
plt.show()