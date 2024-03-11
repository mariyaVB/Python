# 1.	Создать таблицу "Студенты" с полями: Имя, Фамилия, Возраст, Группа.

import sqlite3 as sql

with sql.connect('students.db') as connect:
    students = connect.cursor()
    students.execute("""CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    faculty TEXT)""")

print('База данных "Студенты" создана.')


def add_student(cur, name, age, faculty):
    cur.execute(f'INSERT INTO Students(name, age, faculty) VALUES ("{name}", "{age}", "{faculty}")')

    # with sql.connect('students.db') as con:
    #     cur = con.cursor()
    #     add_student(cur, name, age, faculty)


while True:
    command = input('''
    1 = Добавить запись в таблицу
    0 = Выход''')

    match command:
        case '1':
            name_student = input('Введите имя студента: _____')
            age_student = int(input('Введите возраст студента: _____'))
            while age_student < 11:
                print('В Хогвартс принимают с 11 лет.')
                age_student = int(input('Введите возраст студента: _____'))

            def choice_faculty():
                for fac in ['🦁Гриффиндор', '🦅 Когтевран', '🦫 Пуфендуй', '🐍 Слизерин']:
                    print(f'{fac}')
                    choice = input('Выбрать этот факультет? 1 = Да | 2 = Нет | 0 = Выход\nОтвет _____')
                    if choice == '1':
                        return fac
                    if choice == '2':
                        pass
                    if choice == '0':
                        return 0
            faculty_student = choice_faculty()

            with sql.connect('students.db') as con:
                cur = con.cursor()
                add_student(cur, name_student, age_student, faculty_student)

        case '0':
            break



