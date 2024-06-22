import math
number = int(input('Введите число: '))
while int(math.sqrt(number)) - (math.sqrt(number)) != 0:
    number = int(input('Введите другое число: '))
print(f'{number} является полным квадратом')

