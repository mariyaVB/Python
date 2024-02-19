from alchemy import *


def line():
    print('\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n')


while True:
    command = input('''
1 = Заглянуть в магазин 🏪
2 = Зайти в лабораторию 🧉
3 = Отправиться в сад 🌱
4 = Посмотреть что лежит в подсумке 💼
5 = Открыть Книгу Зельеварения 📖
                                                   
0 = Закончить игру
Выбор _____''')

    match command:
        case '0':
            break

        case '1':
            line()
            person.show_balance()
            shop = input('Купить = 1 | Продать = 2 | 0 = Выход\nВыбор _____')
            match shop:
                case '0':
                    pass

                case '1':
                    print('Витрина:')
                    plant = choice_plant(plant_shop)
                    if person.pay_plant(plant) is person.balance:
                        inventory.add_plant(plant)
                        print(f'Ваши семена {plant.plant_title} добавлены в инвентарь 👌')
                        person.show_balance()
                        line()

                case '2':
                    sell_potion = choice_potion(inventory.potion)
                    inventory.delete_potion(sell_potion)
                    person.sell_potion()
                    person.show_balance()

        case '2':
            line()
            cooking = input('Начнем варить зелье? 1 = Да 2 = Нет\nОтвет _____')
            match cooking:
                case '1':
                    print('Выбирай что сварить:')
                    recept = choice_recept(collection_potion.book)
                    if recept != 0 and type(recept) is Alchemy:
                        ingredient = find_ingredient(recept)
                        print(ingredient)
                        if ingredient == 'Зелье варится ⚗️':
                            line()
                            inventory.add_potion(recept)
                            inventory.delete_flowers()
                            show_smell(recept)
                            line()
                        if ingredient == 'Взрыв 💥':
                            find_flowers(recept)
                            inventory.delete_flowers()
                            print('О нет вы ГОРИТЕ!!!!!🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥')
                            pour_fire(person)
                            line()
                    if recept == 0 or type(recept) is not Alchemy:
                        print('Вы ни чего не выбрали! 🗿')

                case '2':
                    pass

        case '3':
            line()
            print('Добро пожаловать в сад 🌱. Что посеять?')
            plant_seeds = choice_plant(inventory.plant)
            if type(plant_seeds) is Plant:
                i_pl = person.plant_flower(plant_seeds)
                inventory.add_flowers(i_pl)
                print('\nУспешно посажено 👌.')
                inventory.delete_plant(plant_seeds)
                line()
            else:
                print('\n❌ Вы ничего не выбрали. Попробуйте снова.')
                line()
                pass

        case '4':
            line()
            inventory.show_inventory()
            line()

        case '5':
            print('Вы умеете готовить следующие зелья:')
            collection_potion.show_book()
            line()
            new_potion = input('Хотите добавить новое зелье? 1 = Да 0 = Нет\nВыбор _____')
            match new_potion:
                case '0':
                    pass

                case '1':
                    new_title = input('Придумай название зелью _____')
                    new_effect = input('Какой эффект от него _____')
                    print('Зеля состоят из 2 ингредиентов. Выбирай из имеющихся 👇')
                    print('Первый ингредиент 1️⃣')
                    new_ingredient1 = choice_plant(plant_shop)
                    print('Второй ингредиент 2️⃣')
                    new_ingredient2 = choice_plant(plant_shop)

                    collection_potion.add_potion(Alchemy(new_title, new_effect, new_ingredient1, new_ingredient2))
                    line()
                    print('Новое зелье уже в книге Зельеварения. Посмотреть?')
                    yes_or_no(collection_potion)