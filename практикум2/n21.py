p1, p2 = input().split('-')
m = [x for x in 'abcdefgh']
if abs(m.index(p2[0]) - m.index(p1[0]))==1 and abs(int(p2[1]) - int(p1[1]))==2:
    print('верно')
elif abs(m.index(p2[0]) - m.index(p1[0]))==2 and abs(int(p2[1]) - int(p1[1]))==1:
    print('верно')
else:
    print('ошибка')