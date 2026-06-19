# Выдать уникальных авторов с любой книгой

```sql
select distinct on (a.id)
	a.first_name,
	a.last_name,
	b.title as any_book
from authors a
join books b on a.id = b.author_id
order by a.id, b.title
```

- distinct on - это расширение SQL именно для PostgreSQL (в чистом SQL такого нет). Его суть: для каждой уникальной комбинации в скобках оставь только одну строку, а какую именно - решает ORDER BY.  В данном случае - "для каждого `a.id` оставь только одну строку"

# Количество книг в каждом жанре

```sql
SELECT genre, COUNT(*) as book_count
from books
group by genre
order by book_count DESC -- сортировка по убыванию
```

# Кто из посетителей чаще брал книгу

```sql
SELECT borrowers.first_name, borrowers.last_name, count(borrowed_books.id) as total_borrowed
from borrowers
join borrowed_books on borrowers.id = borrowed_books.borrower_id
group by borrowers.id, borrowers.first_name, borrowers.last_name
order by total_borrowed DESC
LIMIT 1;
```

# Наиболее часто арендуемые книги

```sql
select books.title, count(borrowed_books.book_id) as total_borrowed
from books
join borrowed_books on books.id = borrowed_books.book_id
group by books.id, books.title
order by total_borrowed DESC
limit 3;
```

# Получить длину имени и фамилии

Для книг (пробно, работает на данных из двух слов)

```sql
select title,
	length(title) as full_length,
	position(' ' in title) as first_word_with_space_length,
	length(title) - position(' ' in title) as second_name_length
from books
```

Учебный пример

```sql
select member_name,
	length(member_name) as full_length,
	position(' ' in member_name) as firstname_with_space_length,
	length(member_name) - position(' ' in member_name) as lastname_length
from familymembers;
```

# Вывести полное имя члена семьи и длину его фамилии

```sql
select member_name,
	LENGTH(member_name) - POSITION(' ' in member_name) as lastname_length
from FamilyMembers;
```

# Найти пользователей с почтой

```sql
select * from users where email ~ '@(outlook\.com|gmail\.com)$'
```

# Поиск по исключению цифр из номеров

```sql
select * from users where phone_number ~ '^[^28]*$';
```

- `[^28]` - не содержит 2 и 8
- `^$` - вся строка
- `*` - сколько угодно раз

# Найти по номеру +7

```sql
select * from users where phone_number ~ '^\.+7';
```

# Группировка данных по типу жилья с количеством записей

```sql
select home_type, COUNT(*) as count_rooms from Rooms group by home_type
```

# Найти первый по алфавиту жанр для каждого автора

```sql
select author, min(genre) as first_genre
from books
group by author;
```

# Подсчёт книг для каждого жанра

```sql
select genre, count(*) as book_count
from books
group by genre
```

# Самая поздняя дата выезда

```sql
select room_id, MAX(end_date) as last_end_date from reservations group by room_id
```

# Найти книгу с самой поздней публикацией

```sql
select title, published_date from books order by published_date desc limit 1;
```

C использованием подзапроса

```sql
select distinct title, published_date
from books
where published_date = (
	select max(published_date)
	from books
)
```

# Вывести данные из одной таблицы при объединении

```sql
SELECT FamilyMembers.* FROM Payments
INNER JOIN FamilyMembers
    ON Payments.family_member = FamilyMembers.member_id

```

# Книги и авторы (разные таблицы)

```sql
select b.title, CONCAT(a.first_name, ' ', a.last_name) as author_fullname from books b
join authors a on b.author_id = a.id
```

### Добавьте одно внутреннее соединение с таблицей **Student**. Объедините по полям **Student_in_class.student** и **Student.id** и вместо идентификатора ученика выведите его имя (поле **first_name**).

```sql
select Class.name, Student.first_name from Class
join student_in_class on class.id = Student_in_class.class
join student on student_in_class.student = Student.id
```

## Получение самого младшего члена семьи (с помощью подзапросов)

```sql
select * from familymembers
where birthday = (select max(birthday) from familymembers)
```

#### Найти имена всех владельцев жилья, которые сами при этом никогда не снимали жилье

1. Получаем список всех владельцев жилья

   ```sql
   select distinct name from users inner join rooms
   on Users.id = Rooms.id
   ```
2. Получаем список id пользователей, снимавших жильё

   ```sql
   select distinct user_id from reservations
   ```
3. Фильтруем список всех владельцев по условию, что id владельца жилья не равен ни одному из идентификаторов пользователей, когда-либо снимавших жильё

   ```sql
   select distinct name from users inner join rooms
   on users.id = rooms.owner_id
   where users.id <> all (
   	select distinct user_id from reservations
   )
   ```

   #### Получить информацию о владельцах жилья стоимостью больше 150 условных единиц:


   ```sql
   select * from users where id IN (
   	select distinct owner_id from rooms where price >= 150
   )
   ```

#### Выведите названия товаров из таблицы Goods (поле **good_name**), которые ещё ни разу не покупались ни одним из членов семьи (таблица **Payments**).

```sql
select good_name from goods where good_id NOT IN (
	select good from payments
)
```

#### Информация о всех бронированиях, где цена жилья на момент брони соответствует текущей стоимости жилья:

```sql
select * from reservations
where (room_id, price) in (select id, price from rooms)
```

тот же запрос в другом стиле

```sql
select Reservations.* from Reservations
inner join Rooms
on Reservations.room_id = Rooms.id
where reservations.price = Rooms.price
```

#### Выведите список комнат (все поля, таблица **Rooms**), которые по своим удобствам (**has_tv, has_internet, has_kitchen, has_air_con**) совпадают с комнатой с идентификатором "11".

```sql
select * from rooms where (has_tv, has_kitchen, has_air_con) IN 
(select has_tv, has_kitchen, has_air_con from rooms where id = 11)
```

аналог

```sql
SELECT * 
FROM rooms 
WHERE has_tv = (SELECT has_tv FROM rooms WHERE id = 11)
  AND has_internet = (SELECT has_internet FROM rooms WHERE id = 11)
  AND has_kitchen = (SELECT has_kitchen FROM rooms WHERE id = 11)
  AND has_air_con = (SELECT has_air_con FROM rooms WHERE id = 11)
  AND id != 11;
```

#### Имена членов семьи и сумма их самого дорогого товара

```sql
select Familymembers.member_name, (
	select MAX(unit_price) from Payments where Payments.family_member = FamilyMembers.member_id
) as good_price
from FamilyMembers;
```

#### Все полёты компании Aeroflot (табличное выражение)

```sql
with aeroflot_trips as
	(select plane, town_from, town_to) from company
		inner join trip on Trip.company = Company.id where name = 'Aeroflot')

select * from Aeroflot_trips;
```

с книгами

```sql
with books_items (one, two, three) AS (
	select title, CONCAT(authors.first_name, ' ', authors.last_name) as author, published_date from books
	join authors on authors.id = books.author_id
)

select one, two, three from books_items;
```

## Вывести возраст (с помощью case)

```sql
select first_name, last_name, 
	(case
		WHEN extract(year from age(now(), birth_date)) >= 18 THEN 'Совершеннолетний'
		else 'Несовершеннолетний'
	end as strange)
from authors
```

## Определить принадлежность ученика в этапу образования

```sql
SELECT name,
CASE
	-- Извлекаем номер класса из его названия и проверяем вхождение
	WHEN SUBSTRING(name, 1, POSITION(' ' IN name) - 1) IN ('10', '11') THEN 'Старшая школа'
	WHEN SUBSTRING(name, 1, POSITION(' ' IN name) - 1) IN ('5', '6', '7', '8', '9') THEN 'Средняя школа'
	ELSE 'Начальная школа'
END AS stage
FROM Class
```

В другом стиле:

```sql
SELECT name,
CASE SUBSTRING(name, 1, POSITION(' ' IN name) - 1)
  WHEN '11' THEN 'Старшая школа'
  WHEN '10' THEN 'Старшая школа'
  WHEN '9' THEN 'Средняя школа'
  WHEN '8' THEN 'Средняя школа'
  WHEN '7' THEN 'Средняя школа'
  WHEN '6' THEN 'Средняя школа'
  WHEN '5' THEN 'Средняя школа'
  ELSE 'Начальная школа'
END AS stage
FROM Class

```

Альтернативный вариант

```sql
SELECT 
    name,
    CASE
        WHEN SUBSTRING(name FROM '^\d+') IN ('10', '11') THEN 'Старшая школа'
        WHEN SUBSTRING(name FROM '^\d+')IN ('5', '6', '7', '8', '9') THEN 'Средняя школа'
        ELSE 'Начальная школа'
    END AS stage
FROM Class;
```

Отделение имени (для себя)

```sql
with test AS (select concat(first_name, ' ', last_name) as full_name from authors)

select substring(full_name, 1, position(' ' IN full_name) -1) as name from test
```

## Категоризация жилья по цене

```sql
select id, price, 
	CASE WHEN price >= 150 THEN 'Комфорт-класс' ELSE 'Эконом-класс' END AS category
	FROM Rooms
```

## Проверка на boolean

```sql
SELECT id, has_tv::text FROM Rooms;
```

```sql
select id, (
CASE 
    WHEN has_tv THEN 'YES' 
    ELSE 'NO' 
END

) as has_tv from Rooms
```

#### Заменить в таблице пустые строки на NULL, существующие значения оставить без изменений

```sql
update books set
genre = nullif(genre, '')
```

#### Подготовка данных для сравнения

Агрегатные функции (count, avg, sum) игнорируют null. Если есть заглушки вроде 0 или '', которые портят статистику, их превращают в null

```sql
select avg(nullif(rating, 0)) from reviews;
```

#### Первичный ключ при добавлении новой записи

```sql
insert into goods select max(good_id) + 1, 'Table', 2 from goods;
```

#### Вставка записи с подзапросом

```sql
insert into goods (good_id, good_name, type)
select
	(select coalesce(max(good_id), 0) + 1 FROM Goods),
	'Table',
	gt.good_type_id
from Goodtypes gt
where gt.good_type_name = 'equipment';
```

#### Практика с транзакциями

```sql
-- begin;

-- update books set
-- genre = 'Фантастика'
-- where id = 44;

-- SAVEPOINT step1;

-- select genre from books where id = 44

-- rollback;

-- rollback to savepoint step1;

-- commit;
```

### Удалить все бронирования жилья, в котором отсутствует кухня

```sql
delete from reservations
using rooms
where reservations.room_id = rooms.id
and rooms.has_kitchen = false;
```

### Удаление нескольких таблиц одновременно в PostgreSQL (транзакции)

```sql
begin;
delete from reservations
using rooms
where reservations.room_id = rooms.id
and rooms.has_kitchen = false;

delete from rooms
where rooms.has_kitchen = false;
commit;
```

#### Измените запрос так, чтобы удалить товары (Goods), имеющие тип деликатесов (delicacies)

```sql
DELETE FROM Goods 
USING GoodTypes
WHERE GoodTypes.good_type_id = Goods.type
AND Goodtypes.good_type_name = 'delicacies'

```

## Cравнение разных типов (если user_id - строка)

```sql
where cast(user_id as int) = 123;
```

## Определение возраста

```sql
select extract(year from age(now(), '1996-12-18 06:00:00'))
```

## Извлечь час из времени

```sql
SELECT extract(hour from TIME '14:30:45') AS hour_value
```

#### Выведите имена (поле **member_name**) и возраст для каждого человека из таблицы **FamilyMembers**

```sql
select member_name, extract(year from age(now(), birthday)) as age
from FamilyMembers;
```
