import json


class AirTicket:
    def __init__(self, flight_direction, departure, place, cost, list_fly, num):
        self.flight_direction = flight_direction
        self.departure = departure
        self.place = place
        self.cost = cost
        self.list_fly = list_fly
        self.num = num

    def view_available_flights(self):
        print(self.list_fly)

    def del_ticket(self):
        f = open('booking.txt', 'w', encoding='utf-8')
        f.close()
        print('Ваш билет удален!')

    def book_a_ticket(self):
        text_book = f'Номер бронирования: {self.num}\n'
        text_book2 = f'Рейс: {self.flight_direction} Вылет: {self.departure} Место: {self.place} Стоимость: {self.cost}'

        with open('booking.txt', 'w', encoding='utf-8') as t:
            t.write(text_book)
            t.write(text_book2)
        print(f'Ваш билет сохранен в документ booking.txt, номер вашего бронирования {self.num}.\n')













