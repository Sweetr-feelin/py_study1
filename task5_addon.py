#По входным атрибутам выдается описание задачи
class Task_info:
    
    def __init__(self, number, name):
        self.number = str(number)
        self.name = name
    
    def task_info(self):
        return "Номер: " + self.number + ". Описание: " + self.name + "."

class Backlog:
    task_quantt: int
    backlog: list
    
    def __init__(self, task_quantt):
        self.task_quantt: float = task_quantt
        self.backlog = []
    
    #Эмуляция создания бэклога
    def bl_creation_emul(self):
        for i in range(1, self.task_quantt + 1):
            descr = "Задача " + str(i)
            self.task = Task_info(i, descr)
            self.backlog.append(self.task)
        return self.backlog
        
    #Показывает часть бэклога - сколько запрошено
    def bl_show(self, number_to_show, backlog):
        if self.task_quantt >= number_to_show:
            for i in range(number_to_show):
                result = "Номер: " + backlog[i].number + ". Описание: " + backlog[i].name + "."
                print(result)
        else:
            print("В наличии только", self.task_quantt, " задач.")
            print("Укажите меньшее количество")

print("Требуемые типы для работы с Backlog")
print(Backlog.__annotations__)

backlog = Backlog(6)
bl = backlog.bl_creation_emul()
backlog.bl_show(int(input("Сколько отобразить задач? - ")), bl)
