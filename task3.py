import csv

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

text_input = input().lower()

while text_input != '0':
    for row in data:
        if text_input in row[1].lower():
            print(f'У {row[1]} найдена песня: {row[2]}')
            break
    else:
        print('К сожалению, ничего не удалось найти. ')
    text_input = input().lower()