print("here")

for a in range(50):
    for b in range(50):
        for c in range(50):
            for d in range(50):
                res = (3*(2**a)*((2**b)-1) + (2**c)*((2**d)-3)) % 9
                # print(res)
                if res == 0:
                    print(f"(a,b,c,d) = ({a},{b},{c},{d})")