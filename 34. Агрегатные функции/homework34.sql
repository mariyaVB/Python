/*
***Задание: Анализ данных сотрудников***

Создайте таблицу `Employees` со следующими столбцами:
- `employee_id` - идентификатор сотрудника (уникальный ключ)
- `department_id` - идентификатор отдела, к которому относится сотрудник
- `employee_name` - имя сотрудника
- `salary` - заработная плата сотрудника
- `hire_date` - дата приема на работу

Вам нужно выполнить любые 5 запросов:
1. Определить общее количество сотрудников в компании.
2. Рассчитать среднюю заработную плату в компании.
3. Определить количество сотрудников в каждом отделе.
4. Найти самую высокооплачиваемую должность.
5. Рассчитать общую сумму затрат на заработную плату для каждого отдела.
6. Найти средний стаж работы сотрудников в компании.
7. Определить месяц с наибольшим числом наймов сотрудников.
*/

CREATE TABLE IF NOT EXISTS Employees (
	employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
	department_id TEXT NOT NULL,
	employee_name TEXT NOT NULL,
	salary REAL CHECK (salary > 0),
	hire_date DATE NOT NULL
);

INSERT INTO Employees (department_id, employee_name, salary, hire_date) VALUES
("Автотранспортный цех", "Иванов Иван Иванович", 35000, "2013-01-19"),
("Автотранспортный цех", "Петров Петр Петрович", 28500, "2020-05-01"),
("Автотранспортный цех", "Сидоров Сидор Сидорович", 33000, "2015-11-27"),
("Администрация", "Николаев Николай Николаевич", 43000, "2013-10-10"),
("Администрация", "Ленина Елена Васьльевна", 50000 , "2008-04-07"),
("Администрация", "Васильева Татьяна Петровна", 37000 , "2023-05-01"),
("Ремонтный цех", "Кузьмин Кузьма Кузьмич", 38000 , "2010-09-20")


--1. Определить общее количество сотрудников в компании.
SELECT COUNT(employee_id) as "Всего сотрудников" FROM Employees;

--2. Рассчитать среднюю заработную плату в компании.
SELECT AVG(salary) as "Средняя заработная плата" FROM Employees;

--3. Определить количество сотрудников в каждом отделе.
SELECT COUNT(employee_id) as "Kоличество сотрудников ",  department_id  as "Oтдел"
FROM Employees
GROUP BY department_id;

--4. Найти самую высокооплачиваемую должность.
SELECT department_id,  MAX(salary) FROM Employees;

--5. Рассчитать общую сумму затрат на заработную плату для каждого отдела.
SELECT SUM(salary) as "Зарплата общая",   department_id  as "Oтдел"
FROM Employees
GROUP BY department_id

--6. Найти средний стаж работы сотрудников в компании.
SELECT AVG((JulianDay("2024-02-28") - JulianDay(hire_date)))  as "Средний стаж в днях" FROM Employees

--7. Определить месяц с наибольшим числом наймов сотрудников.
SELECT COUNT(employee_id) as "Количество наймов", strftime("%m", hire_date) as "Месяц"
FROM Employees
GROUP BY strftime("%m", hire_date)
ORDER BY COUNT(employee_id) DESC LIMIT  1;


/*
***Задание: Анализ продаж***

У вас есть таблица `Sales`, содержащая информацию о продажах различных товаров в разных магазинах. 

Вам нужно выполнить любые 5 запросов:
1. Найти общее количество проданных товаров за весь период.
2. Рассчитать общую сумму выручки за весь период.
3. Определить самый популярный товар (товар с наибольшим количеством продаж).
4. Рассчитать общее количество продаж по месяцам.
5. Найти месяц с наибольшим объемом продаж.
6. Рассчитать общую сумму выручки и количество проданных товаров для каждого магазина.
7. Рассчитать средний чек (среднюю сумму покупки) в каждом магазине.
8. Определить товары, проданные только в определенном магазине.
*/

CREATE TABLE  IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    store_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price REAL
);

INSERT INTO Sales (product_id, store_id, sale_date, quantity, price) VALUES
(1, 711, "2024-02-28", 1, 750),
(2, 711, "2024-02-28", 1, 250),
(3, 711, "2024-02-29", 2, 125),
(1, 5, "2024-02-28", 1, 350),
(3, 5, "2024-02-29", 3, 125)
(2, 5, "2024-03-01", 1, 250)

--Найти общее количество проданных товаров за весь период.
SELECT SUM(quantity) FROM Sales;

--Рассчитать общую сумму выручки за весь период.
SELECT SUM(quantity * price) FROM Sales;

--Определить самый популярный товар (товар с наибольшим количеством продаж).
SELECT SUM(quantity) as "Количество", product_id as "ID товара"
FROM Sales
GROUP BY product_id
ORDER BY COUNT(product_id) DESC LIMIT  1;

-- Рассчитать общее количество продаж по месяцам.
SELECT COUNT(id) as "Количество продаж", strftime("%m", sale_date) as "Месяц"
FROM Sales
GROUP BY strftime("%m", sale_date);

--Найти месяц с наибольшим объемом продаж.
SELECT SUM(quantity * price) as "Обьем продаж",  strftime("%m", sale_date) as "Месяц"
FROM Sales
GROUP BY strftime("%m", sale_date)
ORDER BY COUNT(product_id) DESC LIMIT  1;

--Рассчитать общую сумму выручки и количество проданных товаров для каждого магазина.
SELECT SUM(quantity * price) as "Сумма общая", SUM(quantity) as "Количество товаров", store_id as "Магазин"
FROM Sales
GROUP BY store_id

--Рассчитать средний чек (среднюю сумму покупки) в каждом магазине.
SELECT SUM(quantity * price) / SUM(quantity) as "Средняя сумма покупки", store_id as "Магазин"
FROM Sales
GROUP BY store_id

--Определить товары, проданные только в определенном магазине.
SELECT product_id as "ID товара", store_id as "Магазин"
FROM Sales
WHERE store_id = 5





