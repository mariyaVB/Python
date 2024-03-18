def enter():
    print('\n')


list_category = ['Настольные игры', 'Компьютерные игры']


def choice_category(category_file):
    for category in category_file:
        print(f'🟣 {category}')
    choice = input('Категория товара: _____')

    return choice


def valid_category(category_file, category=None, new_category=None):
    if category is not None:
        if category not in category_file or len(category) == 0:
            print('‼️Категория не найдена')
            return False
        return category

    if new_category is not None:
        if new_category == '':
            return None

        if new_category not in category_file:
            print('‼️Категория не найдена')
            return False
        return new_category


def valid_digit(digit):
    try:
        int(digit)
    except ValueError:
        print('Не может быть строкой.')
        return False

    if int(digit) <= 0:
        print(f'‼️Не может быть 0 или быть отрицательным.')
        return False
    return digit


def valid_text(text):
    if 5 > len(text) >= 0:
        print('‼️ Название должно быть не менее 5 символов.')
        return False
    if text.isdigit() is True:
        print('‼️ Не может содержать одни цифры.')
        return False
    return text


def valid_redaction(variable, func):
    if variable == '':
        print('⤵️Не изменено.')
        return None

    if len(variable) > 0:
        redaction = func
        return redaction


def get_product(list_id):
    choice = input('\nid товара_____')

    for i_id in list_id:
        i_id = str(i_id).rstrip(',)').lstrip('(')
        if choice == i_id:
            print('✅id найден.')
            return choice
    print('‼️id не найден.')
    return False


def show_del_product(del_product):
    for product in del_product:
        return product






