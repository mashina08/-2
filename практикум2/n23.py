n = int(input())
if n < 11:
    print(n-1)
elif 11<=n<=190:
    n -= 10
    num = 10+(n-1)//2
    if (n-1)%2==0:
        print(num//10)
    else:
        print(num%10)
else:
    n -= 190
    num = 100+(n-1)//3
    if (n-1)%3==0:
        print(num//100)
    elif (n-1)%3==1:
        print(num//10%10)
    else:
        print(num%10)

