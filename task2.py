1.1. 
1. Видеохостинг YouTube
Может быть класс "Видео" с переменными:
Наименование
Описание
Ссылка на файл
Размер файла

2. Мессенджер
Может быть класс "Сообщение" с переменными:
Текст сообщения
Время отправки
Время доставки
Время прочтения
Имя отправителя
Имя получателя

1.2.
class Dwarf:
    name = "Гимли" # Имя
    age = 0 # возраст, полных лет
    power = 40 # уровень силы
    health = 100 # уровень здоровья
    stamina = 80 # предел выносливости
    
class Weapon:
    name = "Винтовка" # наименование
    weight = 10 # вес
    firepower = 14 # уровень огневой силы
    health = 100 # уровень повреждений
    ammo = 42 # количество патронов
    
class Animal:
    name = "Тузик" # Имя
    binomial = 0 # возраст, полных лет
    power = 10 # уровень силы
    health = 100 # уровень здоровья
    stamina = 120 # предел выносливости

dwarf1 = Dwarf()
dwarf1.age = 120

dwarf2 = Dwarf()
dwarf2.name = "Torin"

dwarf3 = Dwarf()
dwarf3.stamina = 0

weapon = Weapon()
weapon.weight = 300

animal = Animal()
animal.power = 1000

1.3.
class Weapon:
    name = "Винтовка" # наименование
    weight = 10 # вес
    firepower = 14 # уровень огневой силы
    health = 100 # уровень повреждений
    ammo = 42 # количество патронов
    
class Animal:
    name = "Тузик" # Имя
    binomial = 0 # возраст, полных лет
    power = 10 # уровень силы
    health = 100 # уровень здоровья
    stamina = 120 # предел выносливости

animal = Animal()
animal.power = 1000

weapon = Weapon()
weapon = animal
