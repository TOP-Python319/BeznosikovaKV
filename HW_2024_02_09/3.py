# Написать программу, которая определяет, является ли год високосным.

# Номер года программа должна получить из stdin (пользовательский ввод). 
# Если год является високосным, то программа должна вывести в stdout слово “да”.
# В противном случае должно быть выведено слово “нет”.

# Примечание: год является високосным, если его номер кратен 4, но одновременно не кратен 100,
# или если он кратен 400.

# Пример ввода:
#     2020

# Пример вывода:
#     да

# РЕШЕНИЕ

# Запросим у пользователя год
print('Проверка года на високосность')
year = int(input('Введите год: '))

print(f'{year} является високосным годом?')
# Сделаем рассчеты
# Если високосный выведем "да"
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Да')
# Иначе выведем "нет"
else:
    print('Нет')


# Ввод:
#     2020

# Вывод:
#     Да