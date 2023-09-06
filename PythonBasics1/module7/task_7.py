print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

counter = 0
sum_values = 0

for point in range(int(input('Введите число a: ')), int(input('Введите число b: ')) + 1):
  if point % 3 == 0:
    counter += 1
    sum_values += point

print('Ответ:', sum_values / counter)
