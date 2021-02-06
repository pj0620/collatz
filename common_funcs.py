# h(x) for positive integer inputs
def h_p(x):
    if x == 0: return 0
    res = 0
    while x%2 == 0:
        res += 1
        x = x >> 1
    return res

def h(x):
    if x < 0:
        x = abs(x)
    if x-int(x) == 0:
        return h_p(int(x))
    else:
        frac = Fraction(x)
        return h_p(int(frac.numerator))-h_p(int(frac.denominator))

def c(x):
    return int(x/u_old(x))

def u(x):
    if x == 0:
        return 0
    res = x
    while res % 2 == 0 and res != 1:
        res = res // 2
    return res

def u_old(x):
    return 2**h(x)
def ui_old(x):
    return 1/u_old(x)

def getX(xL,L):
    X = [xL]
    x = xL
    for i in range(L):
        x = int((3*x+1)*ui(3*x+1))
        X.append(x)
    return X[::-1]

def getP(X):
    P = [1]
    for i in range(1,len(X)):
        P.append(P[i-1]*(3*X[i]+1))
    return P

def getG(X):
    G = [1]
    for n in range(1,len(X)):
        G.append(
            G[n-1]*(3*X[n])/(3*X[n]+1)
        )
    return G

def check_P_theorem(X,P):
    for m in range(1, L + 1):
        lvalue=P[m] * ui(P[m])
        rvalue=1
        for k in range(m):
            rvalue*=X[k]
        if lvalue != rvalue:
            print(f"wrong !!!!! {lvalue} != {rvalue}")
            break

# returns ui(P[n])
def ui_pn(n,X):
    res = X[0]/(3*X[n]+1)
    for k in range(1,n):
        res *= X[k]/(3*X[k]+1)
    return res

# derives x0 using rest of X
def derive_x0_P(X,P):
    x0=(3 ** L) * X[L] * ui(P[L])
    for k in range(1, L + 1):
        x0 += (3 ** (k - 1)) * ui(P[k])
    return x0

def derive_x0_X(X):
    prods = [1]
    for k in range(1,L+1):
        prods.append(prods[k-1]*X[k]/(3*X[k]+1))

    res = (3**L)*X[L]*(X[0]/(3*X[L]+1))*prods[L-1]
    for j in range(1,L+1):
        res += (3**(j-1)) * (X[0]/(3*X[j]+1)) * prods[j-1]
    return res

# returns total steps for x to reach 1
#
#   x_{n-1} = c(3*c(x_{n}) + 1)
#
def get_num_steps(x):
    cur = x
    steps = 0
    while cur != 1:
        cur = c(3*c(cur) + 1)
        steps += 1
    return steps