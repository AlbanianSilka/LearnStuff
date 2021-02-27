import xlsxwriter
import gdown
import random
import timeit
from random import randrange

# ссылка на мой файл на гугл драйве
url = 'https://drive.google.com/uc?id=1ThKn3qS75KCo6UeBVxxv5JFyCay0aKd_'
# # То, с каким именем будет выведен мой файл
output = 'Testing.xlsx'
gdown.download(url, output, quiet=False)
workbook = xlsxwriter.Workbook('Testing.xlsx')
# Просто формат, красящий клетку в жёлтый
rand_yellow = workbook.add_format()
rand_yellow.set_bg_color('yellow')


# Функция для запуска таймера, в ней содержится декоратор
def count_time(func):
    def new_func():
        # Счёт времени делается при помощи библиотеки timeit
        time_started = timeit.default_timer()
        func()
        elapsed = timeit.default_timer() - time_started
        print('Функция "{name}" была выполнена за {time} секунд.'.format(name=func.__name__, time=round(elapsed, 10)))

    return new_func()


@count_time
def random_numbers():
    numbers = range(0, 10)
    worksheet = workbook.add_worksheet(name='Sheet1')
    for x in numbers:
        for y in numbers:
            worksheet.write_column(x, y, [random.randint(1, 100)])
    for i in numbers:
        worksheet.write_column(i, randrange(10), [random.randint(1, 100)], rand_yellow)
    workbook.close()