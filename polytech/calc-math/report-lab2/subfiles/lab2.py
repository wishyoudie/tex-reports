import math
import pandas as pd
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

# numpy.linalg.eig
# plt.plot([0, 1, 2, 3], [0, 1, 4, 9], 'r')
# plt.show()

# w, v = LA.eig(np.diag((1, 2, 3)))
#print(w, v)
# q, r = LA.qr(np.diag((1, 2, 3)))
# LA.cholesky
# k_k = 3
# a = np.random.rand(k_k, k_k)
# x = np.random.rand(k_k, 1)
# b = a @ x
# pogr = []
# for i in range(15):
#     s, j = LA.eig(a)
#     j[0][0] = j[0][0] * 10 ** i
#     t = np.dot(np.dot(s, j), LA.inv(s))
#     b1 = t @ x
#     l, u = LA.lu(t)
#     x1 = inv(u) @ inv(l) @ b1
#     pogr[i] = LA.norm(x1 - x) / LA.norm(x)

# plt.plot(pogr)
# plt.show()

