from common_funcs import u, get_num_steps
import matplotlib.pyplot as plt
from math import log2
import numpy as np
import progressbar

N = 1000000

sums = [0]*N
sums_a = [0]*N

us = [0]*N
us_a = [0]*N

X = [0]
steps_sums = [0]

f = open("out.csv", "w")

for i in progressbar.progressbar(range(1,N)):
    sums[i] = sums[i-1] + u(i)
    # sums_a[i] = (i*(i+2))/3
    # us[i] = u(i)
    # us_a[i-1] = sums_a[i] - sums_a[i-1]
    steps_sums.append(get_num_steps(sums[i]))
    X.append(i)

run_avg = [0]*N
log_a = [0]*N
sum = 0
for i in progressbar.progressbar(range(1,N)):
    # keep track of running average
    sum += steps_sums[i]
    run_avg[i] = sum/i

    f.write(f"{i},{run_avg[i]}\n")

    # log approximation
    # log_a[i] = 3*log2(i)

f.close()

# plt.plot(us)
# plt.plot(us_a)
# plt.plot(sums)
# plt.plot(sums_a)
fig = plt.figure()
ax = fig.gca()
# ax.set_xticks(np.arange(0, N, 1))
# ax.set_yticks(np.arange(0, 4, 1))
ax.scatter(X, steps_sums)
# ax.scatter(X, log_a)
# plt.legend(["running average", "log approx"])
# ax.grid()
plt.show()