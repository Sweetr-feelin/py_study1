4.1.
class Weapon:
    def __init__(self, nam, weight, range):
        self.name = nam # название
        self.weight = weight # вес
        self.range = range # дистанция нанесения урона
    
    def damage(self, dist):
        if dist <= self.range:
            if self.type == "firearms":
                self.ammo -= 1
                return print('Огнестрельный урон от оружия', self.name, 'равен', self.firepower)
            else:
                return print('Урон холодного оружия', self.name, 'равен', self.sharpness)
        return 0

class firearms(Weapon):
    
    def __init__(self, nam, weight, range, type, ammo, power):
        super().__init__(nam, weight, range)
        self.type = "firearms"
        self.ammo = ammo # количество зарядов
        self.firepower = power # урон от огнестрела

class cold_weapon(Weapon):
    
    def __init__(self, nam, weight, range, type, points):
        super().__init__(nam, weight, range)
        self.type = "cold_weapon"
        self.sharpness = points # урон от хол. оружия

pistol = firearms("Пистолет", 2, 10, firearms, 14, 5)
pistol.damage(5)

knife = cold_weapon("Нож", 1, 1, cold_weapon, 3)
knife.damage(1)

---

"""
4.2. Теория своими словами
Полиморфизм подтипов: разные классы содержат полностью одинаковые методы

Ad hoc полиморфизм: один объект класса содержит методы с одинаковыми названиями но разным набором параметров
(или с одинаковым набором параметров, которые различаются по типам данных)

Параметрический полиморфизм: один метод (с одним набором параметров соответственно) может обрабатывать на входе параметры разных типов

В представленном примере присутствуют разные классы (Cat и Bird), в которых есть методы с одинаковыми названиями (foo) и входными параметрами
(полиморфизм подтипов),но разной обработкой, и осуществляется обращение к методу (do_something_with_animal) с подачей на вход 
параметров разных типов/классов (параметрический полиморфизм)
"""

---

4.3. Первая часть задания
class Warrior: # воин

    def __init__(self, nam):
        self._name = nam # имя

    def foo(self):
        return print("Warrior")

class Dwarf(Warrior): # дварф

    def __init__(self, nam):
        super().__init__(nam)
    
    def foo(self):
        return print("Dwarf")

class Elf(Warrior): # эльф
    def __init__(self, nam):
        super().__init__(nam)
    
    def foo(self):
        return print("Elf")

warrior1 = Warrior("warrior1")
warrior1.foo()

warrior2 = Dwarf("warrior2")
warrior2.foo()

warrior3 = Elf("warrior3")
warrior3.foo()

---

4.3. Вторая часть задания
import random

class Warrior: # воин

    def __init__(self, nam):
        self._name = nam # имя

    def foo(self):
        return print("Warrior")

class Dwarf(Warrior): # дварф

    def __init__(self, nam):
        super().__init__(nam)
    
    def foo(self):
        return print("Dwarf")

class Elf(Warrior): # эльф
    def __init__(self, nam):
        super().__init__(nam)
    
    def foo(self):
        return print("Elf")


list = []
n = 500
for i in range(n):
    name_num = random.randint(1,500)
    name = "warrior" + str(name_num)
    if name_num % 2 == 0:
        warrior = Dwarf(name)
    else:
        warrior = Elf(name)
    list.append(warrior)
    list[i].foo()

---

4.3. Вторая часть задания - вариант с добавлением типизации:

import random

class Warrior:  # воин

    def __init__(self, nam: str):
        self._name = nam  # имя

    def foo(self) -> str:
        return "Warrior"

class Dwarf(Warrior):  # дварф

    def __init__(self, nam):
        super().__init__(nam)

    def foo(self) -> str:
        return "Dwarf"

class Elf(Warrior):  # эльф
    def __init__(self, nam):
        super().__init__(nam)

    def foo(self) -> str:
        return "Elf"


lst: list = []
n: int = 50
for i in range(n):
    name_num: int = random.randint(1, 500)
    name: str = "warrior" + str(name_num)
    if name_num % 2 == 0:
        warrior: Dwarf = Dwarf(name)
    else:
        warrior: Elf = Elf(name)
    lst.append(warrior)
    print(lst[i].foo())

---

4.3. Вторая часть задания - обновленный вариант:

import random

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def do_something_with_animal(animal: Animal):
    animal.foo()

cat = Cat()
bird = Bird()
lst = [cat, bird]

def animals(l: list):
    l.clear()
    n = 500
    for i in range(n):
        num = random.randint(1, 500)
        if num % 2 == 0:
            animal = Cat()
        else:
            animal = Bird()
        l.append(animal)
    return l

animals(lst)
for j in range(10):
    do_something_with_animal(lst[j])

"""
Почему получился такой вывод?
Разные элементы списка - это разные объекты разных классов, содержащие методы с одинаковыми названиями и набором параметров.
Получается, что обращение к разным элементам списка за выполнением якобы одного метода выдает разные результаты.
"""
