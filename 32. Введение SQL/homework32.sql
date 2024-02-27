/*
1. Создать таблицу группа (имя, рейтинг, курс):
- добавить 3 любые группы
- показать группы(имя, рейтинг и курс)  рейтинг, которых меньше либо равен 50
*/
CREATE  TABLE IF NOT EXISTS team (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	rating INTEGER DEFAULT 0 CHECK (0 <= rating <= 100),
	faculty TEXT DEFAULT "Gryffindor"
);

INSERT INTO team (name, rating) VALUES
("Гарри Поттер", 89),
("Рон Уизли", 82),
("Гермиона Грейнджер", 100)
("Невилл Долгопупс", 50)

SELECT * FROM team WHERE rating <= 50;


/*
2. Создать таблицу игры (имя игры, дата и время сохранения)
- добавить 3 любые игры 
- показать все записи игр
*/

CREATE TABLE IF NOT EXISTS games (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title_game TEXT NOT NULL,
	saving DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO games (title_game) VALUES
("The Last of Us Part II"),
("Uncharted 4: A Thief's End"),
("Ghost of Tsushima")

SELECT * FROM games


/*
3. Создать таблицу занятие (тип, дата, стоимость)
- добавить 3 любых занятия
- показать все занятия, тип которых соответствует английский
*/

CREATE TABLE IF NOT EXISTS classes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	lesson TEXT NOT NULL,
	start_lesson DATETIME NOT NULL,
	price_lesson REAL NOT NULL CHECK (price_lesson > 0)
);

INSERT INTO classes (lesson, start_lesson, price_lesson) VALUES
("Физическая химия", "2024-02-28 12:00:00",  1850),
("Сапромат", "2024-03-01 08:30:00",  1550),
("Английский", "2024-03-04 10:15:00",  1500)

SELECT * FROM classes WHERE lesson = "Английский"
 




