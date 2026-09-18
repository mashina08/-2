x, y = map(int, input().split())
print((max(x, y)%min(x, y))+1)