import math
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_b = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_c = (a**2 + b**2 - c**2) / (2 * a * b)
    a = math.degrees(math.acos(cos_a))
    b= math.degrees(math.acos(cos_b))
    c = math.degrees(math.acos(cos_c))
print(a,b,c, sep='\n')