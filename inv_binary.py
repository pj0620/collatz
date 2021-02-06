x_val = 3

N = 10

for x_val in range(1, 10000000):
    # get bin(x)
    cur = x_val
    i = 0
    x = [0]*N
    while cur > 0 and i < N:
        next = cur - 2**i
        if next >= 0:
            x[i] = 1
            cur = next
        i += 1

    # get bin(1/x)
    cur = 1/x_val
    i = 0
    xi = [0]*N
    while cur > 0 and i < N:
        xi[i] = int(cur)
        if cur >= 1:
            cur -= 1
        cur *= 2
        i += 1

    S = 0
    for i in range(N):
        S += x[i]*xi[i]

    if S != 0:
        print("x = " + str(x_val))