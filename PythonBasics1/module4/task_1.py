print('Задача 1. Датчик погоды')

# В квартире стоит датчик погоды за окном
# , который определяет, идёт дождь или нет.
# Если пошёл дождь, датчик оповещает владельцев сообщением: «Пошёл дождь. Возьмите зонтик!»
# Напишите программу,
# которая получает на вход число 0 или 1.
# Единица означает, что дождь идёт.
# Если дождь идёт, то выводите на экран сообщение: «Пошёл дождь. Возьмите зонтик!».

# Пример:
# На улице идёт дождь? 1
# Пошёл дождь. Возьмите зонтик!

# Пример 2:
# На улице идёт дождь? 0
# Дождя нет =)

isRaining = input('На улице идёт дождь? ')

if int(isRaining) == 1:
  print('Пошёл дождь. Возьмите зонтик!')

elif int(isRaining) == 0:
  print('Дождя нет =)')

else:
  print('Какая-то странная погода (:')
