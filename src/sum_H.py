import matplotlib.pyplot as plt
from scipy import stats

def h(x):
    if x == 0: return 0
    res = 0
    while x%2 == 0:
        res += 1
        x = x >> 1
    return res

xs =  [x    for x in range(5)]
hs =  [h(x) for x in xs]
S_hs = [hs[0]]*len(hs)
P_hs = [hs[1]]*len(hs)
for k in range(1,len(hs)-1):
    S_hs[k] = S_hs[k - 1] + hs[k]
    P_hs[k] = P_hs[1+k - 1] * hs[1+k]

slope, intercept, r_value, p_value, std_err = stats.linregress(xs,P_hs)

print("slope: ",slope,", intercept: ",intercept,"r: ",r_value,"p:",p_value,"std_err:",std_err)

plt.plot(xs,P_hs)
plt.show()

