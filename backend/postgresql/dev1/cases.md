# Посмотреть список столбцов таблицы

```SQL
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'pg_proc'
ORDER BY ordinal_position;
```
