# 1. Создать БД “онлайн-магазина,”с таблицами users, orders, products и требования:
#   a. Пользователи могут регистрироваться, входить в систему и изменять свои данные. ✅
#   b. Администратор может добавлять, удалять и изменять информацию о продуктах. ✅
#   c. Пользователи могут просматривать каталог товаров, добавлять их в корзину и оформлять заказы. ✅
#   d. После оформления заказа пользователь должен получить подтверждение по электронной почте. ‼️‼️
#   Разобрать как подключать модуль отправки сообщений ‼️‼️
#   e. Статус заказа должен автоматически изменяться в зависимости от его выполнения. ✅


import sqlite3 as sql


def db_decorator(func):
    def db_connection(self, *args, **kwargs):
        self.connection = sql.connect(self.db_name)
        self.cursor = self.connection.cursor()

        result = func(self, *args, **kwargs)

        self.connection.commit()
        self.connection.close()
        return result
    return db_connection


class Users:
    def __init__(self, db_name='shop_db.db'):
        self.db_name = db_name
        self.create_table()

    @db_decorator
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                            (id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                            email_user TEXT UNIQUE NOT NULL,
                            name_user TEXT NOT NULL,
                            password_user TEXT UNIQUE NOT NULL)''')

    @db_decorator
    def add_user(self, email, name, password):
        self.cursor.execute('''INSERT INTO Users (email_user, name_user, password_user) VALUES 
                            (?, ?, ?)''', (email, name, password))

    @db_decorator
    def redaction_user(self, email_user, name=None, password=None):
        request = 'UPDATE Users SET '
        new_user = []

        if name is not None:
            request += 'name_user = ?, '
            new_user.append(name)

        if password is not None:
            request += 'password_user = ?, '
            new_user.append(password)

        request = request.rstrip(', ')
        request += ' WHERE email_user = ? '
        new_user.append(email_user)

        self.cursor.execute(request, tuple(new_user))

    @db_decorator
    def show_user(self, email_user=None):
        request = 'SELECT * FROM Users'
        where = ''

        if email_user is not None:
            where = f'WHERE email_user = ?, ({email_user})'

        self.cursor.execute(request, where)
        return self.cursor.fetchall()

    @db_decorator
    def delete_user(self, email_user):
        self.cursor.execute('DELETE FROM Users WHERE email_user = ?', (email_user,))


    @db_decorator
    def show_name(self, email_user):
        self.cursor.execute('SELECT name_user FROM Users WHERE email_user = ?', (email_user,))
        return self.cursor.fetchall()

    @db_decorator
    def show_id(self, email_user):
        self.cursor.execute('SELECT id_user FROM Users WHERE email_user = ?', (email_user,))
        return self.cursor.fetchall()


class Products:
    def __init__(self, db_name='shop_db.db'):
        self.db_name = db_name
        self.create_table()

    @db_decorator
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                                    (id_product INTEGER PRIMARY KEY AUTOINCREMENT,
                                    category_product TEXT,
                                    title_product TEXT NOT NULL,
                                    price_product REAL CHECK (price_product > 0) NOT NULL,
                                    count_product INTEGER CHECK (count_product >= 0))''')

    @db_decorator
    def add_product(self, category, title, price, count):
        self.cursor.execute('''INSERT INTO Products (category_product, title_product, price_product, count_product) VALUES 
                            (?, ?, ?, ?)''', (category, title, price, count))

    @db_decorator
    def redaction_product(self, id_product, category=None, title=None, price=None, count=None):
        request = 'UPDATE Products SET '
        new_product = []

        if category is not None:
            request += 'category_product = ?, '
            new_product.append(category)

        if title is not None:
            request += 'title_product = ?, '
            new_product.append(title)

        if price is not None:
            request += 'price_product = ?, '
            new_product.append(price)

        if count is not None:
            request += 'count_product = ?, '
            new_product.append(count)

        request = request.rstrip(', ') + ' WHERE id_product = ? '
        new_product.append(id_product)

        self.cursor.execute(request, tuple(new_product))

    @db_decorator
    def delete_product(self, id_product):
        self.cursor.execute('DELETE FROM Products WHERE id_product = ?', (id_product,))

    @db_decorator
    def show_product(self, id_product=None, category=None):
        request = 'SELECT * FROM Products '
        where = ''

        if id_product is not None:
            where += f'WHERE id_product = {id_product}'

        if category is not None:
            where += f'WHERE category_product = "{category}"'

        request = request + where

        self.cursor.execute(request)
        return self.cursor.fetchall()

    @db_decorator
    def find_id_product(self):
        self.cursor.execute('SELECT id_product FROM Products')
        return self.cursor.fetchall()

    @db_decorator
    def get_count_product(self, id_product):
        request = 'SELECT count_product FROM Products WHERE id_product = ? '
        self.cursor.execute(request, (id_product,))
        return self.cursor.fetchall()


class Orders:
    def __init__(self, db_name='shop_db.db'):
        self.db_name = db_name
        self.create_table()

    @db_decorator
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Orders
                                    (id_order INTEGER PRIMARY KEY AUTOINCREMENT,
                                    user_order INTEGER,
                                    cart_order INTEGER,
                                    quanty_order INTEGER,
                                    status_order TEXT,
                                    FOREIGN KEY (cart_order) REFERENCES Products(id_product),
                                    FOREIGN KEY (user_order) REFERENCES Users(id_user))''')

    @db_decorator
    def add_order(self, user=None, cart=None, quanty=None, status='Добавлен в корзину'):
        self.cursor.execute('''INSERT INTO Orders (user_order, cart_order, quanty_order, status_order) VALUES 
                            (?, ?, ?, ?)''', (user, cart, quanty, status))

    @db_decorator
    def redaction_order(self, id_order, quanty=None, status=None):
        request = ''
        if quanty is not None:
            request += f'UPDATE Orders SET quanty_order = {quanty} WHERE id_order = {id_order}'

        if status is not None:
            request += f'UPDATE Orders SET status_order = "{status}" WHERE id_order = {id_order}'

        self.cursor.execute(request)

    @db_decorator
    def delete_order(self, id_order):
        self.cursor.execute('DELETE FROM Orders WHERE id_order = ?', (id_order,))

    @db_decorator
    def show_order(self, id_user=None):
        where = ''
        param = ('id_order, name_user, email_user, title_product, quanty_order, price_product, '
                 'price_product * quanty_order as "Итог", status_order')
        join1 = 'JOIN Users ON user_order = Users.id_user '
        join2 = 'JOIN Products ON cart_order = Products.id_product '
        if id_user is not None:
            where = f'WHERE user_order = {id_user}'

        request = f'SELECT {param} FROM Orders ' + join1 + join2 + where

        self.cursor.execute(request)
        return self.cursor.fetchall()

    @db_decorator
    def get_product_other(self, order):
        request = 'SELECT cart_order FROM Orders WHERE id_order = ?'
        self.cursor.execute(request, (order,))
        return self.cursor.fetchall()

    @db_decorator
    def get_quanty_order(self, order):
        request = 'SELECT quanty_order FROM Orders WHERE id_order = ?'
        self.cursor.execute(request, (order,))
        return self.cursor.fetchall()

    @db_decorator
    def get_status_order(self, order):
        request = 'SELECT status_order FROM Orders WHERE id_order = ?'
        self.cursor.execute(request, (order,))
        return self.cursor.fetchall()









