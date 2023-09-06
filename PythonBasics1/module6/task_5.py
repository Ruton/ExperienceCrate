print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

ticket = int(input('Введите номер билета: '))

left_sum = (ticket // 100000) + (ticket // 10000 % 10) + (ticket // 1000 % 10)
right_sum = (ticket // 100 % 10) + (ticket // 10 % 10) + (ticket % 10)

if left_sum == right_sum:
  print('Вам попался счастливый билет! Ура!')

else:
  print('Это обычный билет, повезёт в другой раз.')
