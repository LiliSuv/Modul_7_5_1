import os
import time

directory = os.getcwd ()
for root, dirs, files in os.walk (directory):
    files = [f for f in os.listdir () if os.path.isfile (f)]
    for file in files:
        filepath = os.path.join (root,file)
        filetime = os.path.getmtime (filepath)
        formatted_time = time.strftime ("%d.%m.%Y %H:%M", time.localtime (filetime))
        filesize = os.path.getsize (filepath)
        parent_dir = os.path.dirname (filepath)
        print (f'{'_' * 80}\n '
            f'Обнаружен файл: {file},\n Путь: {filepath},\n '
            f'Размер: {filesize} байт,\n Время изменения: {formatted_time},\n '
            f'Родительская директория: {parent_dir}\n'
            f'{'_' * 80}')
