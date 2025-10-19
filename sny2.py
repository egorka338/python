# 5 , 7 
a = int(input('введите трехзначное число'))
b = a // 100
c = a // 10 % 10
r = a % 10
if b == 5 or  c == 5 or r == 5:
    print('yes')
elif b == 7 or c == 7 or r ==7:
    print('yes')
else:
    print('no')
