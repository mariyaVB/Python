# ------------------------------------------------ Задание ---------------------------------------------------------
# Дописать метод удаления и/или частичного поиска контакта (см. текст задания из классной работы).
# Задание из классной работы:
# Написать программу для управления списком контактов. В качестве примера, добавьте в программу два объекта Contact
# в список контактов. Так же необходимо выполнить операции по удалению контакта и поиску контакта в списке
# (удаление и поиск осуществляется пользователем). Результаты операций должны выводятся на экран.


class Contact:
    def __init__(self, name_contact, phone):
        self.name_contact = name_contact
        self.phone = phone

    def display_info(self):
        print(f'Name: {self.name_contact}. Phone number: {self.phone}')


class BusinessContact(Contact):
    def __init__(self, name_contact, phone, company_contact):
        super().__init__(name_contact, phone)
        self.company_contact = company_contact

    def display_info(self):
        print(f'Name: {self.name_contact}. Phone number: {self.phone}. Company : {self.company_contact}')


class PhoneBook:
    def __init__(self):
        self.book = []

    def add_contact(self, contact):
        self.book.append(contact)

    def remove_contact(self, contact):
        key = self.book.index(contact)
        return key

    def __delitem__(self, key):
        del self.book[key]

    def find_contact(self, contact):
        if contact == '':
            return False
        for el_book in self.book:
            a = el_book.name_contact
            if a.startswith(contact):
                return el_book

        return False

    def display_book(self):
        for el_book in self.book:
            el_book.display_info()


# Создание телефонной книги
phone_book = PhoneBook()

# Создание контактов
contact1 = Contact('Nikita', '+7 987 657 7677')
contact2 = BusinessContact('Petr Vladimirovich', '+7 238 11 3409', 'You Steel')
contact3 = Contact('Sveta', '+7 451 309 4513')

# Добавление контактов в книгу
phone_book.add_contact(contact1)
phone_book.add_contact(contact2)
phone_book.add_contact(contact3)

# Посмотреть книгу
print('Contact book:')
phone_book.display_book()

# Найти контакт, можно вводить имя частично
search_contact = input('Find the name of the contact person: ____')
found_contact = phone_book.find_contact(search_contact)
if found_contact:
    print('Find:')
    found_contact.display_info()
else:
    print('The contact was not found.')

# Удалить контакт
remove_contact = input('Remove the name of the contact person: ____')
deleting_contact = phone_book.find_contact(remove_contact)

if deleting_contact:
    print('Deleted')
    del phone_book[phone_book.remove_contact(deleting_contact)]
else:
    print('The contact was not found.')

# Проверяем удалился ли контакт
phone_book.display_book()









