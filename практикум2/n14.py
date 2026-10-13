n = int(input())
g = n//493
s = (n%493)//17
k = n%17
if g!=0:
    print(f'{g} галлеонов')
if s!=0:
    print(f'{s} сиклей')
if k!=0:
    print(f'{k} кнатов')
