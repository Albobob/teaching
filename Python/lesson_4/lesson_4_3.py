print('*' * 98)
print('\n4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив\n'
      'чисел, соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения\n'
      'задания обязательно используйте генератор.\nПример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7,'
      '4, 11].\nРезультат: [23, 1, 3, 10, 4, 11]\n')
print('*' * 98)

ls = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
ls_2 = [i for i in ls if ls.count(i) == 1]
print(ls)
print(ls_2)