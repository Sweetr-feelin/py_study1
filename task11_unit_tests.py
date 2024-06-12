# Первая версия сортировки:
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

sort_massive(10,-25,25)

# Первая версия тестов:
import unittest
from sort_massive import sort_massive

class sort_massive_TestCases(unittest.TestCase):

    def test_small_positive(self):  # Малый диапазон положительных целых чисел
        n = 10
        min = 1
        max = 10
        x = sort_massive(n, min, max)
        for i in range(n-1):
            self.assertLessEqual(x[i], x[i+1])

    def test_small_negative(self):  # Малый диапазон положительных и отрицательных целых чисел, включая "0"
        n = 10
        min = -3
        max = 3
        x = sort_massive(n, min, max)
        for i in range(n-1):
            self.assertLessEqual(x[i], x[i+1])

    def test_great_negative(self):  # Большой диапазон положительных и отрицательных целых чисел, включая "0"
        n = 50000
        min = -10000
        max = 10000
        x = sort_massive(n, min, max)
        for i in range(n-1):
            self.assertLessEqual(x[i], x[i+1])

    def test_float(self):  # Ввод дробного числа в качестве параметра
        n = 10.1
        min = -3
        max = 3
        x = sort_massive(n, min, max)
        for i in range(n-1):
            self.assertLessEqual(x[i], x[i+1])

if __name__ == '__main__':
    unittest.main()

# Вторая версия сортировки:
import random

n = 10
x = []
min = 1
max = 10
for i in range(n):
    x.append(random.randint(min, max))

def other_sort_massive(n, x):
    changes = True
    while changes == True:
        changes = False
        for j in range(n - 1):
            if x[j] > x[j + 1]:
                y = x[j]
                x[j] = x[j + 1]
                x[j + 1] = y
                changes = True
    return x

other_sort_massive(n, x)

# Вторая версия тестов:
import unittest
from other_sort_massive import other_sort_massive
import random

class other_sort_massive_TestCases(unittest.TestCase):

    def createNsort_lsts(self, n, min, max):
        lst1 = []
        lst2 = []
        for i in range(n):
            x = random.randint(min, max)
            lst1.append(x)
            lst2.append(x)
        other_sort_massive(n, lst1)
        lst2.sort()
        return lst1, lst2

    def test_small_positive(self):  # Малый диапазон положительных целых чисел
        n = 10
        min = 1
        max = 10
        self.createNsort_lsts(n, min, max)
        self.assertEqual(self.createNsort_lsts, self.createNsort_lsts)


    def test_small_negative(self):  # Малый диапазон положительных и отрицательных целых чисел, включая "0"
        n = 10
        min = -3
        max = 3
        self.createNsort_lsts(n, min, max)
        self.assertEqual(self.createNsort_lsts, self.createNsort_lsts)

    def test_great_negative(self):  # Большой диапазон положительных и отрицательных целых чисел, включая "0"
        n = 5000
        min = -10000
        max = 10000
        self.createNsort_lsts(n, min, max)
        self.assertEqual(self.createNsort_lsts, self.createNsort_lsts)

    def test_float(self):  # Ввод дробного числа в качестве параметра
        n = 10.1
        min = -3
        max = 3
        self.createNsort_lsts(n, min, max)
        self.assertEqual(self.createNsort_lsts, self.createNsort_lsts)

if __name__ == '__main__':
    unittest.main()
