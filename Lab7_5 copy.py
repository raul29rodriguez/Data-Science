'''Exercise 5
Same as in Ex. 4, create two graphs with one plot each. Use the subplots function'''
from matplotlib import pyplot as plt
COSC1310grades = {"HW1" : 35, "HW2" : 49, "HW3" : 74, "HW4" : 67, "HW5" : 75}
COSC3360grades = {"HW1" : 89, "HW2" : 93, "HW3" : 74, "HW4" : 82, "HW5" : 93}
COSC1310_keys=list(COSC1310grades.keys())
COSC1310_values=list(COSC1310grades.values())
COSC3360_keys=list(COSC3360grades.keys())
COSC3360_values=list(COSC3360grades.values())
fig, ax=plt.subplots(nrows=1,ncols=2)
ax[0].plot(COSC1310_keys,COSC1310_values,label='COSC1310',linewidth=3,color='b')
ax[1].plot(COSC3360_keys,COSC3360_values,label='COSC3360',linewidth=3,color='k')
ax[0].set_title('COSC1310')
ax[1].set_title('COSC3360')
ax[0].set_xlabel('Homeworks')
ax[0].set_ylabel('Grades')
ax[1].set_xlabel('Homeworks')
ax[1].set_ylabel('Grades')
ax[0].grid(True,color='k')
ax[1].grid(True,color='k')
ax[0].set_ylim(0,100)
ax[1].set_ylim(0,100)
ax[0].legend()
ax[1].legend()
plt.show()