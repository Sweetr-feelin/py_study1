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
