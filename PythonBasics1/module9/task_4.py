print('Задача 4. Театр')

# Планируется построить театр под открытым небом,
# но для начала нужно хотя бы примерно понять сколько должно быть рядов,
# сидений в них и какое лучше сделать расстояние между рядами.
#
# Напишите программу,
# которая получает на вход кол-во рядов, сидений и свободных метров между рядами,
# а затем выводит примерный макет театра на экран.

# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======

rows = int(input('Введите кол-во рядов: '))
seats = '=' * int(input('Введите кол-во сидений ряду: '))
walkway = '*' * int(input('Введите кол-во метров между рядами: '))

#вариант с использованием for
#print('\n')
#
#for _ in rows:
#  print(f'{seats} {walkway} {seats}')

scheme = (f'{seats} {walkway} {seats}\n') * rows
print(f'\n{scheme}')
