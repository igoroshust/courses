



# Анализ данных о продажах

Необходимо сохранить данные о продажах в CSV, а затем - проанализировать их и сохранить результаты в JSON

```Python
import json
import csv


sales = [
    ['Date', 'Product', 'Category', 'Price', 'Quantity'],
    ['2023-01-05', 'HP Laptop', 'Electronics', '45000', '2'],
    ['2023-01-10', 'Apple Smartphone', 'Electronics', '85000', '3'],
    ['2023-01-15', 'Book "Python"', 'Books', '1200', '5'],
    ['2023-02-10', 'Microwave', 'Home Appliances', '7000', '1']
]


# Записываем в csv
with open('sales.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(sales)
  
  
# Читаем и анализируем данные
with open('sales.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Пропускаем заголовки
  
    # Подготовка переменных для анализа
    total_revenue = 0
    sales_by_category = {}
  
    # Анализ данных
    for row in reader:
        date, product, category, price, quantity = row
        revenue = float(price) * int(quantity)
      
        # Общая выручка
        total_revenue += revenue
      
        # Выручка по категориям
        if category in sales_by_category:
            sales_by_category[category] += revenue
        else:
            sales_by_category[category] = revenue
          
    # Вывод результатов анализа
    print(f'\nОбщая выручка: {total_revenue} rub.')
    print(f'\nВыручка по категориям:')
    for category, rev in sales_by_category.items():
        print(f'{category}: {rev} rub.')
      
      
# Сохраняем результаты анализа
results = {
    "total_revenue": total_revenue,
    "sales_by_category": sales_by_category
}

# Формируем JSON-файл с результатами
with open('sales_analysis.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=2)
    print('Serialized in JSON!')
  
  
# Читаем JSON-файл
with open('sales_analysis.json', 'r', encoding='utf-8') as file:
    save_results = json.load(file)
  
    print('\nContents of the results JSON file:')
    print(json.dumps(save_results, ensure_ascii=False, indent=2))
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

# Читаем csv

# Логика

# Сериализуем в JSON

# Читаем JSON
```















# Чтение и обработка конфигурационного файла

```Python
# Пример конфигурационного файла
config_text = """
# Параметры БД
database_host = localhost
database_port = 5432
database_name = myapp
database_user = admin
database_password = secret123

# Параметры веб-сервера
server_port = 8080
debug_mode = True
log_level = INFO
"""

with open('config.ini', 'w') as config_file:
    config_file.write(config_text)
  
# Чтение и обработка конфигурации
def read_config(filename):
    config = {}
  
    with open(filename, 'r') as file:
        for line in file:
            # Пропускаем пустые строки и комментарии
            line = line.strip()
            if not line or line.startswith('#'):
                continue
        
            # Разделяем ключ и значение
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
            
    return config

# Считываем конфигурацию
app_config = read_config('config.ini')

# Используем параметры
print("Конфигурация приложения:")


print(f"База данных: {app_config['database_name']} на {app_config["database_host"]}")

print(f"Пользователь БД: {app_config['database_user']}")

print(f"Порт веб-сервера: {app_config['database_port']}")

print(f"Режим отладки: {app_config['debug_mode']}")
```

# Таблица умножения

```python
# Таблица умножения

for i in range(1, 4):  # строки
    for j in range(1, 4):  # столбцы
        print(f'{i} * {j} = {i*j}', end='\t')
    print()  # переход на новую строку после каждой строки таблицы
```

# Разворот списка

```python
fruits = ["яблоко", "банан", "вишня", "груша", "апельсин"]

reversed_list = fruits[::-1]

print(fruits)
```

# Определить наибольшую оценку и лучшего студента

```python
students = ["Анна", "Иван", "Мария", "Петр", "Елена"]
grades = [95, 82, 90, 78, 88]

top_student, highest_score = max(zip(students, grades), key=lambda x: x[1])

print(f"{top student} with score {hightest_score}")
```

- zip берёт элементы из нескольких итерируемых объектов парами по индексам и возвращает итератор кортежей. Сшивает списки - первый с первым, второй со вторым. Если длины разные, zip останавливается на длине самого короткого. Необходимо, что дальше работать с парой студент-оценка как с одним элементом.
- key говорит max, по какому значению сравнивать элементы
- key=lambda x: x[1] - короткая анонимная функция, принимающая один аргумент x и возвращающая его второй элемент x[1]. x - каждый кортеж (имя, оценка), x[1] - оценка. Это значение говорит: сравний элементы по их второму полю (оценке)

  zip даёт последовательность

  max перебирает эти кортежи, для каждого вызывая `key(x)`: для ('Анна', 95) -> key вернёт 95

  затем max выбирает тот кортеж, у которого значение key наибольшее

  поскольку max возвращает кортеж вида `(имя, оценка)`, он сразу распаковывается в две переменные

```python
list(zip(students, grades))  # [("Анна", 95), (...), (...)]
```

# Вывести первый, последний и третий элемент ввода (при наличии)

```python
# Считайте список чисел из одной строки
numbers = list(map(int, input().split()))

# Выведите первый элемент списка
print(numbers[0])

# Выведите последний элемент списка
print(numbers[-1])

# Выведите третий элемент списка (если он существует, иначе выведите "No third element")
print(numbers[2] if len(numbers) > 2 else 'No third element')
```

# Распаковка списка

```python
numbers = [10, 20, 30, 40]

print(*numbers)  # 10, 20, 30, 40
```

# Проверка уникальности элементов

```Python
def are_all_unique(items):
    return len(set(items)) == len(items)

print(are_all_unique([1, 2, 3, 4, 5]))  # True
print(are_all_unique([1, 2, 3, 3, 3]))  # False
```

# Оценка производительности

```Python
import timeit

data = list(range(10000))
data_set = set(data)

list_time = timeit.timeit('9999 in data', globals=globals(), number=100_000)  
set_time = timeit.timeit('9999 in data_set', globals=globals(), number=100_000)

print(f'Список: {list_time:.6f} сек на 100k проверок')
print(f'Множество: {set_time:.6f} сек на 100k проверок')
print(f'Множество быстрее в {list_time/set_time:.1f} раз')
```

- globals() встроенная в Python функция, возвращающая словарь с глобальным пространством имён текущего модуля. Словрь, где ключи - имена глобальных переменных, функций, классов, а значения - сами объекты

`{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002292AAB7410>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\Applications\\courses\\backend\\python\\main.py', '__cached__': None}`

- В этом примере передаём globals timeit.timeit() для корректного выполнения строки `'9999 in data'`, так как изначально она выполняет его в пустом окружении. А так выполняет в том же окружении, где определены data и data_set.

# Подсчитать количество упоминаний слова в словаре

Решение учителя

```Python
text = "one two three one two"

words = text.split()
counts = {}

for word in words:
  if word in counts:
    counts[word] += 1
    # Через get()
    counts[word] = counts.get(word, 0) + 1
  else:
    counts[word] = 1

  

print(counts)  # {'one': 2, 'two': 2, 'three': 1}
```

Рекомендация (оптимизация, чистота)

```Python
from collections import Counter

text = "one two three one two"

counts = Counter(text.split())  # Counter({'one': 2, ...})
```

Платформа

```Python
def count_frequency(text):
    result = {}
    for i in text.split():
        result[i] = result.get(i, 0) + 1

    return result

text = 'the quick brown fox jumps over the lazy dog fox'

word_counts = count_frequency(text)

print(
    word_counts
)
```

Counter

```Python
from collections import Counter

def count_frequency(text: str) -> dict:
  return dict(Counter(text.split()))

text = input()
word_counts = count_frequency(text)
print(word_counts)
```

# Создать словарь с оценками для студентов

Моё решение

```Python
students = 'Igor Egor Oleg Natalia Sean Walter'
scores = '90 80 30 40 50 49'

def create_total_dict(item1, item2):
    return dict(zip(item1.split(), map(int, item2.split())))

print(create_total_dict(students, scores))
```

Через генератор словаря

```Python
students = 'Igor Egor Oleg Natalia Sean Walter'
scores = '90 80 30 40 50 49'

def create_total_dict(item1, item2):
    students = item1.split()
    scores = map(int, item2.split())
    return {name: score for name, score in zip(students, scores)}  # for name, score in [('Igor', 90), ('Egor', 80)]:

print(create_total_dict(students, scores))
```

Платформенное

```Python
names = input().split()
grades = list(map(int, input().split()))

students = dict(zip(names, grades))

print(students)
```

# Разница дат

В этой задаче вам предстоит создать программу для выполнения операций с датами. Пользователь вводит дату и количество дней, которое нужно прибавить или вычесть из этой даты. Ваша программа должна вычислить новую дату и вывести ее.

## Входные данные

* Первая строка содержит дату в формате ДД.ММ.ГГГГ (например, 15.03.2023)
* Вторая строка содержит целое число (положительное или отрицательное), которое указывает, сколько дней нужно добавить к дате (или вычесть из даты, если число отрицательное)

## Выходные данные

Одна строка, содержащая новую дату в том же формате ДД.ММ.ГГГГ

```Python
from datetime import datetime, timedelta

date_str = '31.12.2026'
days = 5

# Преобразуем строку в дату по формату ДД.ММ.ГГГГ
current_value = datetime.strptime(date_str, "%d.%m.%Y")

# Прибавляем/вычитаем дни
new_value = current_value + timedelta(days=days)

# Форматируем обратно в строку
result_date = new_value.strftime("%d.%m.%Y")
print(result_date)
```

# Заменить двойные слеши на одинарные

```Python
s = 's = "C:\\Users\\igoroshust\\AppData\\Roaming\\Python\\Python314\\site-packages"
clean = s.replace('\\\\', '\\')  # C:\Users\igoroshust\AppData\Roaming\Python\Python314\site-packages
```
