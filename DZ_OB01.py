#Управление задачами
#атрибуты: описание задачи, срок выполнения и статус(выполнено / не  выполнено).
#Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка
#текущих (не выполненных) задач.
class Task:
    def __init__(self, name, date_end, status=False):  #инициируем атрибуты
        self.name = name  #описание задачи
        self.date_end = date_end   #Срок выполнения
        self.status = status   #Статус - вып или не вып.

    #Определим функции

    def mark_end(self):  # Отметка о выполнении з-чи
        self.status = True

     def is_completed(self):  #Проверка статуса
         return self.status

    def add_task(self, task_name, task_date):  #добавление новой задачи
        self.name = task_name
        self.date_end = task_date  #Дата, до которой нужно исполнить
        self.status = False



    def list_true_tasks(self):  #Вывод невыполненных задач
        if self.status == False:
            print(self.name)


