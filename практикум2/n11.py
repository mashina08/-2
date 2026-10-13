xc = float(input())
yc = float(input())
r = float(input())
x = float(input())
y = float(input())
if (x - xc)**2 + (y - yc)**2 < r**2:
    print('точка внутри окружности')
elif (x - xc)**2 + (y - yc)**2 > r**2:
    print('точка вне окружности')
else:
    print('точка лежит на окружности')