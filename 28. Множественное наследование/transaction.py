# 	Transaction (Транзакция):
# ●	Свойства: дата, тип (выдача/возврат), книга, пользователь.
# ●	Методы: запись транзакции, вывод информации о транзакции.

from datetime import date


class Transaction:
    def __init__(self):
        self.data = ''
        self.status = ''
        self.book = ''
        self.user = ''

    def write_transaction(self, status, user, book):
        self.data = date.today()
        self.status = status
        self.book = book
        self.user = user

    def show_transaction(self):
        print(f'Дата: {self.data} | Статус: {self.status} | Книга: {self.book} | Пользователь: {self.user}.')


