# class A:
#     def __init__(self):
#         self.__private_a = '__private_a'# Доступна для родительского класса
#         self._protected_a = '_protected_a'
#         self.public_a = 'public_a'
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print(self.public_a)
#         print(self._protected_a)
#         # print(self.__private_a) #AttributeError: 'B' object has no attribute '_B__private_a'
#
# b = B()
# print('--------------------------------')
# print(b.public_a)
# # print(b._protected_a)
# # print(b.__private_a)



# # --------------------------------- упаковка и распаковка данных -----------------------------
# def perimetr(*sides):
#     print(type(sides), sides)#sides -tuple
#     for side in sides:
#         print(side)
#
# perimetr(222,333,444) # 222,333,444 -> питон упаковал данные в tuple(222,333,444)
# print('-----------------------------')
# perimetr([222,333,444]) # [222,333,444] -> питон упаковал данные в tuple ([222,...])
# print('-----------------------------')
# perimetr(*[222,333,444])# *[222,333,444]-> 222,333,444  - распаковка

#
class ZeroDenominator(Exception): # Exception == Исключения == Ошибка в момент выполнения программы
    '''Исключение нулевого знаменателя'''
    def __str__(self):
        return f'denominator не должен быть равен 0'

class Fraction: #дробь обыкновенная
    def __init__(self, numerator, denominator): # numerator - числитель # denominator - знаменатель
        if denominator == 0:
            raise ZeroDenominator # обращение к классу ZeroDenominator
        self.numerator = numerator
        self.denominator = denominator

try:
    fraction = Fraction(1, 0)
except ZeroDenominator:
    # попросить пользователя переопределить делитель и т.д.\
    print(ZeroDenominator())
# try:
#     print(6/0)
# except ZeroDivisionError:
#     # попросить пользователя переопределить делитель и т.д.
#     print('деление на ноль плохо')