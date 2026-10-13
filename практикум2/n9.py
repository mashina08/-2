breed = input('Собака короткошерстной породы? ')
height = input('Рост собаки менее 50 см? ')
if breed==height=='да':
    tail = input('У собаки короткий хвост? ')
    if tail=='да': print('английский бульдог')
    else:
        ear = input('У собаки длинные уши? ')
        if ear == 'да': print('гончая')
        else:
            body = input('У собаки короткое тело? ')
            if body == 'да': print('мопс')
            else: print('чихуахуа')
elif breed == 'да' and height=='нет':
    weight1 = input('Собака весит более 50 кг? ')
    if weight1 == 'да': print('датский дог')
    else: print('фоксхаус')
elif breed == 'нет' and height=='да':
    char = input('У собаки доброжелательный характер? ')
    if char == 'да': print('кокер-спаниэль')
    else: print('ирландский сеттер')
else:
    height2 = input('У собаки рост менее 70 см? ')
    if height2 == 'да':
        ear = input('У собаки длинные уши? ')
        if ear=='да': print('большой вандейский грифон')
        else: print('колли')
    else:
        white = input('Окрас рыжий с белыми отметинами? ')
        if white == 'да': print('сербернар')
        else:
            colour = input('Белоснежный окрас? ')
            if colour == 'да': print('ирландский волкодав')
            else: print('ньюфаундлер')