print('Задача 7. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
#
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
#
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5

text = input('Введите текст: ')
current_target = 0
new_target = 0

for symbol in text:
    if symbol != ' ':
        new_target += 1
    else:
        if new_target > current_target:
            current_target = new_target
        new_target = 0

if new_target > current_target:
    current_target = new_target

print(f'Длина самого длинного слова: {current_target}')
