c = input()
if c[0] in 'aceg' and c[1] in '1357':
    print('черный')
elif c[0] in 'bdfh' and c[1] in '2468':
    print('черный')
else:
    print('белый')