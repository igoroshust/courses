import psycopg2  # Подключаем драйвер для работы с pgSQL. С его помощью Python общается с базой - отправляет запросы, получает результаты.
from psycopg2.extras import DictCursor  # импортирует специальную обёртку для курсора. Обычный курсор возвращает строки как кортежи (по индексам: row[0]), а DictCursor - как словари (по именам колонок: row['title'])

# Устанавливаем соединение с базой
conn = psycopg2.connect(
    user="postgres", password="postgres", host="127.0.0.1", port="5432", dbname="posts"
)

# Проверка подключения в БД
if conn:
    print("connected!")
    
# Создаём курсор - инструмент для отправки SQL-запросов и получения результатов
cursor = conn.cursor(cursor_factory=DictCursor)  # cursor_factory=DictCursor говорит: "Возвращай строки как словари". Дальше можно писать new['title'] вместо news[0]

# Ввод от пользователя
title = input('Введите заголовок: ')
text = input('Введите текст: ')

# Формируем запрос на вставку данных в таблицу posts
sql = f'INSERT INTO posts (title, text) VALUES (%s, %s)'  # защита от SQL-инъекций
cursor.execute(sql, (title, text))  # отправка запроса в БД
conn.commit()  # Фиксируем транзакцию (без этого данные не сохраняться). В PostgreSQL все изменения "висят" до commit().

cursor.execute("SELECT * FROM posts")  # Выборка всех строк из news
result = cursor.fetchall()  # fetchall() забирает все строки результата в список
# print(type(result))
# print(type(result[0]))

# Итерация по результатам ответа
for news in result:
    print(news['title'])

# Закрываются курсор и соединение (освобождаются ресурсы на стороне БД)
cursor.close()
conn.close()
    
    
    
"""Пример безопасного файла"""
import psycopg2
from psycopg2.extras import DictCursor

conn = None

try:
    conn = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432",
        dbname="posts"
    )
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        title = input('Введите заголовок: ')
        text = input('Введите текст: ')

        sql = 'INSERT INTO posts (title, text) VALUES (%s, %s)'
        cursor.execute(sql, (title, text))
        conn.commit()

        cursor.execute('SELECT * FROM posts')
        for row in cursor.fetchall():
            print(row['title'])

except Exception as e:
    print("Ошибка работы с БД:", e)
finally:
    if 'conn' is not None:  # можно вместо None использовать locals() - встроенную функцию Python, возвращающая словарь с локальными переменными текущей области видимости.
        conn.close()
