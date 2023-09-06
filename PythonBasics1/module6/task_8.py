print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

funds = int(input('Введите сумму вклада: '))
interest = int(input('Введите процент по вкладу: '))
goal = int(input('Введите целевую сумму: '))
years = 0

while funds < goal:
  years += 1
  funds += int(funds * interest / 100)

print(f'Вклад достигнет целевой суммы за {years} лет.')
