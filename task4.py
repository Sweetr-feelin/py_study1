class Weapon:
    def __init__(self, ammo, weight, health):
        self.__ammo = ammo
        self.__weight = weight
        self.__health = health
        
    def Load(self, ammo, weight, health):
        self.__ammo = ammo
        self.__weight = weight
        self.__health = health
    
    def Count_ammo(self):
        return self.__ammo
    
    def Count_weight(self):
        return self.__weight

    def Define_health(self):
        return self.__health
    
    def Shoot(self):
        self.__ammo -= 1
        self.__weight -= 0.1
        self.__health -= 1.5
    
    def Reload(self,):
        self.__ammo += 1
        self.__weight += 0.1
    
    def Clean(self,):
        self.__health += 1.5

rifle = Weapon(0, 0, 100)
rifle.Load(42, 10, 100)
print("Начальные параметры: ")
print("Количество патронов: ", rifle.Count_ammo())
print("Вес оружия: ", rifle.Count_weight())
print("Загрязненность оружия: ", rifle.Define_health())

shooting_count = int(input("Сколько патронов отстреляли? - "))

for i in range(shooting_count):
    rifle.Shoot()
print("Остаток патронов после стрельбы: ", rifle.Count_ammo())
print("Вес после стрельбы: ", rifle.Count_weight())
print("Загрязненность оружия после стрельбы: ", rifle.Define_health())

for i in range(shooting_count):
    rifle.Reload()
    rifle.Clean()
print("Конечные параметры: ")
print("Количество патронов: ", rifle.Count_ammo())
print("Вес оружия: ", rifle.Count_weight())
print("Загрязненность оружия: ", rifle.Define_health())

---

class Dwarf:
    def __init__(self, dwarf_power, dwarf_health):
        self.__power = dwarf_power
        self.__health = dwarf_health
    
    def Morning(self, dwarf_power, dwarf_health):
        self.__power = dwarf_power
        self.__health = dwarf_health
    
    def Define_power(self):
        return self.__power

    def Define_health(self):
        return self.__health
        
    def Work(self):
        self.__power -= 5
        self.__health -= 5
    
    def Drink(self,):
        self.__health -= 40
    
    def Rest(self,):
        self.__power += 5
        self.__health += 10

dwarf1 = Dwarf(0, 0)
dwarf1.Morning(40, 100)
working_hours = int(input("Сколько часов работал дворф? - "))

for i in range(working_hours):
    dwarf1.Work()
print("Сколько сил осталось у дворфа после работы? - ", dwarf1.Define_power())

dwarf1.Drink()
print("Как себя чувствовал дворф после бара? - ", dwarf1.Define_health())

for i in range(8):
    dwarf1.Rest()
    
print("Как себя чувствовал дворф после отдыха? - ", dwarf1.Define_health())

---

class Weapon:
    def __init__(self, weight):
        self.weight = weight

class firearms(Weapon):
    
    def Load(self, ammo):
        self.ammo = ammo
    
    def Power(self, power):
        self.firepower = power

class cold_weapon(Weapon):
    
    def Sharpness(self, points):
        self.sharpness = points
    
    def Length(self, cm):
        self.length = cm

---

class Dwarf:
    def __init__(self, n):
        self.name = n

class Warrior(Dwarf):
    
    def Load(self, d):
        self.defense = d
    
    def Power(self, p):
        self.power = p

class Worker(Dwarf):
    
    def Health(self, hp):
        self.health = hp
    
    def Stamina(self, s):
        self.stamina = s
