print('Задача 2. Долги')

# МирПрогБанк наконец-то разделил законопослушных граждан и должников и поместил их в разные базы.
# Но банк не торопится как-то слишком сильно давить на возврат денег.
# Сейчас операторам банка дали задание
# позвонить каждому пятому должнику из списка (они нумеруются с нуля) и спросить,
# сколько примерно денег каждый из них задолжал банку.
#
# Напишите программу,
# которая принимает на вход количество должников,
# затем спрашивает у каждого пятого (начиная с 0) его долг.
# В конце выводится общая сумма долгов.

# Пример:
#
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000

debtors = int(input('Введите количество должников: '))
credits_sum = 0

for debtor in range(0, debtors, 5):
  print('Должник с номером', debtor)
  credits_sum += int(input('Сколько должны? '))

print('Общая сумма долга', credits_sum)
