max_alpha = 16

# def h_p(x):
#     if x == 0: return 0
#     res = 0
#     while x%2 == 0:
#         res += 1
#         x = x >> 1
#     return res
#
# def h(x):
#     if x < 0:
#         x = abs(x)
#     if x-int(x) == 0:
#         return h_p(int(x))
#
# def c(x):
#     return int(x/u(x))
#
# def u(x):
#     return 2**h(x)
#
# def get_num_steps(x):
#     cur = x
#     steps = 0
#     while cur != 1:
#         cur = c(3*c(cur) + 1)
#         steps += 1
#     return steps

def getNextA(A, max_val):
    i = 0
    while A[i] >= max_val:
        A[i] = 1
        i += 1
    A[i] += 1


for n in range(1, 100):
    f = open(f"collatz-{n}.csv", "w")
    f.write("depth, xn, alpha values\n")
    A = [1]*n
    while A[n-1] < max_alpha:
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
            f.write(f"{n}, {xn}, {','.join(str(x) for x in A)} \n")
        getNextA(A, max_alpha)
    f.close()