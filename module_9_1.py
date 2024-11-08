# объявление функции apply_all_func

def apply_all_func(int_list, *functions):
    # Обьявление словаря
    result = {}
# цикл перебора функции
    for i in functions:
        result[i.__name__] = i(int_list)
    return result

#данные
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))