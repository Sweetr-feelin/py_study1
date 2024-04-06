4.2. Первая часть задания
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

Вторая часть задания
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
n = 10
for i in range(n):
    name_num = random.randint(1,10)
    name = "warrior" + str(name_num)
    if name_num % 2 == 0:
        warrior = Dwarf(name)
    else:
        warrior = Elf(name)
    list.append(warrior)
    list[i].foo()
