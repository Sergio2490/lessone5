class Warrior():
    def __init__(self, name, power, endurance, hair_color):   #init - спец метод,ф-ция создания нашего объекта класса - воина.self - обяз.пар-тр, указывает, что мы создаем ф-ция для себя, конкретно для этого класса
        self.name = name    # в def(name,...) - передаем информацию
        self.power = power  #чтобы хар-ки стали хар-ками именно этого класса, мы д.обозначить, что они к нему принадлежат
        self.endurance = endurance # в этих 4-х строках - создаем характеристику персонажа
        self.hair_color = hair_color

    def sleep(self):   # Создаем МЕТОД СПАТЬ. Класс м создать и без init, если нет хар-к, а есть только функци
        print(f"{self.name} лег спать")
        self.endurance += 2  #пока спит - добавляется 2 очка выносливости.

    def eat(self): #метод КУШАТЬ
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):    #метод БИТЬ
        print(f"{self.name} бьет кого-то")
        self.endurance -= 6

    def walk(self):    #метод ХОДИТЬ
        print(f"{self.name} гуляет")  #не изменяем атрибуты при этом

    def info(self):   #метод выводит всю инф-ю о персонаже
        print(f"Имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")  #это мы создали лишь пустой шаблон - name, self.name и т.д. Это как форма с полуми. куда нужно что-то вписать

#создадим объект класса. Сначала - созд переменную, к-я б. хранить в себе объект данного класса
war1 = Warrior("Степа", 76, 54, 'коричневый')
war2 = Warrior("Егор", 45, 23, "блонд")
#print(war1.name) # через точку - прописываем хар-ки объекта
#print(war2.power)    #ранее здесь при описании класса, здесь писали self -то, что атрибут относится
#print(war2.endurance)  #к данному классу. Здесь же указываем конкретный объект war1, а уже через
#print(war2.hair_color) #него ссылаемся на наш класс

#print(war2.endurance)  #23  проверим выносливость, тк сон увелич ее на 2
#print(war2.power)   #45

#war2.sleep()   #Егор лег спать
#war2.eat()     #Егор сел кушать

#print(war2.endurance)   #выносл была 23 Егор лег спать 25 - стала
#print(war2.power) # сила была 45, после еды стала 46
war1.sleep()  #задействуем все методы класса обоих воинов
war1.eat()
war1.hit()
war1.walk()
war1.info()

war2.sleep()  #задействуем все методы Егора
war2.eat()
war2.hit()
war2.walk()
war2.info()
