#5
print(98 * '*')

ls = [7, 5, 3, 3, 2]


def rank(num: int) -> []:
    ls.append(num)
    ls.sort(reverse=True)
    return ls


print('Для выхода введите "000"')
while True:
    a = input('Введите рейтинг... ')
    if a == '000':
        print('Выход')
        print(98 * '*')
        break
    elif a == '':
        continue
    elif 2 <= int(a) <= 7:
        a = int(a)
        print(rank(a))
    else:
        print('Введите значение от 2 до 7')
        continue