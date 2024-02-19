import random


# _____________________________________________ PLANT, FLOWERS CLASS __________________________________________________
class Plant:
    def __init__(self, title, price):
        self.plant_title = title
        self.plant_price = price

    def __str__(self):
        return f'{self.plant_title}'

    def show_plant(self):
        print(f'Название растения: {self.plant_title}\nСтоимость: {self.plant_price}')


class Flowers(Plant):
    def __init__(self, title, price):
        super().__init__(title, price)
        self.count = self.random_count()

    @staticmethod
    def random_count():
        count = random.randint(2, 5)
        return count

    def __str__(self):
        return f'{self.plant_title} | Количество {self.count} шт.'

    def delete_count(self):
        self.count -= 1
        return self.count


# _________________________________________ COLLECTION CLASS____________________________________________________________
class Collection:
    def __init__(self, *recept):
        self.book = list(recept)

    def __str__(self):
        return f'{self.book}'

    def add_potion(self, potion):
        if type(potion) is not Alchemy:
            print('Должен быть класс Алхимия')
        self.book.append(potion)

    def show_book(self):
        count = 0
        for potion in self.book:
            count += 1
            print('---------------------------------------------------------------------------------------------------')
            print(f'{count}. {potion}')


# ____________________________________________ INVENTORY CLASS ________________________________________________________
class Inventory:
    def __init__(self):
        self.plant = []
        self.potion = []
        self.flower = []

    def show_inventory(self):
        count_plant = '🪴'
        count_potion = '🧪'
        count_flower = '🌸'

        print('Растения в подсумке: ')
        for plant in self.plant:
            print(f'{count_plant} {plant}')
        print('-------------------------------------------------------------------------------------------------')

        print('Зелья в подсумке:')
        for potion in self.potion:
            print(f'{count_potion} {potion.potion}')
        print('-------------------------------------------------------------------------------------------------')

        print('Урожая в подсумке: ')
        for flower in self.flower:
            print(f'{count_flower} {flower.plant_title} {flower.count} шт.')

    def add_plant(self, *plants):
        for plant in plants:
            if type(plant) is not Plant:
                raise 'Растение должно быть класса Plant'
            self.plant.append(plant)

    def add_potion(self, *potions):
        for potion in potions:
            if type(potion) is not Alchemy:
                raise 'Зелье должно быть класса Alchemy'
            self.potion.append(potion)

    def add_flowers(self, *harvest):
        for flower in harvest:
            if type(flower) is not Flowers:
                raise 'Цветы должны быть класса Flowers'
            self.flower.append(flower)

    def delete_plant(self, seed):
        self.plant.remove(seed)
        return self.plant

    def delete_potion(self, del_potion):
        self.potion.remove(del_potion)
        return self.potion

    def delete_flowers(self):
        for flowers in self.flower:
            if flowers.count <= 0:
                self.flower.remove(flowers)
        return self.flower


# ________________________________________________ ALCHEMY CLASS________________________________________________________
class Alchemy:
    def __init__(self, potion, effect, *ingredient):
        self.potion = potion
        self.ingredient = ingredient
        self.effect = effect
        self.smell = self.smell_cooking(potion)

        if self.valid_ingredient(self.ingredient) < 1:
            raise 'Зелью нужен хотя бы один ингредиент.'
        if self.valid_ingredient(ingredient) > 2:
            raise 'У зелья максимум 2 ингредиента.'

    @staticmethod
    def valid_ingredient(ingredients):
        count = len(ingredients)
        return count

    @staticmethod
    def unpacking_ingredient(plants):
        if len(plants) == 1:
            for i in plants:
                return f'{i}'
        elif len(plants) == 2:
            for i in plants:
                return f'{i}, {plants[plants.index(i) + 1]}'

    @staticmethod
    def smell_cooking(potion):  # Рандомный результат готовки зелья
        smell = ['Встреча абсолю ванили и бобов тонка, оттененная маслом сандалового дерева.\n',
                 'Сверкающий бергамот, жасмин самбак и белый мускус сплетаются воедино в объемную,\n '
                 'обволакивающую композицию., Лист фиалки, мандарин и кардамон приоткрывают завесу тайны и пропускают\n'
                 'вперёд туманный ладан, мускатный орех, лабданум и абсолют розы.']
        if potion == 'Амортенция':
            return (f'Дуэт дамасской розы и пиона раскрывается благородством, подобно страстным и сияющим эмоциям.\n'
                    f'Мягкий, легкий аккорд белого мускуса завершает букет аромата, рассказывающего историю любви.\n')
        if potion == 'Феликс Фелицис':
            return (f'Воздух пронизан легкими цветочными оттенками красного жасмина и розы, подчеркнутыми яркими\n'
                    f'аккордами зеленого мандарина и мяты на основе базовых успокаивающих нот мускуса и амбретты.\n')
        if potion == 'Оборотное':
            return (f'Аромат с зелено-мускусным характером, в котором ноты ветивера смешиваются с нотами дерева,\n'
                    f'окутанного плющом, с кожаной основой.')
        if potion == 'Зелье Настроения':
            return (f'Чарующая сладость ванили и сахарной пудры дополняют ноты воздушной сахарной ваты, мускуса,\n'
                    f'свежих красных ягод и карамели.')
        if potion == 'Живая Смерть':
            return (f'Насыщенный шлейф из чувственных нот перуанского бальзама, обжаренных бобов тонка, сандалового\n'
                    f'дерева, ветивера и кедра.')
        else:
            smell_random = random.choice(smell)
            return smell_random

    def __str__(self):
        return f'{self.potion} | Состав: {self.unpacking_ingredient(self.ingredient)}\nЭффект: {self.effect}'

    def show_potion(self):
        print(f'{self.potion} | Состав: {self.unpacking_ingredient(self.ingredient)}\nЭффект: {self.effect}')

    @staticmethod
    def cook_potion(finished_potion):
        return finished_potion


# __________________________________________________ GAME CLASS _____________________________________________________
class Game:
    def __init__(self):
        self.balance = 100

    def show_balance(self):
        print(f'В вашем кошельке {self.balance} 🪙')

    @staticmethod
    def plant_flower(seeds):
        flower = Flowers(seeds.plant_title, seeds.plant_price)
        return flower

    def pay_plant(self, price_plant):
        if (self.balance - price_plant.plant_price) < 0:
            print(f'У вас недостаточно 🪙')
        else:
            self.balance -= price_plant.plant_price
            return self.balance

    def sell_potion(self):
        price_potion = random.randint(10, 50)
        self.balance += price_potion
        print(f'Зелье продано за {price_potion} 🪙')
        return self.balance


# ------------------------------------------------------ FUNCTION -----------------------------------------------------
def yes_or_no(collection):  # Показывает новое зелье
    show = input('1 = Да 2 = Нет\nОтвет _____')
    if show == '2':
        pass
    if show == '1':
        return collection.show_book()


def choice_recept(recipes):  # Выбор зелья для готовки
    for recept in recipes:
        print(f'🧾 {recept}')
        choice = input('Выбрать этот рецепт? 1 = Да | 2 = Нет | 0 = Выход\nОтвет _____')
        if choice == '1':
            return recept
        if choice == '2':
            pass
        if choice == '0':
            return 0


def find_ingredient(herb):  # Сравнивает цветы в подсумке с составом зелья
    counting = []
    for flower in inventory.flower:
        for ingredient in herb.ingredient:
            if flower.plant_title == ingredient.plant_title:
                counting.append(flower)
    if len(counting) == 0:
        return f'У вас нет цветочков для зелья 🥀'
    if len(counting) == 1:
        for count in counting:
            for ingredient in herb.ingredient:
                if count.plant_title != ingredient.plant_title:
                    return f'Не хватает: 🌸 {count.plant_title}'
    if len(counting) == 2:
        for flower in counting:
            flower.delete_count()
        print(f'Начинаем варить! ⚗️')
        result = result_cooking()
        return result


def find_flowers(herb):  # Удаляет количество цветочков после приготовления зелья
    flowers = []
    for flower in inventory.flower:
        for ingredient in herb.ingredient:
            if flower.plant_title == ingredient.plant_title:
                flowers.append(flower)

    for flower in flowers:
        flower.delete_count()


def result_cooking():  # Рандом результата
    list_result = ['Взрыв 💥', 'Зелье варится ⚗️', 'Зелье варится ⚗️', 'Зелье варится ⚗️']
    result = random.choice(list_result)
    return result


def pour_fire(pers):
    fire = input('1 = Потушить самому\n2 = Вызвать пожарных\nОтвет _____')
    if fire == '1':
        print(f'🧯💦🧯💦🧯💦🧯💦🧯💦🧯💦🧯💦\nПотушено!')
    if fire == '2':
        person.balance -= 15
        print('🚒🧑‍🚒👩‍🚒🚒🧑‍🚒👩‍🚒🚒🧑‍🚒👩‍🚒🚒🧑‍🚒👩‍🚒🚒🧑‍🚒👩‍🚒\nПотушено! За услугу списано 15 🪙.')
        return pers.balance


def show_smell(potion):   # Выводит запах зелья
    print(f'🍃{potion.smell}🍃')


def choice_plant(plants):  # Перебирает семена в подсумке и должна вернуть объект семена
    emoji = ['🌸', '💮', '🪷', '🪻', '🌿', '🍀', '🍁', '☘️']
    for plant in plants:
        print(f'{random.choice(emoji)} {plant}')
        choice = input('Выбрать это растение? 1 = Да | 2 = Нет | 0 = Выход _____')
        if choice == '1':
            return plant
        if choice == '2':
            pass
        if choice == '0':
            break


def choice_potion(inventory_potion):   # Перебирает зелья в подсумке
    for potion in inventory_potion:
        print(f'{'🧪'} {potion.potion}')
        choice = input('Выбрать это зелье для продажи? 1 = Да | 2 = Нет | 0 = Выход _____')
        if choice == '1':
            return potion
        if choice == '2':
            pass
        if choice == '0':
            break


# ------------------------------------------------------- PLANT ----------------------------------------------------
plant1 = Plant("Шалфей", 10)
plant2 = Plant("Ромашка", 15)
plant3 = Plant("Полынь", 5)
plant4 = Plant("Валерьяна", 15)
plant5 = Plant("Чабрец", 25)
plant6 = Plant("Растопырник", 17)
plant7 = Plant("Шкура Бумсланга", 12)
plant8 = Plant("Водоросли", 5)
plant9 = Plant("Майоран", 19)
plant10 = Plant("Тысячелистник", 30)

plant_shop = [plant1, plant2, plant3, plant4, plant5, plant6, plant7, plant8, plant9, plant10]

# -------------------------------------------------- RECEPT POTION--------------------------------------------------
recept1 = Alchemy('Зелье Настроения', 'Зелье, вызывающее смех у выпившего его.', plant1, plant2)
recept2 = Alchemy('Живая Смерть', 'Очень сильное усыпляющее средство.', plant3, plant4)
recept3 = Alchemy('Феликс Фелицис', 'Выпившему его определённое время сопутствует удача во всех начинаниях.',
                  plant5, plant6)
recept4 = Alchemy('Оборотное', 'Выпивший его преображается на один час и выглядит как тот, чьи частички '
                               '(волосы, ногти и т. п.) были добавлены в зелье.', plant7, plant8)
recept5 = Alchemy('Амортенция', 'Любовное зелье, которое создаёт непреодолимое влечение к тому,'
                                ' кто сварил зелье.', plant9, plant10)

# ------------------------------------------------- COLLECTION -------------------------------------------------------
collection_potion = Collection(recept1, recept2, recept3, recept4, recept5)

# --------------------------------------------------- INVENTORY ------------------------------------------------------
inventory = Inventory()

# ------------------------------------------------------ GAME --------------------------------------------------------
person = Game()




















# flower1 = Flowers("Шалфей", 10)
# flower2 = Flowers("Ромашка", 15)
# flower7 = Flowers("Шкура Бумсланга", 12)
# flower8 = Flowers("Водоросли", 5)
# inventory.add_plant(plant8, plant9, plant6)
# inventory.add_potion(recept5)
# inventory.add_flowers(flower7, flower8, flower1)



