n, m = map(int, input().split('x'))
k = int(input())
if k%n==0 and k//n<=m or k%m==0 and k//m<=n:
    print('успешно')
else:
    print('неосуществимо')