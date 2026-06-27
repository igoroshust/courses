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
