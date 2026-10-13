height = int(input())
weight = int(input())
imt = weight/(height/100)**2
if imt<16:
    print('выраженный дефицит массы тела')
elif 16<=imt<18.5:
    print('недостаточная масса тела')
elif 18.5<=imt<25:
    print('норма')
elif 25<=imt<30:
    print('избыточная масса тела')
elif 30<=imt<35:
    print('ожирение первой степени')
elif 35<=imt<40:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')