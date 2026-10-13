n, k, m = map(int, input().split())
if n*2%k != 0:
    print((n*2//k + 1)*m)
else:
    print(n*2//k*m)