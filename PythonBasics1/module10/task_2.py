print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

ladder_size = int(input('Введите число: '))

for level in range(ladder_size):
  level += 1
  for block in range(level):
    print(level, end=' ')
  print()
