print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

overall = int(input('Укажите количество вводимых чисел: '))
max_sum = 0
target_number = None

for _ in range(overall):
  number = input('Введите число: ')
  if number.isdigit():
    last_sum = 0
    for digit in number:
      last_sum += int(digit)
    if last_sum > max_sum:
      max_sum = last_sum
      target_number = number

print('Число', target_number, 'имеет наибольшую сумму цифр среди',
      'введённых натуральных чисел -', max_sum)
