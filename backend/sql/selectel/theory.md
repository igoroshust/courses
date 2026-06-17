# Cоздание таблиц

SQL делится на:

- DDL (Data Definition Language) - управление структурой (CREATE, ALTER, DROP)
- DML (Data Manipulation Language) - работа с данными (SELECT, INSERT, UPDATE, DELETE)
- DCL (Data Control Language) - управление доступом (GRANT, REVOKE, DENY)

**Создание таблицы books**

```sql
 CREATE TABLE books (
	id SERIAL PRIMARY KEY, -- можно id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
	title VARCHAR(100) NOT NULL,
	author VARCHAR(100) NOT NULL,
	published_date DATE,
	available BOOLEAN DEFAULT TRUE
);
```

- id - первичный ключ
- serial - значение для этого поля генерируется автоматически при создании новой записи
- INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY - лучше использовать эту запись для новых версию PostgreSQL, это стандарт SQL и он ведёт себя предсказуемее

**Добавление столбца**

```sql
ALTER TABLE books ADD COLUMN genre VARCHAR(100);
```

### Заполнение таблиц

Основные команды DML:

- SELECT - выборка данных
- INSERT - добавление новых записей
- UPDATE - обновление существующих данных
- DELETE - удаление записей

**Добавление данных в существующую таблицу**

```sql
INSERT INTO books (title, author, published_date, available, genre) VALUES
('Преступление и наказание', 'Фёдор Достоевский', '1866-01-01', TRUE, 'Роман'),
('Идиот', 'Фёдор Достоевский', '1869-01-01', FALSE, 'Роман'),
('Война и мир', 'Лев Толстой', '1869-01-01', TRUE, 'Роман-эпопея'),
('Анна Каренина', 'Лев Толстой', '1877-01-01', FALSE, 'Роман'),
('Мастер и Маргарита', 'Михаил Булгаков', '1967-01-01', TRUE, 'Фантастика');
```

# Связывание таблиц

### Один ко многим

Для решения проблемы с дублированием данных в одной таблице, существуют связи между таблицами по принципу "один ко многим". Часть информации выносится в отдельную таблицу и связывается с остальными.

Вынесем авторов в отдельную таблицу authors и свяжем её с таблицей books. У каждого автора может быть несколько книг, а у каждой книги может быть только один автор - поэтому такая связь называется "один ко многим"

**Создание таблицы authors**

```sql
CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birth_date DATE,
	nationality VARCHAR(50) NOT NULL
);
```

**Пересоздание таблицы books с внешним ключом**

```sql
DROP TABLE books;
CREATE TABLE books (
	id serial primary key, -- можно id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
	title varchar(100) not null,
	published_date DATE,
	available BOOLEAN DEFAULT TRUE,
	genre varchar(100),
	author_id INTEGER REFERENCES authors(id) -- ссылка на столбец 'id' в таблице 'authors' (у книги - один автор)
);
```

- REFERENCES задаёт внешний ключ для столбца author_id в таблице books, который ссылается на столбец id таблице authors. Это связывает каждую книгу с автором, обеспечивая целостность данных и упрощая поиск и фильтрацию по авторам.

**Поиск авторов и всех книг с помощью JOIN**

```sql
SELECT books.title, authors.first_name, authors.last_name
FROM books
JOIN authors ON books(author_id) = authors(id);
```

### Многие ко многим

Посетители библиотеки могут брать книги и возвращать их. Один читатель может взять несколько книг, и одну книгу можно взять несколько раз. Это пример связи многие ко многим. В данном случае это полезно для фиксировании истории событий

Таблица посетителей

```sql
create table borrowers (
	id int generated always as identity primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	email varchar(100) not null,
	phone varchar(20) not null
)

```

Возникает вопрос: как отслеживать все книги, взятые посетителями?

Первая нормальная форма запрещает хранить список книг в таблице посетителей. Создать borrower_id в таблице книг мы не можем, так как одну книгу можно взять несколько раз.

Решение - новая таблица, хранящая информацию о взятых книгах:

```sql
create table borrowed_books (
	id integer generated always as identity primary key,
	borrow_date date not null,
	return_date date,
	book_id integer references books(id),
	borrower_id integer references borrowers(id)
);
```

Регистрация нового посетителя

```sql
INSERT INTO borrowers (first_name, last_name, email, phone)
VALUES
    ('Иван', 'Иванов', 'ivan.ivanov@example.com', '88005553536');
```

Если посетитель захочет взять книгу

```sql
INSERT INTO borrowed_books (borrow_date, return_date, book_id, borrower_id)
VALUES
    ('2022-01-01', '2022-01-15', 1, 1);
```

Узнать, какие книги взял пользователь с id 1:

```sql
select b.title as b, bor.borrow_date, bor.return date
from books b
join borrowed_books bor on bors.id = b.author_id
where b.author_id = 1;
```

# Почему в group by обязательно использовать поля из select

В sql действует правило: все неагрегированные столбцы в SELECT должны быть в GROUP BY. Если в запросах нет агрегатных функций вроде `COUNT`, `SUM` и т.д., то поле из select необходимо включать в group by, иначе СУБД не поймёт, как "свернуть" строки: для одного book_id может быть много записей о выдаче, и без явной группировки непонятно, какое значение `title` брать. Лучше группировать по `id` (books.id), поскольку:

- гарантируется уникальность (pk уникален)
- соответствует семантике
- стандарт SQL и строгие СУБД

```sql
select books.title, count(borrowed_books.book_id) as total_borrowed
from books
join borrowed_books on books.id = borrowed_books.book_id
group by books.id, books.title
order by total_borrowed DESC
limit 3;
```

## Схемы (Schemas)

Схемы в PostgreSQL - это логические контейнеры (папки) для объектов внутри одной базы данных: таблиц, представлений (view), функций и т.п.

Аналогия:

- База данных - диск `C:`
- Схема - папка внутри диска `C:\Projects\MyApp`
- Таблица - это файл внутри папки `users.csv`
