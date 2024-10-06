class Warrior():
    def __init__(self, name, power, endurance, hair_color):   #init - спец метод,ф-ция создания нашего объекта класса - воина.self - обяз.пар-тр, указывает, что мы создаем ф-ция для себя, конкретно для этого класса
        self.name = name    # в def(name,...) - передаем информацию
        self.power = power  #чтобы хар-ки стали хар-ками именно этого класса, мы д.обозначить, что они к нему принадлежат
        self.endurance = endurance # в этих 4-х строках - создаем характеристику персонажа
        self.hair_color = hair_color

    def sleep(selfself):   # Создаем МЕТОД СПАТЬ. Класс м создать и без init, если нет хар-к, а есть только функци
        print(f"{seff.name} лег спать")
        self.endurance += 2  #пока спит - добавляется 2 очка выносливости.

    def  eat(self): #метод КУШАТЬ
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):    #метод БИТЬ
        print(f"{self.name} бьет кого-то")
        self.endurance -+ 6

    def walk(self):    #метод ХОДИТЬ
        print(f"{self.name} гуляет")  #не изменяем атрибуты при этом

    def info(self):   #метод выводит всю инф-ю о персонаже
        print(f"Имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")  #это мы создали лишь пустой шаблон - name, self.name и т.д. Это как форма с полуми. куда нужно что-то вписать

