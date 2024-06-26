# В код ниже добавил логгирование и assert'ы. Лог выводил в отдельный файл, содержимое в "task10.1.log".

import logging
logger = logging.getLogger(__name__)

class Weapon:
    def __init__(self, ammo, weight, health):
        self.__ammo = ammo
        self.__weight = weight
        self.__health = health

    def load(self, ammo, weight, health):
        self.__ammo = ammo
        self.__weight = weight
        self.__health = health

    def count_ammo(self):
        if self.__ammo == 0:
            logger.info('No ammo')
        return self.__ammo

    def count_weight(self):
        return self.__weight

    def define_health(self):
        if self.__health <= 15:
            logger.info('Low weapon health')
        return self.__health

    def shoot(self):
        assert self.__ammo > 0
        self.__ammo -= 1
        self.__weight -= 0.1
        self.__health -= 1.5
        assert self.__health > 0

def log_info():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    rifle.count_ammo()
    logger.info('Finished')

def log_warning():
    logging.basicConfig(filename='myapp.log', level=logging.WARNING)
    logger.info('Started')
    rifle.define_health()
    logger.info('Finished')

rifle = Weapon(0, 10, 100)
rifle.load(1, 10, 16)

log_info()
log_warning()

print("Начальные параметры: ")
print("Количество патронов: ", rifle.count_ammo())
print("Вес оружия: ", rifle.count_weight())
print("Загрязненность оружия: ", rifle.define_health())

shooting_count = int(input("Сколько патронов отстреляли? - "))

for i in range(shooting_count):
    rifle.shoot()

log_info()
log_warning()

print("Остаток патронов после стрельбы: ", rifle.count_ammo())
print("Вес после стрельбы: ", rifle.count_weight())
print("Загрязненность оружия после стрельбы: ", rifle.define_health())
