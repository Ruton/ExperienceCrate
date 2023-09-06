print('Задача 9. Выражение')

# Дано число x.
# Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

number = int(input('Введите число x: '))
top = 0
bottom = 1

for step in range(6):
    bottom *= 2
    top = bottom - 1

    if not step:
        top_result = number - top
        bottom_result = number - bottom

    else:
        top_result *= (number - top)
        bottom_result *= (number - bottom)

print(f'Ответ: {top_result / bottom_result}')

