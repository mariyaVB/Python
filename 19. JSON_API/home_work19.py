# ----------------------------------------------- Задача ---------------------------------------------------------------
# 1. выберите апи из предложенных или предложите свой
# 2. укажите цель(пример. Хочу создать папку “название фильма”, поместить в нее текстовый файл(.txt) с информацией о фильме)
# 3. Напишите код
# 4. в отчете к дз, укажите что за апи вы выбрали и вашу цель
#
# Цель может быть любой, какую вы заходите, но она должно соответствовать следующим параметрам:
# 1. У вас должна программа написанная на языке python
# 2. Результат этой программы должен формировать текстовый или графический файл


# !!!!!!!!!!!!!!!!!!!!!!!! Ознакомиться с созвездиями (параметр функции указывать на латинице) !!!!!!!!!!!!!!!!!!!!!!!!!!
# signs =
# aquarius - водолей
# pisces - рыбы
# aries - овен
# taurus - телец
# gemini - близнецы
# cancer - рак
# leo - лев
# virgo - дева
# libra - весы
# scorpio - скорпион
# sagittarius - стрелец
# capricorn - козерог
#



import requests
import os
from datetime import datetime

def horoscope(signs):
    # 1 Получение json гороскопа
    url_text = f'https://ohmanda.com/api/horoscope/{signs}'
    everyday_horoscope = requests.get(url_text).json()

    # 2 Получение json картинки
    key = 'key=41343447-da8c8ea5af539d5968656af71'
    name_img = f'q=signs+{signs}'
    type_img = 'image_type=illustration'
    url_img = f'https://pixabay.com/api/?{key}&{name_img}&{type_img}&category=abstraction&per_page=3'
    sign_img = requests.get(url_img).json()
    list_img = sign_img['hits']
    dict_img = list_img[1]
    img = dict_img['webformatURL']

    # 3 переменная даты
    data = datetime.now().strftime("%m-%d-%Y")

    # 4 Создание папок и файлов
    if not(os.path.exists('Ежедневный гороскоп')):
        os.mkdir('Ежедневный гороскоп')
        horoscope_txt = open(f'Ежедневный гороскоп\\{signs}-{data}.txt', 'w')
        horoscope_txt.close()

    with open(f'Ежедневный гороскоп\\{signs}-{data}.txt', 'w', encoding= 'utf-8') as f:
        f.write(f'Гороскоп на {data}:' + '\n' + everyday_horoscope['horoscope'])

    end = requests.get(img)
    if end.status_code == 200:
        with open(f'Ежедневный гороскоп\\{signs}{data}.jpg', 'wb') as i:
            i.write(end.content)

    return 'Ваш гороскоп находится в папке Ежедневный гороскоп.'



print(horoscope('capricorn')) # Указать созвездие на латинице



