from random import randint

def read2f_n_count(n):
    if n <= 0:
        return print('Выбрано меньше одного файла')
    else:
        for i in range(1, n + 1):
            x = randint(1, 10)
            print(x)
            name = str(x) + '.txt'

            try:
                fi = open(name, 'rt')
                sum = 0
                s = fi.readline()

                while s != '':
                    try:
                        s = int(s)
                    except:
                        sum = 0
                        print('Неверный формат данных')
                        break
                    sum += s
                    s = fi.readline()
                fi.close()
            except:
                print('Неизвестная ошибка')
                fi.close()

            if sum == 0:
                return print('Получение целевого результата невозможно')
        return print('Сумма чисел в двух файлах равна: ', sum)
