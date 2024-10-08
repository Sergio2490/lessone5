
# Определите класс "Account", имитирующий банковский счет. Класс должен включать атрибуты для хранения
# идентификатора владельца, баланса счета и методы для депозите (пополнения) и снятия средств,
# если на счете достаточно средств

class Account():
    def __init__(self, id, balance):  #ф-ция инициализации объекта класса со всеми хар-ми (атрибутами)
        self.id = id   #прописываем, что эти атрибуты принадлежат именно данному классу
        self.balance = balance

    def deposit(self, money):   #пополнение,  money - аргумент, это сумма, на которую пополняем счет
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на Вашем счете - {self.balance}")

    def withdraw(self, money):    #снятие
        if money > self.balance :
            print(f"Недостаточно средств на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")
    def all_balance(self):
        print(f"Текущий баланс - {self.balance} рублей")

#Класс готов.
man = Account("1233322", 600)
man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)


