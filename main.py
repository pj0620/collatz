import matplotlib.pyplot as plt
import numpy as np
from levels_func import *
from common_funcs import *
from progressbar import progressbar

Lg, As = get_ln_set(4, 100)
Lg = sorted(Lg)
for xn, A in zip(Lg, As):
    if A[0] % 2 == 1:
        print(f"{xn} -> {get_num_steps(xn)} : {sum(A[1:])%2}")

# print(As)
# xs = [a[0] for a in As]
# ys = [a[1] for a in As]
# fig = plt.figure()
# ax = fig.gca()
# ax.set_xticks(np.arange(0, 100, 5))
# ax.set_yticks(np.arange(0, 100, 5))
# plt.scatter(xs, ys)
# plt.grid()
# plt.show()
# for k in L2:
#     print(f"real : {k} -> steps = {get_num_steps(k)}")