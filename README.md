    Обучение проходит в рамках "Высшей Школы Программирования Сергея Бобровского" (https://skillsmart.ru/ama/ky/)

### 1.2. Вспомогательный курс: Основы объектно-ориентированного программирования, тестирование, простые технологии (программная работа с файлами, архивами, изображениями...)

Задания 1-5, и работа надо ошибками в задании 6, выполнялись в Python Tutor (https://pythontutor.com/visualize.html#mode=edit).
Файлы с решениями находятся в репозитории (https://github.com/Sweetr-feelin/py_study1/tree/main)
---
Отчет об ознакомлении с утилитой "Файловый менеджер Far" представлен в виде изображений task7_image1.png и task7_image2.png
---
Отчет о промежуточном задании по настройке Линукс:
* 1. Поставил виртуальную среду VirtualBox (task9_VBmanager.png) и создал на ней место под Ubuntu, но запустить ее так и не смог - не разобрался пока что, почему не запускается.
  2. Запустил встроенную в windows версию Ubuntu (task9_ubuntu_console.png)
  3. Поставил midnight commander (task9_mc.png)
  4. Запустил на встроенной Ubuntu проверку заданий с пакетами через mc (task9_test_packages.png)
---
Задание 10 - отладка и логгирование:
* 1. Первая часть выложена в проекте (https://github.com/Sweetr-feelin/py_study1/blob/main/task10.1.py)
  2. Вторая часть в виде скриншотов предоставлена файлами "task10.2_debug1.png" и "task10.2_debug2.png"
 ---
Задание 11 - тестирование:
* 1. алгоритм сортировки, который делали на предыдущем (нулевом) курсе, оформил в виде функции и выложил в файл - https://github.com/Sweetr-feelin/py_study1/blob/main/task11_sort_function.py
  2. юнит тесты для функции сортировки приложил в файле https://github.com/Sweetr-feelin/py_study1/blob/main/task11_unit_tests.py (тест "test_great_negative" выполняется несколько минут, но работает)
---
Задание 12 - работа с файлами:
* 1. task13_cat_n_files_task1.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task13_cat_n_files_task1.py) - программа создаёт 10 файлов с именами 1.txt, 2.txt, ..., 10.txt, и в каждый записывает три случайных числа, каждое с новой строки
  2. task13_cat_n_files_task2.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task13_cat_n_files_task2.py) - функция, которая удаляет заданный каталог (возможно, непустой) и все файлы внутри него. Если внутри каталога есть подкаталоги, ничего удалять не надо. Функция возвращает флажок успешно/неудача
  3. task12_class_from_string.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task12_class_from_string.py) - программа, которая считывает из текстового файла строки, каждая из которых задаёт содержимое объекта некоторого класса.
---
Задание 13 - каталоги и файлы:
* 1. task13_create10tf.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task12_create10tf.py) - функция с тремя параметрами (путь к каталогу, расширение файла и булев флажок), которая возвращает список из двух списков имён: список всех файлов с заданным расширением в заданном каталоге (включая файлы из его подкаталогов одного уровня вложенности, если флажок = True), и список всех подкаталогов в заданном каталоге (включая подкаталоги одного уровня вложенности, если флажок = True)
  2. task13_read2f_n_count.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task12_read2f_n_count.py) - функция, которая получает на вход два случайных числа от 1 до 10 и путь к файлам, по этим числам открывает два соответствующих файла из задания выше, и возвращает сумму шести чисел (содержимое обоих файлов). Если содержимое любого файла неполно или испорчено, возвращайте информацию об ошибке
---
Задание 14 - работа с архивами:
* 1. task14_add_to_zip.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task14_add_to_zip.py) - функция, которая получает на вход два параметра: имя файла архива и расширение файла, сканирует текущий каталог в поисках файлов с подходящим расширением, и добавляет их в архив (исходно этот архив не существует).
---
Задание 15 - Обработка изображений:
* 1. task15_img_convert.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task15_img_convert.py) - программа, которая получает на вход два типа (расширения) графических форматов, находит в текущем каталоге все графические файлы, соответствующие первому расширению, и конвертирует их в графический формат по второму расширению.
  2. task15_img_convert_n_draw.py (https://github.com/Sweetr-feelin/py_study1/blob/main/task15_img_convert_n_draw.py) - Дополните предыдущую функцию рисованием в центре изображения  незаполненного квадрата, внутри которого будут написаны две строчки (вторая с новой строки).
---
