import psycopg2
from psycopg2.extras import DictCursor

conn = None
try:
    # Устанавливаем соединение с базой
    conn = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432",
        dbname="posts"
    )
    print("connected!")

    # Создаём курсор с возвратом строк как словарей
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        # Получаем данные от пользователя
        title = input('Введите заголовок: ')
        text = input('Введите текст: ')

        # Вставляем данные безопасно (параметризация защищает от SQL‑инъекций)
        sql_insert = 'INSERT INTO posts (title, text) VALUES (%s, %s)'
        cursor.execute(sql_insert, (title, text))
        conn.commit()
        print("Запись успешно добавлена.")

        # Выбираем данные из той же таблицы (исправлено: было 'news', стало 'posts')
        cursor.execute("SELECT * FROM posts")
        result = cursor.fetchall()

        print(f"Тип результата: {type(result)}")
        if result:
            print(f"Тип первой строки: {type(result[0])}")

            for news in result:
                # Так как используется DictCursor, обращаемся по имени колонки
                print(news['title'])
        else:
            print("В таблице пока нет записей.")

except psycopg2.OperationalError as e:
    print(f"Ошибка подключения к базе данных: {e}")
except psycopg2.ProgrammingError as e:
    print(f"Ошибка в SQL или структуре БД (например, нет таблицы): {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
finally:
    # Гарантированно закрываем соединение, если оно было создано
    if conn is not None:
        conn.close()
        print("Соединение с БД закрыто.")
