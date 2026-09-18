from math import pi
a = int(input())
b = int(input())
big = (max(a, b))**2*pi
small = (min(a, b))**2*pi
print(big-small)
