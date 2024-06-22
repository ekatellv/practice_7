n = int(input('введите число: '))
a = 1
volumes = []
v = a ** 3
while v <= n:
    volumes.append(v)
    a += 1
    v = a ** 3
for item in volumes:
    print(item, end=' ')
