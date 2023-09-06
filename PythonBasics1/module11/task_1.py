print('Задача 1. Конвертация')


# При покупках за рубежом
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например,
# если купить что-то в евро,
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
#
# Напишите программу,
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
#
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

purchase = float(input('Введите стоимость в евро: '))
dollar_ratio = 1.25
rubble_ratio = 60.87
conversion = (purchase * dollar_ratio) * rubble_ratio
print(f'Стоимость в рублях, после конверсии, составит: {round(conversion, 2)}')