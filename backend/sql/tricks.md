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
