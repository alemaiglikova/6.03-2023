import os
import random

folders = ['folder1', 'folder2', 'folder3', 'folder4']

for folder in folders:

    files = os.listdir(folder)
    file = random.choice(files)

    if file == 'мусор.json':

        os.remove(os.path.join(folder, file))
        print(f"Файл {file} удален из папки {folder}")
    else:
        print(f"Файл {file} не является мусорным в папке {folder}")