'''Exercise 4
Using the following two dictionaries:
COSC1310grades = {"HW1" : 35, "HW2" : 49, "HW3" : 74, "HW4" : 67, "HW5" : 75}
COSC3360grades = {"HW1" : 89, "HW2" : 93, "HW3" : 74, "HW4" : 82, "HW5" : 93}
create a single graph, with two plots on it, one for each dictionary. The x and y values
correspond to the key and value of each dictionaries. You can use the built-in functions to extract
the keys and values from the dictionaries. Add labels, color, linewidth, and legend to your
graph'''
from matplotlib import pyplot as plt
COSC1310grades = {"HW1" : 35, "HW2" : 49, "HW3" : 74, "HW4" : 67, "HW5" : 75}
COSC3360grades = {"HW1" : 89, "HW2" : 93, "HW3" : 74, "HW4" : 82, "HW5" : 93}
COSC1310_keys=list(COSC1310grades.keys())
COSC1310_values=list(COSC1310grades.values())
COSC3360_keys=list(COSC3360grades.keys())
COSC3360_values=list(COSC3360grades.values())
plt.plot(COSC1310_keys,COSC1310_values,label='COSC1310',linewidth=5,color='b')
plt.plot(COSC3360_keys,COSC3360_values,label='COSC3360',linewidth=5,color='k')
plt.xlabel('Homeworks')
plt.ylabel('Grades')
plt.title("COSC grades")
plt.legend()
plt.grid(True,color='k')
plt.show()