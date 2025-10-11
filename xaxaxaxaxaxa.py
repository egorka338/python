a = int(input('введите трехзначное число'))
b = a // 100
c = a // 10 % 10
h = a % 10
if (b + c + h) % 5 == 0:
    print('yes')
else:
    print('no')