import os
import shutil

# Переименовывание файла(первый путь обязан быть полным, второй может быть относительным)
def Renaming(path, new_name):
    pozitiol_slash = -1
    pozitiol_dot = -1
    path = os.path.abspath(path)
    count = 0
    for i in path:
        if i == '\\':
            pozitiol_slash = count
        elif i == '.':
            pozitiol_dot = count
        count += 1
    new_path = path.replace(path[pozitiol_slash:len(
        path)], '\\' + new_name) + path[pozitiol_dot:len(path)]
    os.rename(path, new_path)

# Перемещение файла(можно указывать относительные пути)
def Path(old_path, new_path):
    old_path = os.path.abspath(old_path)
    new_path = os.path.abspath(new_path)
    os.rename(old_path, new_path)

# Копирование файла
def Copy_File(path, new_path):
    path = os.path.abspath(path)
    new_path = os.path.abspath(new_path)
    shutil.copyfile(path, new_path)

# Создание нового пути(путь указывается полный)
def New_Path(path):
    path = os.path.abspath(path)
    os.makedirs(path)

# Чтение файла по-строчно(передать объект в переменную)
def Read_Split_File(path):
    file = open(path, 'r', encoding='utf-8')
    list = []
    for i in file:  # чтение файла
        i = i.replace('\n', '')
        list.append(i)
    return list

# Удаление файла
def Delete_File(path):
    path = os.path.abspath(path)
    os.remove(path)

# Удаление папки со всем содержимым
def Delete_Folder(path):
    path = os.path.abspath(path)
    shutil.rmtree(path)



