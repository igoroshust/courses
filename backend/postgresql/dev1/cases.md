# Посмотреть список столбцов таблицы

```SQL
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'pg_proc'
ORDER BY ordinal_position;
```


# Возврат количества строк в таблице authors (функция)

```SQL
create function cnt() returns bigint
language sql volatile
return (select count(*) from authors);
```

