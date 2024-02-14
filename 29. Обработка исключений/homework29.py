# Реализуйте систему банковских счетов с использованием наследования.
# Базовый класс "Счет", а затем подклассы, представляющие "Текущий счет", "Сберегательный счет" и "Кредитный счет".
# Реализуйте методы для внесения и снятия средств.

from abc import ABC, abstractmethod
from class_error import *


class Account(ABC):
    @abstractmethod
    def cash_withdrawal(self, take_money):
        print('Снятие')

    @abstractmethod
    def cash_deposit(self, add_money: float):
        print('Пополнение')


class ActualAccount(Account):
    def __init__(self):
        self.money = 0
        print(f'Ваш счет создан | Баланс: {self.money}')

    def view_the_balance(self):
        print(f'Баланс текущего счета: {self.money}')

    def cash_withdrawal(self, take_money):
        if self.money < take_money:
            raise NotEnoughMoney
        if take_money < 0:
            raise NotPositiveSumm
        else:
            self.money = self.money - take_money
            print(f'Снятие {take_money}. Вывод средств выполнен.')

    def cash_deposit(self, add_money: float):
        if add_money < 0:
            raise NotPositiveSumm

        profit = self.money + add_money
        print(f'Пополнение на {add_money}. Внесение средств выполнено.\nБаланс счета: {profit}')
        self.money = profit


class SavingsAccount(Account):
    def __init__(self, year: int, money: float = 0):
        self.year = year
        self.money = money

        if self.money < 0:
            raise NotPositiveSumm

        if self.year <= 0:
            raise NotPositiveYear

        print(f'Ваш сберегательный счет создан. Баланс: {self.money} | Срок: {self.year}')

    def view_the_balance(self, later_year):
        if later_year < 0:
            raise NotPositiveYear
        elif later_year == 0:
            print(self.money)
        elif later_year > self.year:
            raise BigYear
        else:
            self.money = self.money * ((1 + 0.15) ** later_year)
            print(f'Баланс сберегательного счета через {later_year} год(а): {self.money}')
            return self.money

    def cash_deposit(self, add_money: float):
        if add_money < 0:
            raise NotPositiveSumm
        else:
            year = float(input('Сколько прошло лет с первого взноса? _____'))
            self.money = self.money * ((1 + 0.15) ** year)
            self.money += add_money
            print(f'Баланс {self.money} | Внесение {add_money} | Остаток: {self.money}')

    def cash_withdrawal(self, take_money: float, year: int):
        if year < self.year and year > 0:
            raise LittleYear
        elif year <= 0:
            raise NotPositiveYear
        elif year > self.year:
            raise BigYear
        else:
            if take_money > self.money:
                raise NotEnoughMoney
            elif take_money < 0:
                raise NotPositiveSumm
            elif take_money <= self.money:
                self.money = self.money - take_money
                print(f'Перевод на сумму {take_money} завершен. Остаток на сберегательном счете: {self.money}')


def line():
    print('________________________________________________________________')


alfa = ActualAccount()
line()

# ---------------------------------------- Ошибка Введите отрицательное число -----------------------------------------
cash = float(input('Введите сумму пополнения: _____'))
while cash < 0:
    try:
        alfa.cash_deposit(cash)
    except NotPositiveSumm:
        print(f'-*-*-*- {NotPositiveSumm()} -*-*-*-')
        cash = float(input('Введите сумму пополнения: _____'))

alfa.cash_deposit(cash)
line()


# ------------------------ Ошибка Введите сумму для снятия больше баланса/отрицательное число -------------------------
cash = float(input('Введите сумму для снятия: _____'))
while cash > alfa.money or cash < 0:
    try:
        alfa.cash_withdrawal(cash)
    except NotEnoughMoney:
        print(f'-*-*-*- {NotEnoughMoney()} -*-*-*-')
        cash = float(input('Введите сумму для снятия: _____'))
    except NotPositiveSumm:
        print(f'-*-*-*- {NotPositiveSumm()} -*-*-*-')
        cash = float(input('Введите сумму для снятия: _____'))

alfa.cash_withdrawal(cash)
alfa.view_the_balance()
line()


# ------------------------ Ошибка Введите сумму и год для сберегательного счета отрицательными/0 -----------------------
year_save = int(input('На сколько лет открыть сберегательный счет? ____'))
money_save = float(input('Взнос? _____'))
while year_save <= 0 or money_save < 0:
    try:
        SavingsAccount(year_save, money_save)
    except NotPositiveSumm:
        print(f'-*-*-*- {NotPositiveSumm()} -*-*-*-')
        money_save = float(input('Взнос? _____'))
    except NotPositiveYear:
        print(f'-*-*-*- {NotPositiveYear()} -*-*-*-')
        year_save = int(input('На сколько лет открыть сберегательный счет? ____'))

save = SavingsAccount(year_save, money_save)
line()

# ------------------------ Ошибка Введите год, чтобы посмотреть баланс, отрицательными/0 ----------------------------
print('Посмотреть состояние счета на определенное время.')
year_save_later = int(input('Сколько прошло с открытия счета?'))

while year_save_later < 0 or year_save_later > year_save:
    try:
        save.view_the_balance(year_save_later)
    except NotPositiveYear:
        print(f'-*-*-*- {NotPositiveYear()} -*-*-*-')
        year_save_later = int(input('Сколько прошло с открытия счета?'))
    except BigYear:
        print(f'-*-*-*- {BigYear()} -*-*-*-')
        year_save_later = int(input('Сколько прошло с открытия счета?'))

save.view_the_balance(year_save_later)
line()

# ----------------------- Ошибка Введите год меньше срока\отрицательный год\сумму отрицательную ------------------------
take_money_save = float(input('Сколько нужно снять? _____'))
take_year_save = int(input('Сколько прошло лет? _____'))
while take_money_save < 0 or take_money_save > save.money or take_year_save > save.year or take_year_save < save.year or take_year_save <= 0:
    try:
        save.cash_withdrawal(take_money_save, take_year_save)
    except NotEnoughMoney:
        print(f'-*-*-*- {NotEnoughMoney()} -*-*-*-')
        take_money_save = float(input('Сколько нужно снять? _____'))
    except NotPositiveSumm:
        print(f'-*-*-*- {NotPositiveSumm()} -*-*-*-')
        take_money_save = float(input('Сколько нужно снять? _____'))
    except NotPositiveYear:
        print(f'-*-*-*- {NotPositiveYear()} -*-*-*-')
        take_year_save = int(input('Сколько прошло лет? _____'))
    except LittleYear:
        print(f'-*-*-*- {LittleYear()} -*-*-*-')
        take_year_save = int(input('Сколько прошло лет? _____'))
    except BigYear:
        print(f'-*-*-*- {BigYear()} -*-*-*-')
        take_year_save = int(input('Сколько прошло лет? _____'))

save.cash_withdrawal(take_money_save, take_year_save)


