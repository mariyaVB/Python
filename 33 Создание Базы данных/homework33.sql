/*
Создайте таблицу ФИЛЬМЫ
АТРИБУТЫ :
●	id - первичный ключ, автоматически увеличиваемый.
●	title - обязательное поле для заполнения.
●	release_date - дата выхода фильма.
●	genre - жанр фильма.
●	duration - длительность фильма в минутах.
ЗАДАНИЕ:
●	Получить список всех фильмов вместе с их названиями, датами выхода и жанрами.
●	Найти фильмы, вышедшие после 2010 года.
●	Получить список фильмов жанра "Фантастика".
●	Найти фильмы с длительностью более 150 минут.
●	Получить список фильмов, названия которых начинаются на букву "В".
●	Найти фильмы жанра "Боевик", вышедшие до 2005 года.
●	Найти фильмы с длительностью менее 120 минут.
*/

CREATE TABLE IF NOT EXISTS movies (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	release_date DATE NOT NULL,
	genre TEXT NOT NULL,
	duration INTEGER NOT NULL
);

INSERT INTO movies (title, genre, release_date, duration) VALUES
("Пчеловод", "Боевик", "2024-01-31", 96),
("Без Лица", "Боевик", "1997-05-05", 138),
("Аватар", "Фантастика", "2014-07-12", 153),
("В значит Виндетта", "Триллер", "2005-12-11", 132),
("Аквамен 2", "Фантастика", "2023-12-20", 114)

-- Получить список всех фильмов вместе с их названиями, датами выхода и жанрами.
SELECT title, release_date, genre FROM movies;

-- Найти фильмы, вышедшие после 2010 года.
SELECT * FROM movies WHERE strftime ("%Y", release_date) > "2010";

-- Получить список фильмов жанра "Фантастика".
SELECT * FROM movies WHERE genre = "Фантастика";

-- Найти фильмы с длительностью более 150 минут.
SELECT * FROM movies WHERE duration > 150;

-- Получить список фильмов, названия которых начинаются на букву "В".
SELECT * FROM movies WHERE title LIKE "В%";

-- Найти фильмы жанра "Боевик", вышедшие до 2005 года.
SELECT * FROM movies WHERE genre = "Боевик" AND strftime("%Y", release_date) < "2005";

-- Найти фильмы с длительностью менее 120 минут.
SELECT * FROM movies WHERE duration < 120;



/*
Создайте таблицу "Рецепты" со следующими атрибутами:
- id - первичный ключ, автоматически увеличиваемый.
- title - обязательное поле для заполнения, название рецепта.
- author - обязательное поле для заполнения, автор рецепта.
- cuisine - тип кухни, к которой относится рецепт (например, итальянская, японская, мексиканская и т. д.).
- ingredients - обязательное поле для заполнения, список ингредиентов для приготовления.
- instructions - обязательное поле для заполнения, пошаговые инструкции приготовления.
- difficulty - уровень сложности приготовления рецепта (легкий, средний, сложный).

Задача:
1. Получить список всех рецептов вместе с их названиями, авторами и типами кухни.
2. Найти рецепты, где список ингридиентов больше 200 символов.
3. Получить список рецептов Итальянской кухни.
4. Найти рецепты с уровнем сложности "Сложный".
5. Получить список рецептов, названия которых начинаются на букву "П".
6. Найти рецепты автора с именем "Анна".
7. Найти рецепты, использующие помидоры в качестве ингредиента.
*/

CREATE TABLE IF NOT EXISTS receptes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	author TEXT NOT NULL,
	cuisine TEXT NOT NULL DEFAULT "Кухня не указана",
	ingredients TEXT NOT NULL,
	instructions TEXT NOT NULL,
	difficulty TEXT NOT NULL DEFAULT "Уровень сложности не указан"
);

INSERT INTO receptes (title, author, cuisine, ingredients, instructions, difficulty) VALUES
("Авголемоно", "Алексей Зимин", "Греческая", 
"Куриный бульон 2 л, Длиннозерный рис 230 г, Куриное яйцо 4 штуки, Лимонный сок 100 мл,
 Крупная соль по вкусу, Молотый черный перец по вкусу, Листья петрушки по вкусу", 
"1. Вскипятить бульон, убавить огонь до среднего и всыпать рис. Варить 20 минут под неплотно закрытой крышкой.
2. Вмешать сырые яйца, влить лимонный сок и поварить, пока суп не начнет пузыриться.
3. Тогда тщательно перемешать шумовкой и подержать на огне еще 2 минуты, посолить, поперчить и украсить петрушкой.",
"Легкий" ),

("Печенье с шоколадной крошкой", "Анна Олсон", "Европейская", 
"Размягченное несоленое сливочное масло 80гр, Коричневый сахар 50гр, Яйцо 2 шт,
Чайная ложка ванильного экстракта, Мука пшеничная 500гр, Чайная ложка кукурузного крахмала,
Чайная ложка пищевой соды, Чайная ложка соли,  Горький шоколад, нарезанного кусочками 100гр",
"1. Разогрейте духовку до 220ºС.
2. Взбейте сливочное масло и сахар до получения однородной массы. Добавьте яйцо и ваниль и взбейте.
3. Всыпьте муку, кукурузный крахмал, пищевую соду и соль. Всыпьте кусочки шоколада.
4. Выложите столовыми ложками на смазанный маслом противень и выпекайте в течение 8-10 минут, пока края не подрумянятся.
5. Дайте немного остыть и наслаждайтесь.",
"Легкий"),

("Неаполитано", "Адам Джонс", "Итальянская",
"Вода (теплая) 200мл, Дрожжи (моментальные) 10гр, Мука 250гр, Моцарелла 100гр, Пармезан 50гр, 
Соль 1/3 ч.л,  Масло оливковое (первого отжима)30гр  Базилик 10гр Томаты 150гр", 
"1. В емкость для замешивания теста влейте теплую воду, растворите соль, положите дрожжи, размешайте.
2. Влейте столовую ложку оливкового масла. 
3. Просейте муку, замесите тесто, вымешивайте руками достаточно долго, минут 7-10, пока тесто не станет эластичным и не будет липнуть к рукам. 
Подкатайте тесто в шар, накройте пленкой, дайте расстойку в течение 1 часа. 
4. Из подошедшего теста сделайте лепешку, лучше это делать без использования скалки. Просто растягивая руками и формируя круг, готовую лепешку перенесите на лист для выпечки. 
5. Нанесите на основу для пиццы томаты перетертые, делайте это обратной стороны ложки, разравнивая по всей поверхности. 
6. Выложите кусочки моцареллы, разламывая ее просто руками. Посыпьте сверху тертым пармезаном и базиликом. Сбрызните пиццу сверху оливковым маслом, разогрейте духовку до 200 градусов. 
7. Выпекайте пиццу 20-25 минут в зависимости от возможностей вашей духовки. Перед подачей украсьте сверху листиками свежего базилика. Пицца получилась очень вкусная, с тонкой корочкой, это просто песня, а не пицца.",
"Средний"), 

("Паста Поло Песто", "Екатерина Фин", "Итальянская",
"Спагетти 200гр, Вода 2л, Базилик 30гр, Чеснок 1зубч., Кедровые орешки 0.5 стак., Оливковое масло 0.3мл, Соль по вкусу",
"1. Поставьте воду для варки спагетти. Как закипит - посолите (стандарт - 1 ч.л. соли на 1 л воды, но при этому учитывайте и соленость соуса).
2. Соус песто можно взять и магазинный, но домашний, как всегда, натуральнее, вкуснее и дешевле. Сложите в чашу блендера натертый на мелкой терке пармезан, орешки итальянской сосны пинии (их можно заменить кедровыми), нарезанный зубчик чеснока, крупно нарезанный базилик и оливковое масло. Измельчите все до нужной вам консистенции - от кусочков до гладкой пасты, как любите. Попробуйте на соль и остальные вкусы. При необходимости отрегулируйте.
3. Готовые спагетти откиньте на дуршлаг (немного воды оставьте), добавьте спагетти в соус (или наоборот, но так делают очень редко). Перемешайте.
4. Подавайте, свернув спагетти в улитку-горку. Украсьте базиликом, орешками и сыром.",
"Сложный"),

("Солянка мясная", "Константин Ивлев", "Русская",
"Мясной бульон 3л, Ветчина 200гр, Копченая колбаса 200гр, Оливки100гр, Корнишоны (соленые)100гр, Каперсы 50 гр, Лук 1шт.,
Лавровый лист 2шт., Душистый перец (горошины) 3шт., Соль по вкусу, Томаты 5шт, Лимон по вкусу, Сметана по вкусу, Петрушка по вкусу. ",
"1. Начните с приготовления душистого бульона. Говядину берите с косточкой, но с достаточным количеством мяса. Подойдут говяжьи ребрышки, голяшка и другие части мяса. Копченые ребрышки могут быть свиные или говяжьи.
2. Пока варится мясо ветчину нарежьте соломкой, колбасу нарежьте такой же соломкой, корнишоны нарежьте соломкой, говядину охладите, отделите мясо от костей и нарежьте соломкой..
3. В сковороду влейте 3 ст. л. бульона, выложите огурцы и потушите 5-7 минут. Переложите огурцы в кастрюлю с бульоном.
4. В освободившейся сковороде разогрейте сливочное и растительное масло. Обжарьте лук, помешивая, до золотистого цвета.
5. Добавьте перетертые томатны. Перемешайте и жарьте все вместе еще 1 минуту. Переложите зажарку в кастрюлю.
6. Верните в кастрюлю измельченную говядину и копчености. Добавьте оливки и по желанию 50 мл рассола от них. Варите солянку еще 15 минут на медленном огне .
7. В конце по желанию добавьте каперсы.
8. Подавайте с лимоном, сметаной и петрушкой.",
"Сложный")

--1. Получить список всех рецептов вместе с их названиями, авторами и типами кухни.
SELECT title, author, cuisine FROM receptes;

--2. Найти рецепты, где список ингридиентов больше 200 символов.
SELECT * FROM receptes WHERE length(ingredients) > 200;

--3. Получить список рецептов Итальянской кухни.
SELECT  * FROM receptes WHERE cuisine = "Итальянская";

--4. Найти рецепты с уровнем сложности "Сложный".
SELECT * FROM receptes WHERE difficulty = "Сложный";

--5. Получить список рецептов, названия которых начинаются на букву "П".
--SELECT * FROM receptes WHERE title LIKE "П%";

--6. Найти рецепты автора с именем "Анна".
SELECT * FROM receptes WHERE author LIKE "Анна %";

--7. Найти рецепты, использующие помидоры в качестве ингредиента.
SELECT * FROM receptes WHERE ingredients LIKE "%Томаты%"





  


