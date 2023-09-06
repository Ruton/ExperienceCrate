print('Задача 3. Рамка')

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|

width = int(input('Введите ширину рамки: '))
height = int(input('Введите высоту рамки: '))

# В качестве решения подготовил три варианта построения рамок
# В данном случае считаю единицей высоты только строки без "-"
for row in range(height + 2):
    print('|', end='')
    for column in range(width):
        if row == 0 or row == height + 1:
            print('-', end='')
        else:
            print(' ', end='')
    print('|')

# Для визуального разделения таблиц
print()

# В оставшихся случаях считаю каждый вывод "|" единицей высоты
for row in range(height):
    print('|', end='')
    for column in range(width):
        if row == 0 or row == height - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print('|')

# Вариант с "_"
for row in range(height + 1):
    if row:
        print('|', end='')
    else:
        print(' ', end='')
    for column in range(width):
        if row == 0 or row == height:
            print('_', end='')
        else:
            print(' ', end='')
    if row:
        print('|')
    else:
        print(' ')