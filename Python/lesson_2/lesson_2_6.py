from pprint import pprint as pp

info = 'Для выхода введите "Q" \nДля добавления товара введите "C"\nДля просмотра списков товара введите "G"\n Для ' \
       'просмотра аналитики введите "A" '

goods = []
analytics = {
    'name': [],
    'price': [],
    'quantity': [],
    'unit': []
}


def category_func() -> []:
    category = {'name': input('Введите название товара...'), 'price': int(input('Введите цену товара...')),
                'quantity': int(input('Введите колличество товара...')), 'unit': input('Введите ед. измерения...')}
    goods.append((
        len(goods) + 1,
        category,
    ))
    return category


try:
    while True:
        print('Для получения иформации введите "Info" ')
        t = input('Enter...').lower()
        if t == 'q':
            print('Выход')
            print(98 * '*')
            break
        elif t == 'info' or t == '':
            print(info)
            continue
        elif t == 'c' or t == 'с':
            category_func()
            pass
        elif t == 'g':
            print(goods)
        elif t == 'a':
            for i in range(len(goods)):
                itm = goods[i][1]
                analytics['name'].append(itm['name'])
                analytics['price'].append(itm['price'])
                analytics['quantity'].append(itm['quantity'])
                analytics['unit'].append(itm['unit'])
            pp(analytics)

except ValueError:
    print('Цена и кол-во товара должны быть числами ')
