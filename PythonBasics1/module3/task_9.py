print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.

four_digit = int(input('Введите четырёхзначное число: '))

print(four_digit % 10 * 1000 + four_digit // 10 % 10 * 100 + four_digit // 100 % 10 * 10 + four_digit // 1000)