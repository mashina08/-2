n, k, m = map(int, input().split())
v1 = abs(k-m)
v2 = n-abs(k-m)
if v1 <= v2:
    print(v1-1)
else:
    print(v2-1)