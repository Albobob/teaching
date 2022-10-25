print('\n6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,\n'
      'но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.\n')


def int_func(var: str) -> str:
    var.lower()
    return var.capitalize()
    pass


print(int_func("альберт ПЕРЕЛЕЗ чЕрЕз забор"))
