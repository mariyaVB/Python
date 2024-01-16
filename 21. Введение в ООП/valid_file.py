from get_manual_json import get_json_tree, get_json_light, choice_tree, choice_toys, choice_lights


def is_valid_height(doc):
    try:
        choice_height = input('Укажи высоту елки в сантиметрах _____')
        if choice_height in doc:
            return choice_height

        return False
    except (ValueError, AttributeError, SyntaxError):
        return False


def is_valid_tree_toys(doc):
    tree_toys = int(input('Укажи количество елочных игрушек _____'))
    try:
        if int(doc[:3]) <= tree_toys <= int(doc[5:]):
            return tree_toys

        return False
    except (ValueError, AttributeError, SyntaxError):
        return False


def is_valid_lights(doc):
    lights = int(input('Сколько метров выбрали? _____'))
    try:
        if lights <= int(doc):
            return lights

        return False
    except (ValueError, AttributeError, SyntaxError):
        return False


def is_valid_modes():
    modes = input('Ваш выбор _____')
    try:
        if modes == 'мерцание' or modes == 'непрерывное свечение':
            return modes

        return False
    except (SyntaxError, NameError):
        return False




