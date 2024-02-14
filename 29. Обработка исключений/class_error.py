class NotString(Exception):
    def __str__(self):
        return f'Сумма не может быть строкой.'


class NotPositiveSumm(Exception):
    def __str__(self):
        return f'Сумма должна быть положительная.'


class NotPositiveYear(Exception):
    def __str__(self):
        return f'Год не может быть равен 0 или быть отрицательным числом.'


class BigYear(Exception):
    def __str__(self):
        return f'Указанный год превышает срока сберегательного счета.'


class NotEnoughMoney(Exception):
    def __str__(self):
        return f'Недостаточно средств для снятия.'


class LittleYear(Exception):
    def __str__(self):
        return f'Вы пытаетесь вывести средства раньше времени.'




