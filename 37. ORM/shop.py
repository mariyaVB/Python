# Валидация на числа, текст, пароль и логин
# При оплате товара меняется количество товара в таблице из базы данных
# Таблица заказы связана многие ко многим с продуктами и пользователем

from homework37 import *
from valid_product import *
from valid_user import *

user_db = Users()
product_db = Products()
order_db = Orders()


while True:
    command = input('''
        1 = Администратор
        2 = Пользователь

        0 = Выход
        _________''')

    match command:
        case '0':
            break

        case '1':
            print('\n---------------- Панель администратора ----------------')
            while True:
                admin = input('''
                    1: Посмотреть товары/найти товар
                    2: Добавить товар
                    3: Отредактировать товар
                    4: Удалить товар
                    
                    0 = Назад
                    _________''')

                match admin:
                    case '0':
                        break

                    case '1':
                        enter()
                        print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ПРОСМОТР/ПОИСК 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                        while True:
                            find = input('1: Посмотреть\n2: Найти\n0: Назад')
                            match find:
                                case '1':
                                    print('Выбери категорию, или нажми Enter чтобы посмотреть все.')
                                    category = valid_category(list_category, new_category=choice_category(list_category))
                                    while category is False:
                                        category = valid_category(list_category, new_category=choice_category(list_category))

                                    list_find = product_db.show_product(category=category)
                                    for i_list in list_find:
                                        print(i_list)

                                case '2':
                                    list_product = product_db.show_product()
                                    list_id = product_db.find_id_product()
                                    id_product = get_product(list_id)
                                    while id_product is False:
                                        id_product = get_product(list_id)
                                    name = product_db.show_product(id_product=id_product)
                                    print(name)

                                case '0':
                                    break

                    case '2':
                        enter()
                        print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ДОБАВЛЕНИЕ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                        print('Доступные категории:')
                        category = valid_category(list_category, category=choice_category(list_category))
                        while category is False:
                            valid_category(list_category, category=choice_category(list_category))

                        title = valid_text(input('Название товара: _____'))
                        while title is False:
                            print('Не может быть пустой.')
                            title = valid_text(input('Название товара: _____'))

                        price = valid_digit(input('Стоимость товара: _____'))
                        while price is False:
                            price = valid_digit(input('Стоимость товара: _____'))

                        count = valid_digit(input('Остаток товара: _____'))
                        while count is False:
                            count = valid_digit(input('Остаток товара: _____'))

                        product_db.add_product(category, title, price, count)

                    case '3':
                        enter()
                        print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ РЕДАКТИРОВАНИЕ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                        list_product = product_db.show_product()
                        list_id = product_db.find_id_product()
                        id_product = get_product(list_id)
                        while id_product is False:
                            id_product = get_product(list_id)

                        print('\nПропустить пункт ⤵️Enter.')
                        new_category = valid_category(list_category, new_category=choice_category(list_category))

                        while new_category is False:
                            category = choice_category(list_category)
                            new_category = valid_category(list_category, new_category=choice_category(list_category))

                        title = input('Изменить название товара: _____')
                        new_title = valid_redaction(title, valid_text(title))
                        while new_title is False:
                            title = input('Изменить название товара: _____')
                            new_title = valid_redaction(title, valid_text(title))

                        price = input('Изменить стоимость товара: _____')
                        new_price = valid_redaction(price, valid_digit(price))
                        while new_price is False:
                            price = input('Изменить стоимость товара: _____')
                            new_price = valid_redaction(price, valid_digit(price))

                        count = input('Изменить остаток товара: _____')
                        new_count = valid_redaction(count, valid_digit(count))
                        while new_count is False:
                            count = input('Изменить остаток товара: _____')
                            new_count = valid_redaction(count, valid_digit(count))

                        product_db.redaction_product(id_product, new_category, new_title, new_price, new_count)

                    case '4':
                        enter()
                        print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ УДАЛЕНИЕ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                        list_product = product_db.show_product()
                        list_id = product_db.find_id_product()
                        id_product = get_product(list_id)
                        while id_product is False:
                            id_product = get_product(list_id)
                        name = product_db.show_product(id_product=id_product)
                        product = show_del_product(name)
                        product_db.delete_product(id_product)
                        print(f'\n⬜Позиция {product} была полностью удалена.')

        case '2':
            while True:
                user = input('''
                                1: Вход
                                2: Регистрация
                                
                                0: Назад''')

                match user:
                    case '0':
                        break

                    case '1':
                        enter()
                        print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ВХОД 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                        list_mail = user_db.show_user()
                        mail = input('Электронная почта: _____')
                        password = input('Пароль: _____')
                        entrance = check_entrance(mail, password, list_mail)
                        while entrance is False:
                            print('Не верный логин или пароль.')
                            exit_entrance = input('0: Назад\n'
                                                  '1: Попробовать еще раз.')
                            if exit_entrance == '0':
                                break
                            mail = input('Электронная почта: _____')
                            password = input('Пароль: _____')
                            entrance = check_entrance(mail, password, list_mail)
                        list_name = user_db.show_name(mail)
                        print(f'Личный кабинет 🏡 {write_round(list_name)}')
                        while True:
                            enter()
                            menu = input('1: Посмотреть каталог\n'
                                         '2: Посмотреть корзину/заказы\n'
                                         '3: Подтвердить получение\n'
                                         '4: Редактировать профиль\n'
                                         
                                         '0: Выйти с профиля')
                            enter()
                            match menu:
                                case '1':
                                    print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ПРОСМОТР/ПОИСК 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                                    while True:
                                        find = input('1: Посмотреть\n2: Добавить в корзину\n0: Назад')
                                        match find:
                                            case '1':
                                                print('Выбери категорию, или нажми Enter чтобы посмотреть все.')
                                                category = valid_category(list_category, new_category=choice_category(list_category))
                                                while category is False:
                                                    category = valid_category(list_category,new_category=choice_category(list_category))

                                                list_find = product_db.show_product(category=category)
                                                for i_list in list_find:
                                                    print(i_list)

                                            case '2':
                                                print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ДОБАВИТЬ В КОРЗИНУ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                                                list_user = user_db.show_id(mail)
                                                user = write_round(list_user)

                                                list_id = product_db.find_id_product()
                                                product = get_product(list_id)
                                                print(product)
                                                while product is False:
                                                    product = get_product(list_id)
                                                name = product_db.show_product(id_product=product)
                                                print(name)

                                                quanty = valid_digit(input('Количество: _____'))
                                                while quanty is False:
                                                    quanty = valid_digit(input('Количество: _____'))

                                                order_db.add_order(user, product, quanty)

                                            case '0':
                                                break

                                case '2':
                                    enter()
                                    print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ПРОСМОТР КОРЗИНЫ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                                    list_user = user_db.show_id(mail)
                                    user = write_round(list_user)
                                    show_cart = order_db.show_order(user)
                                    for cart in show_cart:
                                        print(cart)

                                    pay = input('1: Оплата\n'
                                                '0: Назад\n')

                                    if pay == '1':
                                        enter()
                                        print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ОПЛАТА 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                                        show_cart = order_db.show_order(user)
                                        for cart in show_cart:
                                            print(cart)
                                        order_pay = input('id заказа для оплаты: _____')
                                        print('👌Оплата прошла успешно!')
                                        order_db.redaction_order(id_order=order_pay, status='Оплачен Отправлен')

                                        id_take_product = order_db.get_product_other(order_pay)
                                        id_take_product = str(id_take_product).lstrip('[(').rstrip(',)]')

                                        count = product_db.get_count_product(id_take_product)
                                        count = str(count).lstrip('[(').rstrip(',)]')

                                        quanty_in_order = order_db.get_quanty_order(order_pay)
                                        quanty_in_order = str(quanty_in_order).lstrip('[(').rstrip(',)]')

                                        res_count = int(count) - int(quanty_in_order)

                                        product_db.redaction_product(id_take_product, count=res_count)

                                    if pay == '0':
                                        pass

                                case '3':
                                    enter()
                                    print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ ПОДТВЕЖДЕНИЕ ПОЛУЧЕНИЯ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                                    show_cart = order_db.show_order(user)
                                    for i in show_cart:
                                        print(i)
                                    confirmation = input('Подтвердить получение, id заказа: _____')

                                    check_status = order_db.get_status_order(confirmation)
                                    for status in check_status:
                                        if 'Оплачен Отправлен' in status:
                                            order_db.redaction_order(id_order=confirmation, status='Доставлен')
                                        else:
                                            print('Ваш заказ еще не оплачен.')

                                case '4':
                                    enter()
                                    print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ РЕДАКТИРОВАНИЕ ПРОФИЛЯ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                                    print('\nПропустить пункт ⤵️Enter.')
                                    new_name = valid_name(new_name=input('Имя: _____'))
                                    while new_name is False:
                                        new_name = valid_name(new_name=input('Имя: _____'))

                                    info_password()
                                    new_password = valid_password(new_password=input('Пароль: _____'))
                                    while new_password is False:
                                        info_password()
                                        new_password = valid_password(new_password=input('Пароль: _____'))

                                    user_db.redaction_user(mail, new_name, new_password)

                                case '0':
                                    break

                    case '2':
                        enter()
                        print('〰️〰️〰️〰️〰️〰️〰️〰️〰️ РЕГИСТРАЦИЯ 〰️〰️〰️〰️〰️〰️〰️〰️〰️')
                        name = valid_name(name=input('Имя: _____'))
                        while name is False:
                            name = valid_name(name=input('Имя: _____'))

                        info_mail()
                        email = valid_email(input('Электронная почта: _____'))
                        while email is False:
                            print('Почта не прошла.')
                            info_mail()
                            email = valid_email(input('Электронная почта: _____'))

                        info_password()
                        password = valid_password(password=input('Пароль: _____'))
                        while password is False:
                            info_password()
                            password = valid_password(password=input('Пароль: _____'))

                        user_db.add_user(email, name, password)









