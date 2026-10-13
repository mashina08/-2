a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
if (c<=a or d<=a or e<=a) and (c<=b or d<=b or e<=b):
    print('да')
else:
    print('нет')