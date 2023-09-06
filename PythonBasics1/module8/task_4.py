print('Задача 4. Отрезок')

#Напишите программу,
# которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

point_a = int(input('Введите число a: '))
point_b = int(input('Введите число b: '))
multiple_of = int(input('Введите число c: '))
average = 0
counter = 0

for number in range(point_a, point_b + 1):

  if not number % multiple_of and number:
    counter += 1
    average += number

print('Среднее арифметическое чисел кратных', multiple_of, 'в заданном отрезке:', average / counter)
