print('*' * 98)
print('\n3.Пользователь вводит месяц в виде целого числа от 1 до 12.\n'
      'Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).\n'
      'Напишите решения через list и dict.\n')
print('*' * 98)

m_dc = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима"
}
m_ls = ['Зима', 'Зима', 'Весна',
        'Весна', 'Весна', 'Лето',
        'Лето', 'Лето', 'Осень',
        'Осень', 'Осень', 'Зима', ]
try:
    m = int(input('Введите месяц в виде целого числа... '))
    print(m_ls[m - 1])
    print(m_dc[m])

except ValueError:
    print('Введите месяц в виде ЦЕЛОГО ЧИСЛА!')