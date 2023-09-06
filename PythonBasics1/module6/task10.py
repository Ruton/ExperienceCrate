print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

mistery = int(input('Введите число от 1 до 100: '))
upper_limit = 100
lower_limit = 1
tryes = 0

while True:
    tryes += 1
    guess = int((upper_limit + lower_limit) / 2)
    answer = int(input(f'Твое число равно(1), меньше(3) или больше(2), чем число {guess}? '))

    if answer == 1:
        print(f'Загаданное число {guess}! Я справился за {tryes} шагов.')
        break

    elif answer == 2:
        lower_limit = guess + 1

    else:
        upper_limit = guess - 1