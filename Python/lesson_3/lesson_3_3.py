print('*' * 98)
print('\n3. Реализовать функцию my_func(),\n'
      'которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.\n')
print('*' * 98)


def my_func(a, b, c):
    ls = sorted([a, b, c])
    return ls[len(ls) - 2] + max(ls)


print(my_func(10, 2, 30))
