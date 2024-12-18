# Lambda-функция
# Исходные данные
first = 'Мама мыла раму'
second = 'Рамена мало было'

# lambda-функцию для следующего выражения - list(map(?, first, second)).
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.
print(list(map(lambda ft, sd: ft == sd, first, second)))


# Замыкание
# объявление функции get_advanced_writer, принимающая название файла для записи
def get_advanced_writer(file_name):
    # объявление функции write_everything, принимающая неограниченное количество данных любого типа
    def write_everything(*data_set):
        # обращение оператором with к file_name для записи всех данных data_set
        # !!! для добавления к существующей записи новых строк вместо 'w+' указать 'a+'
        with open(file_name, 'w+', encoding='utf-8') as file:
            # цикл перебора данных data_set
            for i in data_set:
                # запись в file перведенных в строку данных i из data_set каждого с новой строки
                file.write(str(i) + '\n')

    # возвращение работы функции get_advanced_writer в write_everything
    return write_everything


# исходные данные, результат в файле example.txt
# Изначально файл example.txt - пустой.
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__
# импорт функции choice из модуля random (весь импорт пишется в начале
# всего кода, но это просто для наглядности импорт написан в этом месте)
from random import choice


# объявление класса MysticBall
class MysticBall:
    # метод инициализации объектов с атрибутами words
    def __init__(self, *words):
        self.words = words

    # метод __call__, который случайным образом выбирать слово из words и возвращает
    # его используя импортированную функцию choice
    def __call__(self):
        return choice(self.words)


# исходные данные для Метод __call__
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно', 'Определенно')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())