a = int(input('введите трехзначное число'))
b = a // 100
c = a // 10 % 10
h = a % 10
if (b + c + h) % 5 == int :
    print('yes')
else:
    print('no')