a = int(input('введите x'))
b = int(input('введите y'))
if a > 0 and b > 0:
    print('первая четверть')
if a < 0 and b > 0:
    print('вторая четверть')
if a > 0 and b < 0:
    print('четвертая четверть')
if a < 0 and b < 0:
    print('третья четверть')
if a == 0 and b == 0:
    print('ошибка , не вводите координаты равные нулю')