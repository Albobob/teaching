#   1. Поработайте с переменными, создайте несколько, выведите на экран.
#   Запросите у пользоватля некоторые числа и строки и сохраните в переменные, затем выведите на экран.

try:
    a = str(input('Введите текст...'))
    b = int(input('Введите число...'))

    print(f'Переменная a = {a}, имеет тип {type(a)},'
          f'переменная b = {b}, имеет тип {type(b)}')
except ValueError:
    print('Введите то, что просят!')

print('*************************************************************')

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
try:
    b = int(input('Введите число...'))
    b_1 = int(f'{b}{b}')
    b_2 = int(f'{b}{b}{b}')

    print(f'{b} + {b}{b} + {b}{b}{b} = {b + b_1 + b_2}')

except ValueError:
    print('Введите число!')

print('*************************************************************')

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
try:
    b = int(input('Введите число...'))
    num_string = str(b)
    ls = list(map(int, num_string))
    print(max(ls))



except ValueError:
    print('Введите число!')
