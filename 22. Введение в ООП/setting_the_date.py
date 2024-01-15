import json
from datetime import datetime as dt


def get_time(selected_fly):
    try:
        with open('flights.json', encoding='utf-8') as data:
            data = json.load(data)
            data = data['flights']
            for flight in data:
                if selected_fly == flight:
                    return data[flight][data[flight].find(' ')+1:data[flight].find(' ')+6]
    except (ValueError, AttributeError, SyntaxError):
        return False


def get_data():
    datas = input(str('_____'))
    return datas


def is_valid_data(data, params="%d-%m-%Y"):
    try:
        data_valid = dt.strptime(data, params)
        if data_valid.date() <= dt.now().date():
            return False

        return data
    except (ValueError, AttributeError):
        return False





