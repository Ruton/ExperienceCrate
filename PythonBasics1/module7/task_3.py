print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

yearly_salary = 0

for month in range(1, 13):
    yearly_salary += int(input(f'Введите зарплату за {month}-й месяц: '))

print('Среднегодовая зарплата сотрудника', yearly_salary / 12)