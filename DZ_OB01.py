#Управление задачами
атрибуты: описание задачи, срок выполнения и статус(выполнено / не  выполнено).
Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка
текущих (не выполненных) задач.
class Task:
    def __init__(self, name, date_end, status):  #инициируем атрибуты
        self.name = name  #описание задачи
        self.date_end = date_end   #Срок выполнения
        self.status = status   #Статус - вып или не вып.

    #Определим функции
    def add_task(self):  #добавление новой задачи
        self.name = input("Введите название новой задачи: ")
        self.date_end = input("Введите дату, до которой задачу нужно выполнить в формате ДД.ММ.ГГГГ: ")
        self.status = False
    def mark_end(self):  #Отметка о выполнении з-чи (или изменение статуса)
        if self.status == False:
            self.status = True
        elif self.status == True:
            self.status = False

    def list_true_tasks(self):  #Вывод невыполненных задач
        if self.status == False:
            print(self.name)


