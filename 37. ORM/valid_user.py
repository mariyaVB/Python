import re
# from homework37 import *


def write_round(objects):
    for obj in objects:
        return str(obj).lstrip('(').rstrip(',)')


def valid_name(name=None, new_name=None):
    if name is not None:
        if len(name) <= 5:
            print('Не может путь пустым. Длина имени должна быть более 5 символа')
            return False

        return name

    if new_name is not None:
        if len(new_name) == 0:
            print('⤵️Не изменено.')
            return None

        if 5 > len(new_name) > 0:
            print('Длина имени должна быть более 5 символа')
            return False

        return new_name


def valid_email(email):
    pattern = r"(\w+)(@mail.ru)|(\w+)(@gmail.com)|(\w+)(@yandex.ru)"
    if re.fullmatch(pattern, email):
        return email
    return False


def valid_password(password=None, new_password=None):
    if password is not None:
        pattern = r"([A-Za-z0-9]{8,})"
        if re.fullmatch(pattern, password):
            return password
        return False

    if new_password is not None:
        if len(new_password) == 0:
            print('⤵️Не изменено.')
            return None

        else:
            pattern = r"([A-Za-z0-9]{8,})"
            if re.fullmatch(pattern, new_password):
                return new_password
            return False


def info_mail():
    print('Почта должна быть @mail.ru, @gmail.com, @yandex.ru')


def info_password():
    print('Пароль должен содержать: '
          '🟣 минимум одну большую букву'
          '🟣 длина минимум 8 символов')


def check_entrance(mail, password, list_mail):
    for i_mail in list_mail:
        if mail in i_mail:
            if password in i_mail:
                return True

    return False



# f = user_db.show_user()
# check_entrance('vikkirot23@mai.ru', 'ldjY5732', f)