str = input('Введите строку: ')
result = ''
for index, value in enumerate(str, start=1):
    if index % 3 == 0:
        result += value

print(result)
