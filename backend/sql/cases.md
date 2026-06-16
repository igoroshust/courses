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

# Переименовать таблицу

```sql
alter table borrower_books RENAME TO borrowed_books;
```

**Переименовать колонку**

```sql
alter table borrower_books rename column borrow_date to borrowed_date;
```
