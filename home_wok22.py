# # class Dog:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# # my_dog = Dog(name= 'Koltik', age= 9)
# # print(f'name {my_dog.name}, age {my_dog.age}')
# #
# # mother_dog = Dog(name= 'Yta', age= 4)
# # print(f'name {mother_dog.name}, age {mother_dog.age}')
#
# class Auto:
#     def __init__(self, brand, year, model):
#         self.brand = brand
#         self.year = year
#         self.model = model
#
# my_auto = Auto(brand = 'Mitsubishi', year = 2008, model = 'Evo 9')
# print(f'name {my_auto.brand}, model {my_auto.model}, age {my_auto.year} ')
#
#
#—------------------------------- Задача —--------------------------------#
# Санта отправляется разносить подарки по домам.
# У него есть определенная энергия, которая тратится при каждом передвижении и доставке подарков.
# Создайте класс Santa, представляющий самого Санту. У него должен быть показатель энергии (energy),
# который уменьшается при каждом передвижении.
# Реализуйте методы:
# move(distance): Уменьшает уровень энергии Санты на основании расстояния, которое он перемещается.
# deliver_gifts(houses): Принимает список домов (houses) и уменьшает уровень энергии
# в зависимости от количества доставленных подарков.
# Добавьте возможность увеличения энергии, например, метод rest(), который будет увеличивать энергию Санты после отдыха.

