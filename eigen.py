import numpy as NP
#from scipy import linalg as LA
from scipy.linalg import fblas
import scipy as SP

A = NP.random.randint(0, 2, 25).reshape(5, 5)
print(A)


e_vals, e_vecs = eig(A)
print(e_vals)

print(e_vecs)
