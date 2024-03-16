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
        data.append(row)

    return data

def writer(data):
    """
    Выводит строку типа : “<Название песни> - <артист> - <кол-во прослушиваний>”.
    для всех данных

    Параметры:
    data - список с информацией
    """

    for row in data:
        info = row[0].split(";")
        if int(info[3].split('.')[2]) <= 2002:
            print(f'{info[2]} - {info[1]} - {int(info[0])}')

def listing(data):
    """
    Добавляет кол-во прослушиваний для артистов

    Параметры:
    data  - list с информацией
    """
    new_data = []

    for row in data:
        Ln = 0
        Ls = 0
        dn = 0
        di = 0
        info = row[0].split(";")
        if int(info[0]) == 0:
            for x in info[1]:
                if x == ' ':
                    continue
                else:
                    Ln += 1
            for x in info[2]:
                if x == ' ':
                    continue
                else:
                    Ls += 1

            dn = 12+5*30 + 365*2023
            di = int(info[3].split('.')[0])+ int(info[3].split('.')[1])*30 + int(info[3].split('.')[2])*365
            tn = (int(abs((dn-di))/(Ls+Ln)*10000))
            info[0] = tn
            new_data.append(info)
        else:
            new_data.append(info)
    return new_data


data = read_file('songs.csv')
writer(data)
new_data = listing(data)

with open('songs_new.csv', "w", encoding="utf-8") as file:
    csv_write = csv.writer(file)
    csv_write.writerow(['streams','artist_name', 'track_name', 'date'])

    for row in new_data:
        csv_write.writerow(row)

