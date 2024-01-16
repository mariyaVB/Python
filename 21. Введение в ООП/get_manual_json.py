import json


def get_json_tree():
    with open('manual.json', 'r', encoding='utf-8') as manual:
        manual = json.load(manual)
        manual = manual['tree']
    return manual


def get_json_light():
    with open('manual.json', 'r', encoding='utf-8') as manual:
        manual = json.load(manual)
        manual = manual['light']
    return manual


def choice_tree(doc):
    tree_sm = []
    for sm in doc:
        tree_sm.append(sm)
    return tree_sm


def choice_toys(tree, doc):
    for sm, lot in doc.items():
        if tree == sm:
            # return f'Для елки с размером {tree} см лучше выбрать {lot} игрушек'
            return lot
    return 'Не выбрана елка.'


def choice_lights(tree, doc):
    for sm, lot in doc.items():
        if tree == sm:
            # return f'Для елки с размером {tree} см лучше выбрать {lot} игрушек'
            return lot
    return 'Не выбрана елка.'






