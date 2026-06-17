# Просмотр всех таблиц в БД

SQL

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
AND table_type = 'BASE TABLE';
```

Таблицы из всех схем (без системных)

```sql
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema NOT IN ('pg_catalog', 'information_schema');
```

PSQL

- Основные таблицы

```sql
\dt
```

- Все таблицы

```sql
\dt *.*
```


# Переименовать таблицу

```sql
alter table borrower_books RENAME TO borrowed_books;
```

**Переименовать колонку**

```sql
alter table borrower_books rename column borrow_date to borrowed_date;
```

# Удаление базы данных

1. Отключиться от удаляемой БД (переключитьяс на другую)

   ```sql
   \c postgres
   ```
2. Проверить наличие прав на удаление БД
3. Принудительное завершение сессий (нужны права суперпользователя)

   ```sql
   SELECT pg_terminate_backend(pid) -- завершение сессии
   FROM pg_stat_activity -- все активные сеансы на сервере
   WHERE datname = 'repeat' -- только сессии к базе 'repeat
   AND pid <> pg_backend_pid(); -- кроме моей собственной сессии (критично!)
   ```
4. Выполинть удаление БД

   ```sql
   DROP DATABASE repeat;
   ```

Комментарии

- `pg_terminate_backend(pid)` - функция принудительного завершения сеанса (сессии) пользователя на сервере PostgreSQL
- `pid` - идентификатор процесса (Process ID). У каждого подключения к базе есть свой `pid` - это число, по которому сервер понимает, какую сессию необходимо отменить или завершить.
- `pg_stat_activity` - это системное представление (view), в котором PostgreSQL показывает все активные сеансы на сервере. Это "живой список подключений", отражающий, кто подключён, к какой базе, какой запрос сейчас выполняется, состояние сессии и т.д. Из него берётся `pid `для `pg_terminate_backend`.
- `datname` - это имя базы данных, к которой подключена сессия
- `<>` - не равно
- `pg_backend_pid()` - функция, возвращающая PID текущего сеанса (из которого выполняем запрос). Она нужна, чтобы в фильтрах исключить себя.

# Просмотр подключений к базам (живой список подключений)

```sql
SELECT pid, usename, datname, state, query
FROM pg_stat_activity;
ORDER BY query_start;
```
