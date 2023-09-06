print('Задача 3. Апгрейд калькулятора')


# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.

# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

def megaCalculator():
    number = input('Введите число: ')
    action = int(input(
        '\nВыберите действие:\n\t1. Сумма цифр числа\n' +
        '\t2. Максимальная цифра числа\n\t3. Минимальная цифра числа\n\nВвод: '
    ))
    if action == 1:
        digitSum(number)
    elif action == 2:
        maxDigit(number)
    elif action == 3:
        minDigit(number)
    else:
        print('Некорректный ввод, начните сначала.\n')
        megaCalculator()


def digitSum(number):
    sum = 0
    for digit in number:
        sum += int(digit)
    print(f'Сумма цифир числа {number}: {sum}')
    print('\nСледующая операция\n' + '=' * 18)
    megaCalculator()


def maxDigit(number):
    highest_digit = 0
    for digit in number:
        if int(digit) > highest_digit:
            highest_digit = int(digit)
    print(f'Наибольшей цифрой числа {number} является: {highest_digit}')
    print('\nСледующая операция\n' + '=' * 18)
    megaCalculator()


def minDigit(number):
    lowest_digit = int(number[0])
    for digit in number:
        if int(digit) < lowest_digit:
            lowest_digit = int(digit)
    print(f'Наименьшей цифрой числа {number} является: {lowest_digit}')
    print('\nСледующая операция\n' + '=' * 18)
    megaCalculator()


megaCalculator()
