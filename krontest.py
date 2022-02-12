
import matplotlib.pyplot as plt
import numpy as np

A = np.mat("1 0; 1 1")
A2 = np.kron(A,A)
A4 = np.kron(A2,A2)

#print(A4)

plt.spy(A4)
plt.show()
