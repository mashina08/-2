p = int(input())
if (1000<p<1900 or 2050<p<10000) and p//1000 != p//100%10 != p//10%10 != p%10:
    print('OK')
else:
    print('ERROR')