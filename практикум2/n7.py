n = int(input())
if n%10==n//1000 and n//100%10==n%100//10:
    print('настоящее')
else:
    print('кривое')