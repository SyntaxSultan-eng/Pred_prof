import csv
import string
def read_file(filename):
    '''
    Считывает файл и данные из него переносит в list

    Параметры:
    filename - название файла
    '''
    file = open(filename, encoding='utf-8')
    data = []

    csv_reader = csv.reader(file)
    header = True
    for row in csv_reader:
        if header:
            header = False
            continue
        info = row[0].split(";")
        data.append(info)

    return data

data = read_file('songs.csv')

russian_artists = set()

foreign_artists = set()

cyrillic_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for row in data:
    for text in row[1]:
        if text.lower() in cyrillic_letters:
            russian_artists.add(row[1])
            break
    else:
        foreign_artists.add(row[1])
print(russian_artists)
print(foreign_artists)
print(f'Количество российских исполнителей: {len(russian_artists)}')
print(f'Количество иностранных исполнителей: {len(foreign_artists)}')