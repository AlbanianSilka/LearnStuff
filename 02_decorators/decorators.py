import xlsxwriter
import gdown
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import random
import timeit
from random import randrange

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
gdrive = GoogleDrive()


# ссылка на мой файл на гугл драйве
# url = 'https://drive.google.com/uc?id=1ThKn3qS75KCo6UeBVxxv5JFyCay0aKd_'
# # То, с каким именем будет выведен мой файл
# output = 'Testing.xlsx'
# gdown.download(url, output, quiet=False)
workbook = xlsxwriter.Workbook('Testing.xlsx')
# Просто формат, красящий клетку в рандомний цвет
color = ("#"+''.join(random.choice('0123456789ABCDEF') for j in range(6))
             for i in range(1))
color_str = ''.join(color)
rand_cell_col = workbook.add_format()
rand_cell_col.set_bg_color(color_str)


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
        worksheet.write_column(i, randrange(10), [random.randint(1, 100)], rand_cell_col)
    workbook.close()

file1 = gdrive.CreateFile({'title':'Testing.xlsx'})
file1.SetContentFile('Testing.xlsx')
file1.Upload()
