number = int(input('введите число: '))
questions = 0
while 2 ** questions < number:
    questions += 1
print(questions)
