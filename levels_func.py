import math
import numpy as np

def get_l1_set(max_val):
    return [
        (4 ** i - 1) // 3
        for i in range(1, math.floor(0.5*math.log2(3*max_val+1)))
    ]

def get_l2_set(max_val):
    max_s = int(math.log2(max_val))
    res = []
    for b in range(max_s):
        res += [(2**(4+(-1)**b+b) - 2**(b+1) - 3)//9]
    return res

# used to get next alpha value
# !! optimization:
# !!   A[0] is always even
def getNextA(A, max_val):
    i = 0
    while A[i] >= max_val:
        A[i] = 1
        i += 1
    A[i] += 1

#
# optimization:
#   A[0] is always even
def get_ln_set(n, max_alpha):
    res = []
    As = []
    A = [1]*n
    while A[n-1] < max_alpha:
        # print(f"{A}")
        a = 2**sum(A)
        b = 0
        for k in range(n):
            bp = 0
            if k > 0:
                for t in range(1,k+1):
                    bp += A[n-t]
            b += (3**(n-1-k))*(2**bp)
        xn, r = divmod(a-b, 3**n)
        if r == 0:
            res.append(xn)
            As.append(A.copy())
        getNextA(A, max_alpha)
    return res, As

#
#   second formula
#
def get_ln_set_2(n, max_alpha):
    res = []
    As = []
    A = [1]*n
    A[0] += 1
    while A[n-1] < max_alpha:
        # print(f"{A}")
        a = 2**sum(A)
        b = 0
        for v in range(n):
            pow = 0
            for l in range(v+1):
                pow += A[l]
            b += (3**v)*(2**(-pow))
        xn, r = divmod(a*(1-b), 3**n)
        if r == 0:
            res.append(xn)
            As.append(A.copy())
        getNextA(A, max_alpha)
    return res, As