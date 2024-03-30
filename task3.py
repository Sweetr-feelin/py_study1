class Weapon:
    def __init__(self, weapon_ammo, weapon_weight):
        self.ammo = weapon_ammo
        self.weight = weapon_weight
        self.health = 100
        
    def Shoot(self):
        self.ammo -= 1
        self.weight -= 0.1
        self.health -= 1.5
    
    def Reload(self,):
        self.ammo += 1
        self.weight += 0.1
    
    def Clean(self,):
        self.health += 1.5

rifle = Weapon(42, 10)
print("Начальные параметры: ")
print("Количество патронов: ", rifle.ammo)
print("Вес оружия: ", rifle.weight)
print("Загрязненность оружия: ", rifle.health)

shooting_count = int(input("Сколько патронов отстреляли? - "))

for i in range(shooting_count):
    rifle.Shoot()
print("Остаток патронов после стрельбы: ", rifle.ammo)
print("Вес после стрельбы: ", rifle.weight)
print("Загрязненность оружия после стрельбы: ", rifle.health)

for i in range(shooting_count):
    rifle.Reload()
    rifle.Clean()
print("Конечные параметры: ")
print("Количество патронов: ", rifle.ammo)
print("Вес оружия: ", rifle.weight)
print("Загрязненность оружия: ", rifle.health)

---

class Dwarf:
    def __init__(self, dwarf_power, dwarf_health):
        self.power = dwarf_power
        self.health = dwarf_health
        
    def Work(self):
        self.power -= 5
        self.health -= 5
    
    def Drink(self,):
        self.health -= 40
    
    def Rest(self,):
        self.power += 5
        self.health += 10

dwarf1 = Dwarf(40, 100)
working_hours = int(input("Сколько часов работал дворф? - "))

for i in range(working_hours):
    dwarf1.Work()
print("Сколько сил осталось у дворфа после работы? - ", dwarf1.power, dwarf1.health)

dwarf1.Drink()
print("Как себя чувствовал дворф после бара? - ", dwarf1.health)

for i in range(8):
    dwarf1.Rest()
    
print("Как себя чувствовал дворф после отдыха? - ", dwarf1.power, dwarf1.health)
