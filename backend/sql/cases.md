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
