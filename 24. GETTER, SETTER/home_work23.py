# ------------------------------------------------ Задача --------------------------------------------------------------
# Создать класс "Person" с атрибутами "name", "age", "email" с методами для чтения и записи данных всех трех атрибутов,
# а также реализовать валидацию для атрибута "age":
#     ● должно быть положительным целым числом задача

class Person:
    def __init__(self):
        self.__name = 'Mariya'
        self.__age = self.is_valid_age(30)
        self.__email = 'masha@mail.ru'

    @staticmethod
    def is_valid_age(age):
        if type(age) != int:
            return 'Not int'
        if age <= 0:
            return 'Age negative number'
        return age

    def read_object(self):
        print(f'Имя: {self.__name}, возраст: {self.__age}, почта: {self.__email}')

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def change_name(self, name):
        self.__name = name

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def change_age(self, new_age: int):
        self.__age = self.is_valid_age(new_age)

    @property
    def get_email(self):
        return self.__email

    @get_email.setter
    def change_email(self, new_email):
        self.__email = new_email


print('Начальные атрибуты:')
user = Person()
user.read_object()
print('Меняем атрибуты:')
user.change_name = 'Nikita'
user.change_age = 29
user.change_email = 'nik@mail.ru'
user.read_object()

print(f'Читаем атрибуты: {user.get_name}, {user.get_age}, {user.get_email}')


# ------------------------------------------------ Задача --------------------------------------------------------------
# Создать класс "Book" с атрибутами "title", "author", "genre", с методами для чтения и записи данных всех трех
# атрибутов, а также реализовать валидацию для атрибута "genre":
#     ● должно быть строкой не должно быть пустой строкой и должно содержать наименование только из указанного списка
#     [“фантастика”, “драма”, “проза”]

class Book:
    def __init__(self):
        self.__title = 'Mara and Morok'
        self.__author = 'Lia Arden'
        self.__genre = self.is_valid_genre('фантастика')

    @staticmethod
    def is_valid_genre(genre):
        list_genre = ['фантастика', 'драма', 'проза']
        if genre not in list_genre:
            return 'The genre is not on the list'
        if type(genre) != str:
            return 'The genre is not str'
        return genre

    def read_book(self):
        print(f'Название книги: {self.__title}, Автор: {self.__author}, Жанр: {self.__genre}.')

    @property
    def get_title(self):
        return self.__title

    @get_title.setter
    def change_title(self, new_title):
        self.__title = new_title

    @property
    def get_author(self):
        return self.__author

    @get_title.setter
    def change_author(self, new_author):
        self.__author = new_author

    @property
    def get_genre(self):
        return self.__genre

    @get_genre.setter
    def change_genre(self, new_genre):
        self.__genre = new_genre


book = Book()
print('Начальные атрибуты:')
book.read_book()
print('Меняем атрибуты:')
book.change_title = 'Atlant raspravil plechi'
book.change_author = 'Aina Reind'
book.change_genre = 'драма'
book.read_book()
print(f'Читаем атрибуты: {book.get_title}, {book.get_author}, {book.get_genre}')




