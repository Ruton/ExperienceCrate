print('Задача 1. Кубы чисел')

# Любителю математики Паше снова стало мало распечатанных табличек,
# включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!

# Напишите программу,
# которая возводит в третью степень каждое число от 1 до N
# и выводит результат на экран.

number_n = int(input('Введите число более 1: '))
current_number = 1

while current_number <= number_n:
  print(f'{current_number} в кубе - {current_number ** 3}')
  current_number += 1
