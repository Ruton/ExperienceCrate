print('Задача 8. Замечательные числа')

#Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

for num in range(10, 100):
  if (num // 10) * (num % 10) * 3 == num:
    print(f'Число {num} равно утроенному произведению своих цифр.')