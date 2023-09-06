print('Задача 3. Функция')

# Учитель математики придумывает каждому своему ученику отдельные функции,
# которые нужно отобразить на графике и посчитать.
# А ещё этот учитель разбирается в программировании.
# Поэтому, чтобы не считать вручную все эти функции,
# он написал программу, которая делает всю работу за него.

# Напишите программу,
# которая получает от пользователя число X и вычисляет значение функции Y

# Напомним, как это работает:
# Если X больше нуля Y = X - 12.
# Если X равных нулю Y равен пяти.
# Если X меньше нуля Y равен квадрату X.

# Пример:
# Введите икс: 0
# Игрек равен 5

# Пример 2:
# Введите икс: -6
# Игрек равен 36

unknown = int(input('Введите икс: '))

if unknown < 0:
  print('Игрек равен:', unknown ** 2)

elif unknown > 0:
  print('Игрек равен:', unknown - 12)

else:
  print('Игрек равен:', 5)
