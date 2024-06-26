# Написать программу, которая подсчитывает сумму только положительных чисел.

# Три числа программа должна по очереди получить из пользовательского ввода (stdin — стандартный поток ввода).

# Пример ввода:
#     4
#     -22
#     1.5

# Пример вывода:
#     5.5

# РЕШЕНИЕ

# Запросим у пользователя три числа
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))

# С помощью sum() высчитаем сумму положительных чисел, проверив полученные числа на положительность
result = sum(num for num in (num1, num2, num3) if num > 0)
# Выведем результат сложения
print(result)

# Ввод:
#     4
#     -22
#     1.5

# Вывод:
#     5.5