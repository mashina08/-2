x, y, n = map(int, input().split())
r = x*n + (y*n)//100
k = (y*n)%100
print(f'{r} руб. {k} коп.')