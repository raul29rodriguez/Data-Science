'''Given the following 3 lists:
fruitName = [’Apples’, ’Oranges’, ’Cherries’, ’Watermelon’]
fruitQuantity_2020 = [25, 25, 10, 18]
fruitQuantity_2021 = [22, 18, 9, 19]
Create 4 subplots, as shown in the Figure in the next page, that is, plot, scatter, stack, pie
plots. The x-axis is the list: fruitName while the y-axes consist of fruitQuantity_2020 and
fruitQuantity_2021
Note 1: In order to create two plots in one graph, as is in first subplot, you can use:
ax[0][0].plot(fruitName, fruitQuantity_2020, label=’2020’, color = ’b’)
ax[0][0].plot(fruitName, fruitQuantity_2021, label=’2021’, color = ’c’)
ax[0][0].legend()
Similarly for the others but use different indices and functions
Note 2: For the pie chart add the respective elements from the two lists, that is, fruitQuan-
tity_2020 and fruitQuantity_2021 resulting in one list'''
from matplotlib import pyplot as plt
fruitName = ['Apples', 'Oranges', 'Cherries', 'Watermelon']
fruitQuantity_2020 = [25, 25, 10, 18]
fruitQuantity_2021 = [22, 18, 9, 19]
fruitQuantitysum = [47,43,19,37]
fig, ax=plt.subplots(nrows=2,ncols=2)
ax[0][0].plot(fruitName, fruitQuantity_2020, label="2020", color = 'b')
ax[0][0].plot(fruitName, fruitQuantity_2021, label="2021", color = 'c')
ax[0][0].legend()
ax[0][1].scatter(fruitName, fruitQuantity_2020, label="2020", color = 'b')
ax[0][1].scatter(fruitName, fruitQuantity_2021, label="2021", color = 'c')
ax[0][1].legend()
ax[1][0].stackplot(fruitName, fruitQuantity_2020, fruitQuantity_2021, labels=['2020','2021'], colors=['b','c'])
ax[1][0].legend()
ax[1][1].pie(fruitQuantitysum, labels = fruitName)
plt.show()