-- Творческое задание Фитнесс клуб
-- Есть таблицы:
-- 🟣 Учета тренеров Trainer
-- 🟣 Учета клиентов Clients
-- 🟣 Учета фитнесс программ Fitness

-- Создаем таблицу Timetable со связью "Многие ко Многим", в  ней будет информация о тренировке, какой тренер будет проводить, и дата занятия
-- Создаем таблицу Abonnement со связью "Многие ко Многим", в  ней будет информация о клиенте и на какую тренировку он записан  по расписанию

-- Написать запросы:
--Получить все записи расписания тренровок 
--Получить список всех тренировок у каждого клиента
--Получить список тренировок, длительность которых больше 45
--Получить список дат, на которые еще не назначены тренировки
--Получить список клиентов которые еще не записались на тренировки
--Получить общее количество тренировок на каждого тренера
--Получить список всех тренировок с указанием ведущего тренера и учавствующих клиентов
--Получить количество клиентов записавшихся на тренировки 2024 - 03 - 12
--Получить список всех тренировок, отсортированных по количеству участников
--Получить клиента  с наибольшим количеством посещений

CREATE TABLE IF NOT EXISTS Trainer
(
  id_trainer INTEGER PRIMARY KEY AUTOINCREMENT,
  name_trainer TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS  Fitness
(
  id_fitness INTEGER PRIMARY KEY AUTOINCREMENT,
  title_fitness TEXT NOT NULL,
  duration INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS  Timetable
(
  id_timetable INTEGER PRIMARY KEY AUTOINCREMENT,
  date_fitness DATE,
  fitness INTEGER DEFAULT NULL,
  trainer INTEGER DEFAULT NULL,
  FOREIGN KEY (fitness) REFERENCES Fitness(id_fitness),
  FOREIGN KEY (trainer) REFERENCES Trainer(id_trainer)
);

CREATE TABLE IF NOT EXISTS  Clients
(
  id_client INTEGER PRIMARY KEY AUTOINCREMENT,
  name_client TEXT NOT NULL
);

CREATE TABLE  IF NOT EXISTS  Abonnement
(
  timetable INTEGER DEFAULT NULL,
  client INTEGER NOT NULL,
  FOREIGN KEY (timetable) REFERENCES Timetable(id_timetable),
  FOREIGN KEY (client) REFERENCES Clients(id_client)
);

INSERT INTO Trainer (name_trainer) VALUES 
('Hange Zoe'),
('Erwin Smith'),
('Levi Ackermann');

INSERT INTO Fitness (title_fitness, duration) VALUES 
('Yoga', 60),
('Pilates', 45),
('Circuit Training', 60);

INSERT INTO Timetable (date_fitness, fitness, trainer) VALUES 
('2024-03-11', 1, 1),
('2024-03-12', 1, 1),
('2024-03-12', 2, 2),
('2024-03-12', 3, 3),
('2024-03-13', 2, 3),
('2024-03-13', 3, 2),
('2024-03-14', 3, NULL),
('2024-03-15', NULL, NULL);
 
INSERT INTO Clients (name_client) VALUES 
('Sasha Braus'),
('Rainer Braun'),
('Mikasa Ackermann'),
('Eren Jaeger'),
('Armin Arlert'),
('Annie Leonhart');

INSERT INTO Abonnement (client, timetable) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(3, 5),
(5, 6),
(6, NULL),
(4, 3);


--Получить все записи расписания тренровок 
SELECT * FROM Timetable

--Получить список всех тренировок у каждого клиента
SELECT Clients.name_client as "Имя клиента", Fitness.title_fitness  as "Название тренировки", Timetable.date_fitness as "Дата тренировки" FROM Abonnement
JOIN Clients ON client = Clients.id_client
JOIN Timetable ON timetable = Timetable.id_timetable
JOIN Fitness ON fitness = Fitness.id_fitness

--Получить список тренировок и  дату, с назначенным тренером и длительностью больше 45
SELECT date_fitness as "Дата тренировки", trainer as "Имя тренера", title_fitness  as "Название тренировки", duration as "Продолжительность" FROM Timetable
JOIN Fitness ON fitness = Fitness.id_fitness
WHERE duration > 45 and trainer IS NOT NULL

--Получить список дат с NULL если у них еще не назначены тренировки, или тренер.
SELECT date_fitness as "Дата тренировки", name_trainer as "Имя тренера", title_fitness  as "Название тренировки" FROM Timetable
LEFT JOIN Trainer ON trainer = Trainer.id_trainer
LEFT JOIN Fitness ON fitness = Fitness.id_fitness
WHERE fitness IS NULL OR trainer IS NULL

--Получить список клиентов которые еще не записались на тренировки
SELECT name_client as "Имя клиента" FROM Abonnement
LEFT JOIN Clients ON client = Clients.id_client
WHERE timetable IS NULL

--Получить общее количество тренировок на каждого тренера
SELECT COUNT(fitness) as "Общее количество тренировок", name_trainer as "Имя тренера" FROM Timetable
JOIN Trainer ON trainer = Trainer.id_trainer
GROUP BY trainer

--Получить список всех тренировок с указанием ведущего тренера и учавствующих клиентов
SELECT date_fitness as "Дата тренировки", title_fitness as "Название тренировки", name_trainer as "Имя тренера", name_client as "Записавшиеся клиенты" FROM Abonnement
JOIN Clients ON client = Clients.id_client
JOIN Timetable ON timetable = Timetable.id_timetable
JOIN Trainer ON trainer = Trainer.id_trainer
JOIN Fitness ON fitness = Fitness.id_fitness
ORDER BY name_client ASC

--Получить количество клиентов записавшихся на тренировки 2024-03-12
SELECT COUNT(client) as "Записавшиеся клиенты", date_fitness as "Дата тренировки" FROM Abonnement
JOIN Timetable ON timetable = Timetable.id_timetable
WHERE date_fitness = "2024-03-12"

--Получить список всех тренировок, отсортированных по количеству участников
SELECT COUNT(id_client) as "Общее количество записавшихся клиентов", title_fitness as "Название тренировки" FROM Abonnement
JOIN Timetable ON timetable = Timetable.id_timetable
JOIN Clients ON client = Clients.id_client
JOIN Fitness ON fitness = Fitness.id_fitness
GROUP BY title_fitness

--Получить клиента  с наибольшим количеством посещений
SELECT name_client  as "Имя клиентa", COUNT(timetable) as "Общее количество тренировок" FROM Abonnement
JOIN Clients ON client = Clients.id_client
GROUP BY name_client
ORDER BY COUNT(timetable)  DESC LIMIT 2

