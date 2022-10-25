print('*' * 98)
print('\n7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.\nКаждое '
      'слово    состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно\n'
      'начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().\n')
print('*' * 98)


def int_func(var: str) -> str:
    var.lower()
    return var.capitalize()
    pass


def my_func(value) -> str:
    ls = []
    for i in value.split():
        ls.append(i.capitalize())
    txt = ''
    for i in ls:
        txt += f'{i} '

    return txt


my_string = int_func("альберт ПЕРЕЛЕЗ чЕрЕз забор,  и порвал штаны")
print(my_func(my_string))
