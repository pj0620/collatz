from common_funcs import u, get_num_steps

N = 100

for m in range(N):
    x1 = 0
    for j in range(2**m):
        x1 += u(j)
    print(f"{x1} -> {(m*(m+2))/3} , {get_num_steps(x1)}")