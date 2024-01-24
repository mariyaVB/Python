# ----------------------------------------------------- Задача ----------------------------------------------------
# Создать: класс Book представляющий книгу.
# Реализуйте магические методы сравнения (==, !=, <, >, <=, >=) на основе сравнения года издания книги.
# Книги сравниваются по году издания.

class Book:
    def __init__(self, year_of_publication):
        self.year_of_publication = year_of_publication

    def __eq__(self, other):
        result = self.year_of_publication == other.year_of_publication
        if result:
            return 'Год издания совпадает.'
        return 'Год издания не совпадает.'

    def __ne__(self, other):
        result = self.year_of_publication != other.year_of_publication
        if result:
            return 'Год издания не совпадает.'
        return 'Год издания совпадает.'

    def __lt__(self, other):
        result = self.year_of_publication < other.year_of_publication
        if result:
            return f'{self.year_of_publication} < {other.year_of_publication}'
        return False

    def __gt__(self, other):
        result = self.year_of_publication > other.year_of_publication
        if result:
            return f'{self.year_of_publication} > {other.year_of_publication}'
        return False

    def __le__(self, other):
        result = self.year_of_publication <= other.year_of_publication
        if result:
            return f'{self.year_of_publication} <= {other.year_of_publication}'
        return False

    def __ge__(self, other):
        result = self.year_of_publication >= other.year_of_publication
        if result:
            return f'{self.year_of_publication} >= {other.year_of_publication}'
        return False


book1 = Book(1909)
book2 = Book(1957)
book3 = Book(1957)
print(book1 == book2)
print(book2 != book3)
print(book1 < book2)
print(book1 > book2)
print(book2 <= book3)
print(book3 >= book1)


# ----------------------------------------------------- Задача ----------------------------------------------------
# Создайте: класс Fraction, представляющий дробь.
# Реализуйте магические методы сложения, вычитания, умножения и деления для дробей.

class Fraction:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num


fraction1 = Fraction(234.86)
fraction2 = Fraction(176.21)
print(fraction1 + fraction2)
print(fraction1 - fraction2)
print(fraction1 * fraction2)
print(fraction1 / fraction2)


# ----------------------------------------------------- Задача ----------------------------------------------------
# Создайте: класс Playlist, представляющий плейлист музыкальных треков.
# Реализуйте магические методы для сложения и вычитания двух плейлистов, чтобы объединить или удалить треки.

class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __add__(self, other):
        return self.songs + other.songs

    def __setitem__(self, key, value):
        if key >= len(self.songs):
            add_place = key + 1 - len(self.songs)
            self.songs.extend([None] * add_place)

        self.songs[key] = value

    def __delitem__(self, key):
        del self.songs[key]

    def __str__(self):
        return f'{self.songs}'


print('Создали два плейлиста:')
playlist1 = Playlist(['Candy Shop', 'In Da Club'])
playlist2 = Playlist(['Give It to Me', 'Just a lit bit'])
print(playlist1)
print(playlist2)

print('Добавили в плейлист 1 песню:')
playlist1[2] = 'This is Paris'
print(playlist1)

print('Объединённый плейлист:')
playlist_united = playlist1 + playlist2
print(playlist_united)

print('Удаление третьей песни:')
del playlist_united[2]
print(playlist_united)










