from classes import ChristmasTree, HolidayLights
from get_manual_json import get_json_tree, get_json_light, choice_tree, choice_toys, choice_lights
from valid_file import is_valid_height, is_valid_tree_toys, is_valid_lights, is_valid_modes


def choice_see_tree(tree, lights):
    see_tree = input('Посмотришь на свою елку? 1 - Да, 2 - Нет _____')
    if see_tree == '1':
        return f'{tree.show_tree()} {lights.show_lights()}'
    if see_tree == '2':
        print('Ну и зачем ты ее наряжал тогда? 😒\n')


def change_heights():
    while True:
        change = input(
            '''
            Можно еще изменить высоту елки:
            1 - изменить 
        
            0 - оставить так
            ''')

        match change:
            case '0':
                break

            case '1':
                print(f'Введи новую высоту {choice_tree(get_json_tree())} _____')
                new_height = is_valid_height(get_json_tree())
                while new_height is False:
                    print('Елка не соответствующего размера.🤷‍♀️\n')
                    new_height = is_valid_height(get_json_tree())
                    print('Изменено 👌\n')
                return new_height


def change_toys(h):
    while True:
        change = input(
            '''
            Можно еще изменить количество игрушек:
            1 - изменить 
            
            0 - оставить так
            ''')

        match change:
            case '0':
                break

            case '1':
                print(f'Для елки с размером {h} см лучше выбрать {choice_toys(h, get_json_tree())} игрушек: ')
                new_toys = is_valid_tree_toys(choice_toys(h, get_json_tree()))
                while new_toys is False:
                    print('Не лучший выбор...давай еще 😜')
                    new_toys = is_valid_tree_toys(choice_toys(h, get_json_tree()))
                print('Изменено 👌\n')
                return new_toys


def change_light(h):
    while True:
        change = input(
            '''
            Можно еще изменить длину гирлянды:
            1 - изменить 

            0 - оставить так
            ''')

        match change:
            case '0':
                break

            case '1':
                print(f'Вам подойдет не больше {choice_toys(h, get_json_light())} метров гирлянды.')
                new_light_bulbs = is_valid_lights(choice_lights(h, get_json_light()))
                while new_light_bulbs is False:
                    print('Не лучший выбор...давай еще 😜')
                    new_light_bulbs = is_valid_lights(choice_lights(h, get_json_light()))
                print('Изменено 👌\n')
                return new_light_bulbs


def change_mode():
    while True:
        change = input(
            '''
            Можно еще изменить режим гирлянды:
            1 - изменить 

            0 - оставить так
            ''')

        match change:
            case '0':
                break

            case '1':
                print('Какой режим будет у гирлянды: мерцание, непрерывное свечение?')
                new_glow_modes = is_valid_modes()
                while new_glow_modes is False:
                    print('Есть только два варианта, выбирай из них.')
                    new_glow_modes = is_valid_modes()
                print('Изменено 👌\n')
                return new_glow_modes




