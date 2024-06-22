from math import sqrt
number = int(input('введите число: '))
if int(sqrt(number)) - sqrt(number) == 0:
    print('верно')
else:
    print('неверно')
