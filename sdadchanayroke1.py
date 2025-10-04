a = int(input('введите двухзначное число'))
b = a // 10
x = a % 10
if b > x:
    print("first")
elif b < x:
    print("second")
else:
    print("equal")       