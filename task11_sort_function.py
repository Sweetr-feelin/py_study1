def sort_massive(n, min, max):
    # Ввод данных
    import random
    x = []
    changes = True
    # Создание списка
    for i in range(n):
        x.append(random.randint(min, max))
    # Определение результата
    while changes == True:
        changes = False
        for j in range(n - 1):
            if x[j] > x[j + 1]:
                y = x[j]
                x[j] = x[j + 1]
                x[j + 1] = y
                changes = True
    # Вывод результата
    return x

sort10massive(10,-25,25)
