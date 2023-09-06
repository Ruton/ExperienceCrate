print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите высоту пирамиды: '))
start_number = 1

for floor in range(1, height + 1):
  spacer = '\t' * (height - floor)
  print(spacer, end='')
  for slab in range(start_number, start_number + (floor * 2), 2):
    print(slab, end='\t\t')
    start_number = slab + 2
  print()