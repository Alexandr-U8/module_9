# Ф-ция-генератор all_variants возвращает объект-генератор
# со встроенным итератором.
def all_variants(text):
    # Запуск цикла перебора элементов text
    for i in range(len(text)):
        # Запуск цикла перебора элементов text - i элемент
        for j in range(len(text) - i):
            # Возвращение полученного значения и приостановка
            # выполнения ф-ции до следующего вызова
            yield text[j:j+i+1]

# исходные данные
a = all_variants("abc")
for i in a:
    print(i)