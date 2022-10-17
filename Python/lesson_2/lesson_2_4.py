print(98 * '*')
try:
    a = list(input('Введите строку из нескольких слов...').split())
    for i in range(len(a)):
        print(f'{i + 1}. {a[i][:10]}')
except ValueError:
    print('Введите строку из нескольких слов!')
print(98 * '*')
