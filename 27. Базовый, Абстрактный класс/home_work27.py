# -------------------------------------------------- Задача ----------------------------------------------------------
# Разработать: иерархию классов для компьютерных игр.
# Создайте базовый класс "Игра" с общими характеристиками (например, название, жанр).
# Затем создайте подклассы для различных жанров, таких как "Экшен" и "Стратегия", добавляя уникальные свойства и методы.
# Реализуйте метод для подсчета общего времени игры.

from abc import ABC, abstractmethod
import timeit


class Game(ABC):
    @staticmethod
    def valid_init(info):
        if not type(info) is str:
            raise 'Ошибка в названии игры и жанре.'
        return info

    @abstractmethod
    def __init__(self, title, genre):
        self._title = self.valid_init(title)
        self._genre = self.valid_init(genre)

    @abstractmethod
    def info_game(self):
        print(f'Название игры: {self._title}. Жанр: {self._genre}.')

    @abstractmethod
    def counting_game_time(self):
        raise NotImplementedError("В дочернем классе должен быть переопределен counting_game_time")


class ActionAdventure(Game):
    def __init__(self, title, genre):
        self.time_session = 0
        self.time_break = 0
        super().__init__(title, genre)

    def info_game(self):
        super().info_game()
        print('Смешанный жанр компьютерных игр, сочетающий элементы квеста и экшен.')

    @staticmethod
    def valid_time(time):
        if type(time) is int:
            return time
        raise 'Время должно быть int.'

    def counting_game_time(self):
        self.time_session = self.valid_time(int(input('Сколько времени в минутах, вы провели за игрой: _____')))
        self.time_break = self.valid_time(int(input('Сколько времени в минутах, вы отдыхали от игры: _____')))

        game_time = self.time_session + self.time_break
        print(f'Общее время игры {game_time} минут(ы).')


class Simulation(Game):
    def __init__(self, title, genre):
        self.game_hero = ''
        super().__init__(title, genre)

    def info_game(self):
        super().info_game()
        print('Жанр компьютерных игр, в котором игрок управляет жизнью одного или нескольких виртуальных существ.')

    def counting_game_time(self):
        self.game_hero = input('Есть ли игровые персонажи у вас? 1 = Да 2 = Нет _____')
        if self.game_hero == '1':
            print('Игра бесконечна, пока у вас есть живые персонажи.')
        elif self.game_hero == '2':
            print('Игра окончена!')
        else:
            print('Неверная команда.')


class Strategy(Game):
    def __init__(self, title, genre, multiplayer: int = 1):
        self.__level = 0
        self.__multiplayer = self.valid_multiplayer(multiplayer)
        super().__init__(title, genre)

    @staticmethod
    def valid_multiplayer(multiplayer):
        if 1 <= multiplayer <= 4 and type(multiplayer) is int:
            return multiplayer
        else:
            raise 'Игроков должно быть int от 1 до 4'

    def info_game(self):
        print(f'Название игры: {self._title}. Жанр: {self._genre}. Игроков: {self.__multiplayer}.')
        print('Жанр, в котором залогом достижения победы является планирование и стратегическое мышление.')

    def counting_game_time(self):
        self.__level = input('Выберите сложность игры: 1 = Легко 2 = Средне 3 = Сложно _____')
        if self.__level == '1':
            print(f'Время игры составляет 60 минут.')
        elif self.__level == '2':
            print(f'Время игры составляет 45 минут.')
        elif self.__level == '3':
            print(f'Время игры составляет 30 минут.')
        else:
            print('Неверная команда.')


game1 = ActionAdventure('The Lust Of Us', 'Приключенческий экшен')
game1.info_game()
game1.counting_game_time()

game2 = Simulation('Sims 4', 'Симулятор жизни')
game2.info_game()
game2.counting_game_time()

game3 = Strategy('Heroes of Might and Magic III', 'Пошаговая стратегия', 3)
game3.info_game()
game3.counting_game_time()


