import matplotlib.pyplot as plt
import numpy as np

# print(plt.__doc__)

# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()

# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

lista_1 = [1,2,3]
lista_2 = [4,5,6]
plt.plot(lista_1, lista_2);

#Instrcutiunea show trebuie sa existe in fisierele de tip .py, altfel nu se ruleaza. In cele de tip ipynb nu este nevoie de instructiunea show
plt.show()