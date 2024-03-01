'''Exercise 4
Given the following list: li = [9, "Robot", 3.14, 8, "Vision"], use a filter() function along with a
function named int_dataTypes() to filter out irrelevant data types. Your new list should contain
only integers; print list'''
li = [9, "Robot", 3.14, 8, "Vision"]
def int_dataTypes(x):
    if type(x)==int:
        return True
li = list(filter(int_dataTypes,li))
print(li)