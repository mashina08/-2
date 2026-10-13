k, a, s = map(int, input().split())
if k>=a and k>=s:
    print(k)
elif a>=k and a>=s:
    print(a)
else:
    print(s)