print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
#
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

letter_side = int(input('Введите размер одной из сторон письма: '))
envelop_side = 12
folds = 0

if letter_side > envelop_side:

    for fold in range(0, letter_side, envelop_side * 2):
        folds += 2

    print('Необходимо сложить письмо', folds, 'раз(а).')

else:
    print('Письмо поместится в конверт целиком.')