# Book (Книга):
# ●	Свойства: название, автор, год издания, жанр, количество экземпляров.
# ●	Методы: вывод информации о книге, уменьшение/увеличение количества экземпляров.

class Book:
    def __init__(self, title: str, author: str, year: str, genre: str, count: int):
        self.title = self.check_attribute(title)
        self.author = self.check_attribute(author)
        self.year = self.check_attribute(year)
        self.genre = self.check_attribute(genre)
        self.count = self.check_count(count)

    @staticmethod
    def check_attribute(attribute):
        if type(attribute) is str:
            return attribute
        raise 'Attribute is not str'

    @staticmethod
    def check_count(count):
        if type(count) is int and count >= 0:
            return count
        raise 'Count is not int or count < 0'

    def __str__(self):
        return (f'''Название книги: {self.title}
Автор книги: {self.author}
Год издания: {self.year}
Жанр: {self.genre}
В наличии: {self.count}\n''')

    def show_info_book(self):
        print(f'''Название книги: {self.title}
Автор книги: {self.author}
Год издания: {self.year}
Жанр: {self.genre}
В наличии: {self.count}\n''')

    def add_book(self, quantity):
        self.count += self.check_count(quantity)

    def reduce_book(self, quantity):
        self.count -= self.check_count(quantity)
        if self.count >= 0:
            return self.count
        else:
            raise 'Count < 0'



