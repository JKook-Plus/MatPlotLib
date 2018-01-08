

import matplotlib.pyplot as plt


x1 = input(str("Input The First X Coordinates spaced by commas: "))
x1list = x1.split(",")

y1 = input(str("Input First Y Coordinates spaced by commas: "))
y1list = y1.split(",")

x2 = input(str("Input Second X Coordinates spaced by commas: "))
x2list = x2.split(",")

y2 = input(str("Input Second Y Coordinates spaced by commas: "))
y2list = y2.split(",")







plt.plot(x1list,y1list)
plt.plot(x2list,y2list)
plt.show()
