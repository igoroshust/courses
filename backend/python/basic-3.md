# Лямбда-функции

Лямбда-функции - это безымянная функция из одного выражения: она принимает аргументы и возвращает результат этого выражения. Это крошечная функция прямо там, где она нужна, без имени и без `def`. Они компактнее обычных функций, но для сложных операций читаются хуже.

`lambda аргументы: выражение`

3 характеристики lambda:

- Безымянная - её не объявляют через `def` с именем, а пишут по месту
- Из одного выражения - тело это одна строка, результат которой возвращается
- Это функция - принимает аргументы и возвращает значение

#### Пример

```Python
square_lambda = lambda x: x * x
power_lambda = lambda base, exponent: base ** exponent

print(square_lambda(5))  # 25
print(power_lambda(2, 3))  # 8
```

Лямбда подходят для простых функций (одно выражение), функция используется только один раз (или несколько раз в одном месте), функция передаётся как аргумент другой функции. Наиболее распространённые случаи использования - с функциями высшего порядка вроде `map()`, `filter()`, `sorted()` и д.р.

## L с функциями высшего порядка

**map()** - применение функции к каждому элементу итерируемого объекта

```Python
numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x * 2, numbers))

print(doubled_numbers)

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
```

**filter()** - создаёт итератор из элементов, для которых функция возвращает True

```Python
```

**sorted()** - возвращает отсортированный список, с помощью key можно указать функцию для извлечения значения для сравнения. Упорядочивание последовательностей.

```Python
# Сортировка чисел по абсолютному значению
numbers = [5, -3, 2, -8, 1, 0, -2]

sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)

# Сортировка словарей по значению определенного ключа
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95}
]

# Сортировка по оценке (по убыванию)
sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)
for student in sorted_by_grade:
    print(f"{student['name']}: {student['grade']}")
```

**functools.reduce() -** последовательное применение функции к элементам с накоплением результата. Агрегация, накопление

```Python
from functools import reduce

# Сумма всех чисел в списке
numbers = [1, 2, 3, 4, 5]
total_lambda = reduce(lambda x, y: x + y, numbers)
print(total_lambda)

# Объединение строк
words = ["Hello", "world", "of", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)
```

### Лямбда как аргументы других функций

```Python
# Лямбда-операции
def apply_operation(x, y, operation):
    return operation(x, y)

print(
    f'''Addition: {apply_operation(5, 3, lambda x, y: x + y)}
Subtraction: {apply_operation(10, 5, lambda x, y: x - y)}
Division: {apply_operation(20, 5, lambda x, y: x / y)}
Multiplication: {apply_operation(10, 20, lambda x, y: x * y)}'''
)

# Форматирование данных
def data_formatter(data, formatter):
    return [formatter(item) for item in data]

names = ['alice', 'bob', 'phil']

print(
    data_formatter(names, lambda x: x.title())
)
```

### Ограничения L

1. Нет оператора присваивания `=`
2. Отсутствие docstring
3. Однострочное выражение
4. Ограниченная читаемость

```Python
# Пример сложной логики, где лучше не использовать lambda
complex_lambda = lambda x: (
    x ** 2 if x > 0
    else x + 1 if x < 0 
    else 42
)

# Пример с обычной функцией
def process_number(x):
    """Обрабатывает число по правилам:
    - Положительное -> квадрат
    - Отрицательное -> x + 1
    - Ноль -> 42 
    """
  
    if x > 0:
        return x ** 2
    elif x < 0:
        return x + 1
    else:
        return 42
  
print(process_number(0))
```

# Исключения

Исключение - ошибка, возникшая во время выполнения программы. По умолчанию оно прерывает работу, но его можно перехватить и обработать.

`try-except` - основной механизм обработки исключений в Python, позволяющий:

- Изолировать потенциально опасный код
- Перехватывать ошибки
- Выполнять альтернативные действия
- Продолжать выполнение программы

```Python
try:
    # Рискованный код
except ТипИсключения1:
    # Обработка исключения типа 1
except ТипИсключения2:
    # Обработка исключения типа 2
else:
    # Выполняется, если в блоке try не возникло исключений
finally:
    # Выполняется всегда, независимо от наличия исключений
```

Обработка нескольких видов ошибок

```Python
try:
    file_name = 'result.json'
    file = open(file_name, 'r')
    line = file.readline()
    number = int(line.strip())
    result = 100 / 0
    print(result)
  
except FileNotFoundError:
    print("not found")
  
except ValueError:
    print("value error")
  
except ZeroDivisionError:
    print("zero div")
  
except Exception as e:
    print("Unknown error")
```

P проверяет блоки except в порядке их объявления и выполняет соответствующий код из первого подходящего блока

**Обработка нескольких исключений одним блоком**

```Python
try:
    value = int("abc")
    result = 10 / 0
except (ValueError, ZeroDivisionError):
    print("Произошла ошибка в вычислениях")
```

else - выполнение кода при отсутствии исключений

```Python
try:
    number = int("42")
except (ValueError, ZeroDivisionError):
    print("An error occurred in the calculations")
else:
    print(f'Успешно! Число: {number}')
    print(f'Квадрат числа: {number ** 2}')
```

finally выполняется всегда, полезно для:

- освобождения ресурсов (закрытие файлов, соединений с БД)
- очистки временных данных
- логирования завершения ошибки

```Python
try:
  f = open("example.txt", "w")
  f.write("Привет, мир!")
  # Потенциальное исключение
except IOError:
  print('Произошла ошибка ввода-вывода')
finally:
  print('Закрытие файла')
  f.close()  # Файл будет закрыт в любом случае
```

Информация о типе исключения

`as` нужен для получения объекта исключения

```Python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Type: {type(e).__name__}")
    print(f"Message: {e}")
```

`raise` - вызов исключения

```Python
def check_age(age):
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    if age < 18:
        print("Вы несовершеннолетний")
    else:
        print("Вы совершеннолетний")

try:
    check_age(-5)
except ValueError as e:
    print(f"Ошибка: {e}")
```

Создание собственных исключений

```Python
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email должен содержать символ @")
    print(f"Email {email} корректен")

  
try:
    validate_email("user.example.com")
except InvalidEmailError as e:
    print(f'Valid error: {e}')
```

#### Практические рекомендации

1. Указывать конкретный тип исключения

```Python
# Плохо
try:
    number = int("abc")
except:  # Перехватывает все исключения
    print("Ошибка")
  
  
# Хорошо
try:
    number = int("abc")
except ValueError:
    print("Неверный формат числа")
```

2. Минимизировать код в блоке try

```Python
# Хорошо
try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print('File not found')
    file = None
  
  
if file:
    try:
        content = file.read()
    except:
        print("Ошибка при чтении файла")
    finally:
        file.close()
```

3. Правильное использование else и finally

```Python
def get_value_from_list(my_list, index):
    try:
        value = my_list[index]
    except IndexError:
        print(f'Index {index} out of range')
        return None
    else:
        print('Success')
        return value
    finally:
        print('Operation completed')
    
correct_result = get_value_from_list([1, 2, 3], 1)
uncorrect_result = get_value_from_list([1, 2, 3], 10)
```

# Декораторы

Декоратор - функция, принимающая другую функцию и возвращающая её "обёрнутую" версию (с добавленным поведением)

```Python
def my_decorator(func):
  def wrapper():
    print('Before the call')
    func()
    print('After the call')
  return wrapper

@my_decorator
def say_hello():
    print('Hi world')

say_hello()
```

Запись `@my_decorator` над `say_hello` это сахар над эквивалентом: `say_hello = my_decorator(say_hello)`. Происходит переопределение `say_hello` на новую функцию (которую вернул декоратор). Никакой магии, обычное переприсваивание.

### Декоратор с аргументами функции

Если оборачиваемая функция принимает аргументы, обёртка должна их пробрасывать. Универсальный приём: `*args, **kwargs`.

```Python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before the call')
        result = func(*args, **kwargs)
        print('After the call')
    
        return result
    return wrapper


@my_decorator
def add(a, b):
    return a + b

print(add(5, 3))
```

`*args, **kwargs` означает "приму любые позиционные и именованные аргументы", `func(*args, **kwargs)` пробрасывает их дальше. Этим приёмом декоратор становится универсальным – работает с любой функцией.

- args собирает все позиционные аргументы в кортеж
- kwargs собирает все именованные аргументы в словарь

```Python
def f(*args, **kwargs):
    print("args:", args)  # (1, 2, 3)
    print("kwargs:", kwargs)  # {'x': 10, 'y': 20}
  
f(1, 2, 3, x=10, y=20)
```

### functools.wraps: сохранение имени и docstring

У наивного декоратора есть незаметный побочный эффект: обёрнутая функция "теряет" своё имя и документацию, потому что снаружи виден уже wrapper, а не оригинал.

```Python
def timing(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@timing
def calculate_sum(n):
    """Считает сумму чисел от 0 до n."""
    return sum(range(n))

print(calculate_sum.__name__)  # wrapper
print(calculate_sum.__doc__)  # None
```

В реальном коде это ломает отладку, логирование и работу IDE. Лечится одной строкой – декоратором `@functools.wraps(func)` на `wrapper`.

```Python
from functools import wraps

def timing(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  return wrapper

@timing
def calculate_sum(n):
  """Calculate the sum of numbers from 0 to n"""
  return sum(range(n))

print(calculate_sum.__name__)  # calculate_sum
print(calculate_sum.__doc__)  # Calculate ...
```

Правило: при написании собственного декоратора всегда оборачивайте внутреннюю функцию в `@wraps(func)`. Это сохраняет интроспекцию.

Интроспекция - способность программы осматривать собственные объекты во время выполнения: узнавать их имя, документацию, модуль, место возникновения и т.п.

### Декоратор с параметрами

Для передачи настроек декоратору требуется создание дополнительного уровня, где внешняя функция принимает параметр и возвращает "настоящий" декоратор (например, повтор вызова N-раз)

```Python
from functools import wraps

def repeat(n=1):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwrags):
            result = None
            for _ in range(n):
                result = func(*args, **kwrags)
            return result
        return wrapper
    return my_decorator

@repeat(n=5)
def say_hello(name, surname):
    print('Hi', name, surname)
  
say_hello('igor', 'oshust')
```

Три уровня вложенности:

- **repean(n)** принимает параметр декоратора и возвращает обычный декоратор
- **decorator(func)** принимает функцию и возвращает обёртку
- **wrapper(*args, **kwargs)** обрабатывает реальный вызов

### Цепочка декораторов

Декораторы можно применять несколько. Они применяются снизу вверх: ближайший к функции идёт первым:

```Python
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def format_text(text):
    return text

print(format_text("Hi world"))
```

italic применяется к format_text первым, получается italic-функция. Потом bold оборачивает её снаружи, получается `bold(italic(format_text))`, поэтому сначала закрывается `</i>`, потом `</b>`

### Дополнительно

При инкапсуляции используются декораторы `@property` и `@balance.setter` - это декораторы стандартной библиотеки. `@property` берёт функцию-геттер и превращает её в вычисляемый атрибут.

Декораторы в реальности используются в:

1. Веб-фреймворки (Flask, FastAPI, Django). Привязка URL-функции к обработчику:

```Python
@app.route('/home')
def home():
  return "Main page"
```

2. Кеширование. Сохранение результатов, чтобы не пересчитывать одно и то же.

```Python
from functools import wraps

# cache = {}


def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(30))
```

Без memoize fib(30) пересчитывал бы одно и то же миллион раз и подвисал. С кэшем работает мгновенно. В стандартной библиотеке  есть декоратор `from functools import lru_cache`

3. Тесты. В pytest `@pytest.fixture` и `@pytest.mark.parametrize` - это декораторы, которые превращают обычную функцию в фикстуру или параметризованный тест.




# Работа с датой и временем


Основа работы с данными – три операции: парсинг строки, арифметика, форматирование. Все они лежат в стандартном модуле `datetime`. Пример задачи: посчитать количество ошибок в лог-файле за сутки (в корректном часовом поясе и нужном формате).

**Три основных класса** в модуле datetime:

- datetime: конкретный момент времени с точностью до микросекунд. Используется в 90% случаев.
- date: только дата, без времени. День рождения, дедлайн, дата заказа.
- time: только время суток, без даты.

```Python
from datetime import datetime, date, time

# Момент времени
now = datetime.now()  # 2026-07-01 19:48:41.925402

# Только дата
birthday = date(1990, 5, 15)  # 1990-05-15

# Только время
meeting = time(14, 30)  # 14:30:00
```

У всех трёх классов есть отдельный атрибуты компонентов: .year, .month, .day, .hour, .minute, .second, .microsecond.

```Python
from datetime import datetime, date, time

now = datetime.now()
print(
    now.year,  # 2026
    now.month,  # 7
    now.day,  # 1
    now.hour,  # 19
    now.minute,  # 54
    now.second,  # 49
    now.microsecond,  # 254644

   	now.weekday()  # 2 (среда)
)
```


### Арифметика дат: timedelta

Прибавлять и вычитать даты можно напрямую: результат это timedelta (промежуток времени), либо новый datetime:

```Python
from datetime import datetime, timedelta, date, time

now = datetime.now()

# Прибавить интервал
week_later = now + timedelta(days=7)


# Разница между моментами это timedelta
deadline = datetime(2026, 8, 1)
delta = deadline - now
print(type(deadline))  # <class 'datetime.datetime'>
print(type(delta))  # <class 'datetime.timedelta'>

print(delta)  # 30 days, 3:57:19.017025

print(
    delta.days, # 30
    delta.total_seconds()  # 2606144.361989
)
```


timedelta принимает days, hours, minutes, seconds, weeks, но не months и years (потому что они переменной длины: в феврале 28 или 29 дней, в году 365 или 366). Для прибавления месяцев есть библиотека `dateutil` (внешняя)

### strftime, strptime: между объектом и строкой

В реальном коде даты постоянно проходят через строки – API, логи, БД. Запомнить нужный метод правилом:

- strftime - format: объект -> строка
- strptime - parse: строка -> объект

```Python
from datetime import datetime, timedelta, date, time

now = datetime(2026, 5, 20, 14, 30)  # 2026-05-20 14:30:00

parsed = datetime.strptime("20.05.2026 14:30", "%d.%m.%Y %H:%M")

print(
    now.strftime("%d.%m.%Y %H:%M"),  # 20.05.2026 14:30
    now.strftime("%A, %d %B %Y"),  # Wednesday, 20 May 2026s
    type(now.strftime("%A, %d %B %Y")),  # <class 'str'>
  
    parsed,  # 2026-05-20 14:30:00
    type(parsed)  # <class 'datetime.datetime'>
)
```


### ISO 8601: стандарт обмена датами

Если дату можно передавать между системами (API, JSON, БД), используется ISO 8601: `2026-05-20Т14:30:00`. У datetime есть готовые методы для этого формата, и они быстрее и надёжнее, чем strftime / strptime.

```Python
from datetime import datetime

now = datetime(2025, 5, 12, 14, 30)

# В ISO
iso_string = now.isoformat()  # 2025-05-12T14:30:00  str

# Обратно
parsed = datetime.fromisoformat("2026-05-20T14:30:00")  # 2026-05-20 14:30:00  datetime
```

Правило: внутри программы держите даты как datetime-объекты, при выводе наружу (в JSON, в БД) - `.isoformat()`, при чтении снаружи - `fromisoformat()`. Свой формат с `strftime` нужен только когда мы показываем дату пользователю.


### Часовые пояса: naive vs aware

`datetime.now()` без аргумента возвращает "наивный" (naive) datetime - у него нет информации о часовом поясе. Это распространённая грабля: программа работает "дома", а на сервере в другой стране внезапно показывает время на 7 часов раньше.

Правильно работать с aware datetime, у которого часовой пояс есть (модуль `zoneinfo` умеет в реальные часовые пояса с учётом перехода на летнее время). Ранее использовали pytz до P 3.9.

```Python
from datetime import datetime
from zoneinfo import ZoneInfo

# Aware datetime в UTC и Москве
utc_now = datetime(2026, 5, 20, 14, 30, tzinfo=ZoneInfo("UTC"))
moscow_now = utc_now.astimezone(ZoneInfo("Europe/Moscow"))

print(utc_now)

print(moscow_now)
```

Хранить datetime в БД всегда в UTC, конвертировать в локальную зону пользователя только при выводе. 


### Модуль time

Низкоуровневый модуль time предлагает два наиболее частых метода

```Python
import time

print(
    # Текущий момент как UNIX timestamp (секунд с 1 января 1970)
    time.time(),  # 1782907585.6376035
)


print("Starting...")
time.sleep(0.1)
print("10 seconds have passed")
```

time.time() возвращает unix timestamp - это формат, в котором часто хранят время в БД и логах: одно число, не зависит от часового пояса. Перевести в datetime можно через `datetime.fromtimestamp(ts, tz=ZoneInfo("UTC"))`.

[Главное правило: ]()внутри программы держите даты как объекты, превращайте в строки только на границе с внешним миром.


# Аннотации

Аннотации типов - это специальный синтаксис, позволяющий явно указывать ожидаемые типы данных для переменных, аргументов функций и возвращаемых значений.  Помогает разработчика и IDE точно понимать, какие типы данных ожидаются в разных частях программы, что значительно ускоряет написание кода и отладку, делает код более предсказуемым и читаемым.

Аннтации - только подсказки, P не останавливает выполнение программы, однако они незаменимы для:

- Улучшения автодополнения кода в IDE (PyCharm, VS Code)
- Статического анализа кода (линтером mypy)
- Самодокументируемости кода (код проще читать и понимать)

#### Аннотации переменных

```Python
name: str = "Igor"
age: int = 29
height: float = 1.77
is_developer: bool = False
```


#### Аннтоации функций

```Python
def greet(name: str, age: int) -> str:
  return f"Привет, {name}! Тебе {age} лет."

message = greet("Иван", 25)
print(message)
```

Если функция ничего не возвращает, пишем `-> None`.


#### Аннотация коллекций

```Python
numbers: list[int] = [1, 2, 3, 4, 5]

user_ages: dict[str, int] = {
  "Ivan": 25,
  "Ann": 22
}

user_info: tuple[str, int, float] = ("Алексей", 30, 75.5)

unique_names: set[str] = {"Иван", "Анна", "Пётр"}
```


## Модуль typing


Для сложных сценариев аннтотаций есть встроенный модуль typing:

- Optinal - переменная может содержать значение определённого типа или None

```Python
from typing import Optional

def get_user_email(user_id: int) -> Optional[str]:
  if user_id == 1:
    return "xx@xx.xx"
  return None
```

- Union - переменная может принимать один или несколько типов

```Python
from typing import Union

def process_price(price: Union[int, float]) -> float:
  return float(price) * 1.2
```

- Callable (функции как аргументы) - можно типизировать функцию, переданную аргументом в другую функцию. Callable принимает два аргумента: список типов входных параметров и тип возвращаемого значения.

```Python
from typing import callable

def apply_twice(value: int, func: Callable[[int], int]) -> int:
  return func(func(value))

def double(x: int) -> int:
  return x * 2

  result = apply_twice(3, double)
```


### Создание собственных типов

```Python
Coordinates = tuple[float, float]
UserDict = dict[str, str | int]

def get_location() -> Coordinates:
  return (55.7558, 37.6173)

def process_user(user: UserDict) -> None:
  pass
```


### Целесообразность аннтотации

- Меньше багов. Редактор подсвечивает ошибку до выполнения кода.
- Идеальное автодополнение. IDE точно значет методу объекта, поскольку указан тип.
- Легче читать код. Сразу видно, что функция принимать числовой ID и возвращает словарь, и не нужно вчитываться в тело функции.
