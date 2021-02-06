from common_funcs import u, get_num_steps, h
import matplotlib.pyplot as plt
import numpy as np
from math import floor, log2

N = 50
X = []
Y = []

# IRRATIONAL NUMBER
q = np.exp(1)

# res = 1
# for n in range(1,N):
#     res *= (u(n)/(2*n-1))*(u(n)/(2*n+1))
# print(2*res)

for k in range(N):
    num = floor((2**k)*q)
    den = 2**k
    print(bin(num))

    X.append(k)
    Y.append(log2(num/u(num)))

print(Y[-1])

fig = plt.figure()
# ax = fig.gca()
# ax.set_xticks(np.arange(0, N, 10))
# ax.set_yticks(np.arange(0, 1000, 5))
plt.scatter(X,Y)
# plt.grid()
plt.show()
