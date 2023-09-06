print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def findHcf(number_1, number_2):
  leftover = True
  numbers = sorted([number_1, number_2])
  hcf = numbers[0]
  leftover = numbers[1] % hcf
  while leftover:
    step = hcf % leftover
    hcf, leftover = leftover, step

  print(f'Наибольший общий делитель чисел {number_1} и {number_2}: {hcf}')

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
findHcf(first_number, second_number)