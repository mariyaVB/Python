import json


def get_flight():
    with open('flights.json', encoding='utf-8') as flights:
        dict_flights = json.load(flights)
        dict_flights = dict_flights['flights']
    return dict_flights


def show_flight(dict_flights):
    list_flights = []
    for fly, time in dict_flights.items():
        list_flights.append(f'{fly} : {time}')

    return f'''{list_flights[0]}{'\n'}{list_flights[1]}{'\n'}{list_flights[2]}
{list_flights[3]}{'\n'}{list_flights[4]}{'\n'}Рейсы ежедневные.'''


def choose_a_flight(flights):
    for fly, time in flights.items():
        print(f'{fly} : {time}')
    choice = input(str('Выберите рейс, скопируйте только направление: _________________'))
    selected_flight = choice
    if choice in flights:
        return selected_flight
    else:
        return False


def check_the_place():
    location = int(input('Место_____'))
    try:
        if 1 < location > 50:
            return False
        return location
    except (ValueError, AttributeError, SyntaxError):
        return False


def calculate_the_cost(flights):
    if flights == 'Красноярск - Пхукет':
        cost = '61000 Rub'
        return cost
    if flights == 'Иркутск - Себу':
        cost = '54000 Rub'
        return cost
    if flights == 'Москва - Кариба':
        cost = '37000 Rub'
        return cost
    if flights == 'Владивосток - Токио':
        cost = '26000 Rub'
        return cost
    if flights == 'Новосибирск - Нячанг':
        cost = '73000 Rub'
        return cost


def get_booking():
    with open('booking.txt', 'r', encoding='utf-8') as t:
        text_booking = t.readlines()

    return text_booking


def is_valid_num(book):
    try:
        num_booking = input('Ваш номер бронирования _____')
        text = list(map(lambda el: el.strip('\n'), book))
        for el_text in text:
            if el_text == f'Номер бронирования: {num_booking}':
                return True
        return False
    except (ValueError, SyntaxError):
        return False



















