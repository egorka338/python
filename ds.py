a = int(input('введите x'))
b = int(input('введите y'))
if a > 0 and b > 0:
    print('первая четверть')
elif a < 0 and b > 0:
    print('вторая четверть')
elif a > 0 and b < 0:
    print('четвертая четверть')
elif a < 0 and b < 0:
    print('третья четверть')
elif a == 0 or b == 0:
    print('ошибка , не вводите координаты равные нулю')