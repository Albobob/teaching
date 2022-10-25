print('*' * 98)
print('\n2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:\n'
      'имя, фамилия, год рождения, город проживания, email, телефон.\n'
      'Функция должна принимать параметры как именованные аргументы.\n'
      'Реализовать вывод данных о пользователе одной строкой.\n')
print('*' * 98)

def my_function(first_name: str, last_name: str, year_of_birth: int, city: str, mail: str, phone: str) -> str:
    return f'Имя: {first_name}\nФамилия: {last_name}\nДата рождения: {year_of_birth}\nГород: {city}\nПочта: {mail}\n' \
           f'Номер телефона: {phone}'


print(my_function('Albert', 'Simonyan', 1998, 'Tver', 'treblarpip@gmail.com', '+1(779)1234567'))
