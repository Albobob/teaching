print(98 * '*')
print(
    f'4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение\n'
    f'числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без\n'
    f'встроенной функции возведения числа в степень.\n')
print(98 * '*')


def my_func(x: int, y: int) -> float:
    if y < 0:
        t = 1
        result = []
        for i in range(1, abs(y) + 1):
            t *= x
            result.append(1 / t)
            pass
        return result[len(result) - 1]
    else:
        print('По условию задания y < 0')
        return x ** y


print(my_func(3, -3))
