import os
from texttable import Texttable


def human_read_format(size):
    """Функция должна вернуть представление размера файла в приведенных величинах —
    байтах (Б), килобайтах (КБ), мегабайтах (МБ) и гигабайтах (ГБ).
    Учтите, что 1КБ = 1024Б, 1МБ = 1024КБ, а 1ГБ = 1024МБ.
    1024КБ — это уже 1МБ."""
    if size < 1024:
        return f'{round(size)}Б'
    elif 1024 <= size < 1024 ** 2:
        return f'{round(size / 1024)}КБ'
    elif 1024 ** 2 <= size < 1024 ** 3:
        return f'{round(size / (1024 ** 2))}МБ'
    return f'{round(size / (1024 ** 3))}ГБ'


# C:\Users\User\PycharmProjects\git_project1


path = input()
ans = {}
for i in os.listdir(path):  # файлы в этом каталоге
    try:
        full_path = os.path.join(path, i)
        if not os.path.isfile(full_path):
            size = 0
            for currentdir, dirs, files in os.walk(full_path):
                for file in files:
                    file_path = os.path.join(currentdir, file)
                    size += os.path.getsize(file_path)
            ans[i] = size
    except Exception as e:
        pass

keys = ans.keys()
values = list(ans.values())
values.sort(key=lambda x: -x)
was = []
i = 1
table = Texttable()
table.add_row(['номер', 'имя каталога', 'размер'])
for x in values[0:min(10, len(values))]:
    for item in ans:
        val = ans[item]
        if x == val and item not in was:
            table.add_row([i, item, human_read_format(val)])
            was.append(item)
            i += 1
            break
print(table.draw())
