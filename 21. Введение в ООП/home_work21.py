# ------------------------------------------ Задача 1 --------------------------------------------------------------
# реализовать класс
# 	Класс ChristmasTree
# ●	Атрибуты: высота, количество игрушек.
# ●	Методы: decorate_tree(new_decorations), grow_tree(new_height).
# ●	НЕОБЯЗАТЕЛЬНО: Интерфейс для украшения ёлки и изменения её высоты.

# ------------------------------------------ Задача 2 --------------------------------------------------------------
# реализовать класс
# 	Класс HolidayLights
# ●	Атрибуты: количество лампочек, режимы свечения.
# ●	Методы: change_mode(new_mode), add_lights(new_lights).
# ●	НЕОБЯЗАТЕЛЬНО: Интерфейс для изменения режимов свечения и добавления лампочек.

# ----------------------------------------- Интерфейс ---------------------------------------------------------------
from classes import ChristmasTree, HolidayLights
from get_manual_json import get_json_tree, get_json_light, choice_tree, choice_toys, choice_lights
from valid_file import is_valid_height, is_valid_tree_toys, is_valid_lights, is_valid_modes
from see_tree import choice_see_tree, change_heights, change_toys, change_mode, change_light






while True:
    command = input(
'''Украшение елки:
1 - украсить елку

0 - выход
_____''')
    match command:
        case '0':
            print('Пока 👋')
            break

        case '1':
            print(f'Выбери елку: {choice_tree(get_json_tree())}')
            height = is_valid_height(get_json_tree())
            while height is False:
                print('Елка не соответствующего размера.🤷‍♀️\n')
                height = is_valid_height(get_json_tree())
            print('Идем дальше!👉\n')

            print(f'Для елки с размером {height} см лучше выбрать {choice_toys(height, get_json_tree())} игрушек: ')
            tree_toys = is_valid_tree_toys(choice_toys(height, get_json_tree()))
            while tree_toys is False:
                print('Не лучший выбор...давай еще 😜')
                tree_toys = is_valid_tree_toys(choice_toys(height, get_json_tree()))
            print('Отлично!!! Осталась гирлянда, вперед... 👉\n')

            print(f'Вам подойдет не больше {choice_toys(height, get_json_light())} метров гирлянды.')
            light_bulbs = is_valid_lights(choice_lights(height, get_json_light()))
            while light_bulbs is False:
                print('Не лучший выбор...давай еще 😜')
                light_bulbs = is_valid_lights(choice_lights(height, get_json_light()))
            print('Итак...последнее!👉\n')

            print('Какой режим будет у гирлянды: мерцание, непрерывное свечение?')
            glow_modes = is_valid_modes()
            while glow_modes is False:
                print('Есть только два варианта, выбирай из них.')
                glow_modes = is_valid_modes()
            print('Ураааа!!!! На елка готова 🎄')

            my_tree = ChristmasTree(height, tree_toys)
            my_light = HolidayLights(light_bulbs, glow_modes)
            see_tree = choice_see_tree(my_tree, my_light)

            new_height = change_heights()
            my_tree.grow_tree(new_height)
            new_toy = change_toys(new_height)
            my_tree.decorate_tree(new_toy)
            new_light_bulbs = change_light(new_height)
            my_light.add_light_bulbs(new_light_bulbs)
            new_glow_modes = change_mode()
            my_light.change_glow_modes(new_glow_modes)

            see_new_tree = choice_see_tree(my_tree, my_light)











