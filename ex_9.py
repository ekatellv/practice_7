n, k, r = map(int, input('введите числа: '). split())
days_count = 1
while n <= r:
    days_count += 1
    n = n + (n * k)/100
print(days_count)
