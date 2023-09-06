print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
thirdNumber = int(input('Введите третье число: '))
maximum = firstNumber

if firstNumber < secondNumber:
  maximum = secondNumber

if secondNumber < thirdNumber > firstNumber:
  maximum = thirdNumber

print('Максимальное число:', maximum)
