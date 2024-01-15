# ----------------------------------------- Задача 1 -------------------------------------------------
# Класс Авиабилет должен содержать:
#     - данные о рейсе
#     - дате
#     - месте
#     - стоимости
# Методы должны позволять бронировать билеты, отменять бронь и просматривать доступные рейсы.

# 1. Создать класс со свойствами (file air_ticket.py):
# flight_direction (направление рейса)
# place (место)
# cost (стоимость билета)
#
# Методы класса:
# book_a_ticket (забронировать билет)
# cancel_a_reservation (отменить бронь)
# view_available_flights (посмотреть доступные рейсы)
#
# 2. Данные о направлениях будут записаны в json файл (file flights.json).
# 3. После бронирования будет создан документ с информацией о билете (file booking.txt)
# 4. При отказе от бронирования нужно будет ввести направление рейса и подгрузить данные
# с документа booking.txt и отменить
# 5. Провести проверку на валидность даты и время, и проверку корректности введенных данных



# from air_ticket import AirTicket
# from flights import get_flight, show_flight, choose_a_flight
# from flights import check_the_place, calculate_the_cost, get_booking, is_valid_num
# from setting_the_date import get_data, is_valid_data, get_time
# import random
#
# while True:
#     command = input('''Добро пожаловать на сайт авиакомпании 'ЛЕТУЧИЙ ПОРОХ', чем мы можем помочь?
#
# Просмотреть доступные рейсы выбери 1
# Забронировать рейс выбери 2
# Отменить бронь выбери 3
#
# Выход 0
# _____''')
#
#     match command:
#         case '0':
#             print('Будем ждать Вас снова! До свидания!')
#             break
#         case '1':
#             print('На какую дату проверить рейс, запишите ее в формате дд-мм-гггг?')
#             data = is_valid_data(get_data())
#             while data is False:
#                 print('На эту дату рейсов нет. Выберите другую дату!')
#                 data = is_valid_data(get_data())
#             fly = AirTicket(flight_direction='', departure='', place='', cost='', list_fly=show_flight(get_flight()), num='')
#             fly.view_available_flights()
#         case '2':
#             print('На какой рейс оформить бронь?:')
#             selected_flights = choose_a_flight(get_flight())
#             while selected_flights is False:
#                 print('Рейс не найден. Попробуйте снова.')
#                 selected_flights = choose_a_flight(get_flight())
#
#             print('На какую дату забронировать рейс, запишите ее в формате дд-мм-гггг?')
#             data = is_valid_data(get_data())
#             while data is False:
#                 print('На эту дату рейсов нет. Выберите другую дату!')
#                 data = is_valid_data(get_data())
#             time = get_time(selected_flights)
#
#             print('Выберете посадочное место от 1 до 50:')
#             place = check_the_place()
#             while place is False:
#                 print('Место не найдено. Попробуйте снова!')
#
#             print('Рассчитываем стоимость...3 2 1:')
#             cost = calculate_the_cost(selected_flights)
#             print(f'Стоимость билета: {cost}')
#
#             num_booking = random.randint(100, 999)
#             ticket = AirTicket(selected_flights, f'{data} {time} по мест.вр.', place, cost, list_fly='', num=num_booking)
#             ticket.book_a_ticket()
#
#         case '3':
#             print('Для отмены билета введите номер бронирования.')
#             num_del = is_valid_num(get_booking())
#             while num_del is False:
#                 print('Номер не найден. Попробуйте снова!')
#                 num_del = is_valid_num(get_booking())
#             booking_del = AirTicket(flight_direction='', departure='', place='', cost='', list_fly='', num='')
#             booking_del.del_ticket()







# ----------------------------------------- Задача 2 -------------------------------------------------
# Класс БанковскийАккаунт должен хранить информацию о владельце, балансе

# class ATM:
#     def __init__(self, person, balance):
#         self.person = person
#         self.balance = balance
#
#     def get_info(self):
#         print(f'Держатель счета - {self.person}, баланс счета - {self.balance} рублей.')
#
#
# name1 = ATM('Никифоров Олег Анатольевич', '18000')
# name1.get_info()
#
# name2 = ATM('Епифанцева Екатерина Витальевна', '19000')
# name2.get_info()
#
# name3 = ATM('Лучинин Андрей Олегович', '20000')
# name3.get_info()









