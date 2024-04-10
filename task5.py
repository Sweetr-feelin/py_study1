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