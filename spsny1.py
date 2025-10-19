a = int(input('введите первую сторону'))
b = int(input('введите вторую сторону'))
c = int(input('введите третью сторону'))
if c >= a and c >= b:
    x = c
    y = a
    z = b
elif a >= b and a >= c:
    x = a
    y = b 
    z = c
else:
    x = b
    y = c
    z = a 
if not(x + y > z and y + z > x and z + x > y):
    print('impossible')
elif x**2 == y**2 + z**2:
    print('rectangular')
elif x**2 > y**2 + z**2:
    print('obtuse')
elif x**2 < y**2 + z**2:
    print('acute')
