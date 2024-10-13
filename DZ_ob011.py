class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):  #Отметка задачи как выполненная
        self.completed = True

    def is_completed(self):   #Проверка статуса задачи
        return self.completed

    def __str__(self):  #Возвращает строковое представление задачи
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

    @staticmethod
    def add_task(tasks, description, deadline):  #добавление новой задачи в список задач
        task = Task(description, deadline)  #создаем экземпляр класса
        tasks.append(task)

    @staticmethod
    def get_pending_tasks(tasks):   #Вывод невыполненных задач
        return [task for task in tasks if not task.completed]

# Пример использования:
tasks = []

Task.add_task(tasks, "Закончить изучение темы по классам в Python", "13.10.2024")
Task.add_task(tasks, "Купить обувь", "20.10.2024")
Task.add_task(tasks, "Пройти тему 5 по английскому", "31.10.2024")

# Отметить первую задачу как выполненную
tasks[0].mark_complete()

# Вывести список всех задач
print("Все задачи:")
for task in tasks:
    print(task)

# Вывести список текущих (не выполненных) задач
print("\nТекущие задачи:")
for task in Task.get_pending_tasks(tasks):
    print(task)