a = int(input('введите шестизначное число'))
b = a // 100000
c = a // 10000 % 10
d = a // 1000 % 10
t = a // 10000 % 10
s = a // 10000 % 10
o = a % 10
if b + c + d == t + s + o:
    print('happy')
else:
    print('unhappy')