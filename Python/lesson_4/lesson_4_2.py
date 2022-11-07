from random import randrange

print('*' * 98)
print('\n2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше '
      'предыдущего элемента.\nПодсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его '
      'формирования используйте генератор.\nПример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, '
      '55].\nРезультат: [12, 44, 4, 10, 78, 123].')
print('*' * 98)

ls = list(randrange(-98, 120) for i in range(randrange(12, 24)))
result = []
for i in range(len(ls)):
    try:
        a = ls[i]
        b = ls[i + 1]
        if b > a:
            result.append(b)
    except IndexError:
        pass

print(ls)
print(result)