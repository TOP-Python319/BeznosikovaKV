# Написать программу, которая сравнивает две клетки шахматной доски.

# Программа должна по очереди получить из stdin координаты двух клеток шахматной доски (см. пример ввода).
#     По горизонтали клетка кодируется латинскими буквами от ‘a’ до ‘h’.
#     По вертикали клетка кодируется цифрами от 1 до 8.

# Если две заданные клетки покрашены в один цвет, то программа должна вывести в stdout слово “да”. 
# Если клетки покрашены в разные цвета, то должно быть выведено слово “нет”.

# Примечание: в традиционных шахматах клетка а1 всегда чёрного цвета.

# Пример ввода:
#     a1
#     b2

# Пример вывода:
#     да

# РЕШЕНИЕ

print('Введите координаты двух клеток (a-h)(1-8)')
print('Если клетки одинакого цвета, выведется "да", иначе "нет"')

# Запросим у пользователя координаты двух клеток
cell_1 = input('Введите координаты первой клетки: ')
cell_2 = input('Введите координаты второй клетки: ')

# С помощью функции ord() переведем букву в число
# А цифру в координатах укажем функцией int() для python
meaning_1 = ord(cell_1[0]) + int(cell_1[1])
meaning_2 = ord(cell_2[0]) + int(cell_2[1])

# Поскольку у нас доска состоит из двух цветов (черный и белый)
# приведем полученные значения к остатку (0 или 1)
# Если цвет одинаковый, то значения остатка будут равны

remainder_1 = meaning_1 % 2
remainder_2 = meaning_2 % 2

# Теперь сравним полученные результаты
# И если они равны, то цвета клеток одинаковые, иначе - разные
print('Клетки одного цвета?')

if remainder_1 == remainder_2 :
    print('Да')
else:
    print('Нет')

# Ввод:
#     a1
#     b2

# Вывод:
#     Да