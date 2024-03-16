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

def winners(data):
    '''
    Создает массив дат и сортирует их
    '''
    dates = []
    for row in data:
        dates.append(((int(row[3].split('.')[0]) + int(row[3].split('.')[1])*30 + int(row[3].split('.')[2])*365)))
    return Quick_sort(dates)

def Quick_sort(array):
    """
    Быстрая сортировка
    Параметры:
    array - список
    """
    if len(array)<=1:
        return array

    main = int(array[0])

    less = [int(x) for x in array[1:] if int(x) < main]
    higher = [int(x) for x in array[1:] if int(x) > main]

    return Quick_sort(less) + [main] + Quick_sort(higher)

data = read_file('songs.csv')

dates = winners(data)

i = 0
while True:
    flag = True
    for row in data:
        flag = False
        if int(row[3].split('.')[2]) == (dates[i]//365):
            print(f"{i+1} {row[2]}, {row[1]}, {row[3]}")
            i += 1
    if i == 5 or flag:
        break
