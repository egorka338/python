a = int(input('введите год'))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('год високосный')
else:
    print('не вискосный')