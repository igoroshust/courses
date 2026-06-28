  

# Библиотеки

Библиотека (модуль) – файл с кодом, содержащий функции, классы и переменные, которые можно использовать в своих программах. Это готовые наборы ранее написанного и отлаженного кода.

Импорт

```Python
# Прямой
import math

# Отдельные функции
from math import sqrt, floor 

# Переименование
import math as m
```

## Виды библиотек

1. Встроенные (включенные в стандартную библиотеку Python и доступные сразу после установки языка). `random, math, os, sys, json, collections, re, csv, unittest, datetime`
2. Сторонние библиотеки (созданы другими разработчиками, требуют дополнительной установки). `requests, pandas, numpy, matplotlib, beautifulsoup, fastapi, django, flask, selenium, tesnorflow, pytorch`
3. Собственные (созданые вами для организации своего кода)

#### Вывод атрибутов элемента

```Python
import random
attributes = dir(random)

print(attributes[:10])
```

Комплектующие дистрибутива Python:

- Интерпретатор
- IDLE (встроенная среда разработки)
- pip
- Стандартная библиотека
- Документация и утилиты

Дистрибутив - сборка, позволяющая установить ЯП на ПК `python-3.12.4-amd64.exe`.

## Встроенные библиотеки

Встроенная библиотека (стандартная библиотека) – это набор модулей, включённых в дистрибутив Python и готовых к использованию без дополнительной установки.

1. math

```Python
import math

math.pi
math.e
math.sin(math.pi / 4):.4f
math.cos(math.pi / 4):.4f
math.factorial(5)
math.gcd(12, 18)  # наибольший общий делитель 12 и 18: 6
```

2. random - генерация случайных чисел и выбор случайных элементов

```Python
import random

random.randint(1, 10)
random.random():.4f  # случайное число с плавающей точкой от 0 до 1: 0.3528

# Выбор случайного элемента последовательности
fruits = ["яблоко", ...]
random.choice(fruits)  # яблоко

# Перемешивание последовательности
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  # [3, 1, 5, 2, 4]
```

3. datetime - предоставляет классы для работы с датой и временем

```Python
import datetime

# Текущая дата и время
now = datetime.datetime.now()  # 2026-06-28 14:39:25.225090

# Задание конкретной даты
specific_date = datetime.date(2026, 12, 31)  # 2026-12-31

# Разница между датами
today = datetime.date.today()
new_year = datetime.date(today.year + 1, 1, 1)
days_until_new_year = (new_year - today).days

print('До нового года', days_until_new_year)

# Форматирование даты
formatted_string = now.strftime("%d.%m.%Y %H:%M")  # 15.07.2023 15:42
```

4. os - набор функций для взаимодействия с операционной системой

```Python
import os

# Получение текущей директории
current_dir = os.getcwd()

# Список файлов и папок в директории
files = os.listdir('.') 

# Информация о системе
sys_info = os.name

# Проверка существования файла/директории
file_exists = os.path.exists('cases.md')
```

5. json - предоставляет функции для работы с данными в JSON-формате

```Python
import json

# Словарь Python
person = {
    "name": "Иван",
    "age": 30,
    "city": "Москва",
    "languages": ["Python", "JavaScript", "SQL"]
}

# Преобразование Python-объекта в JSON
python_to_json = json.dumps(person, ensure_ascii=False, indent=4)

# Преобразование JSON в Python-объект
json_object = '{ "name": "Igor", "age": 29, "is_admin": True }'
json_to_python = json.loads(json_object)
```

`json.dumps` превращает Python-объект в JSON-строку. Это необходимо, чтобы отдать данные по API, сохранить в файл или передать в Django-шаблон.

- python_to_json рекурсивно преобразуется в json
- ensure_ascii=False отображает кириллицу
- indent=4 даёт отступы

`json.loads(string)` (load string) берёт json и превращает в Python-объект. Парсит (разбирает) строку по правилам JSON и строит из неё структуры данных Python.

`json.load(file_object)` - читает JSON из файла. На вход подаётся открытый файл (результат `open(...)`).

6. Collections - удобные структуры данных поверх базовых. В модуле также есть defaultdict, namedtuple, deque и другие.

```Python
from colleciton import Counter

text = "Programming on Python"
character_count = Counter(text.lower())  # # Counter({'o': 3, 'n': 3, 'p': 2, 'r': 2, 'g': 2, 'm': 2, ' ': 2, 'a': 1, 'i': 1, 'y': 1, 't': 1, 'h': 1})

print("Three most frequently chars")
for char, count in character_count.most_common(3):
  print(f"'{char}': {count}")

# 'o': 3
# 'n': 3
# 'p': 2
```
