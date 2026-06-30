# ООП

Когда программа моделирует что-то из реального мира – банковский счёт, пользователя, машину – у этой сущности обычно есть данные (баланс, имя, скорость) и действия (внести деньги, представиться, ускориться). ООП позволяет упаковать данные и действия в одну сущность – объект, описанный шаблоном – классом.

```Python
class Car:
    def __init__(self, make, model):
        self.make = make  # марка
        self.model = model  # модель
        self.is_running = False  # заведён двигатель или нет
      
    def start_engine(self):
        """Запуск двигателя"""
        if not self.is_running:
            self.is_running = True
            return f"{self.make} {self.model}: Двигатель запущен!"
        return f"{self.make} {self.model}: Двигатель остановлен"
  
    def stop_engine(self):
        """Остановка двигателя"""
        if self.is_running:
            self.is_running = False
            return f"{self.make} {self.model}: Двигатель остановлен"
        return f"{self.make} {self.model}: Двигатель уже был остановлен"
  
  
my_car = Car("Toyota", "Corolla")
print(my_car.start_engine())
print(my_car.stop_engine())
```

- Car - класс (blueprint)
- my_car - экземпляр (объект) класса
- make, model, is_running - атрибуты (данные объекта)
- start_engine(), stop_engine() - методы (действия объекта)
- `__init__` - специальный метод-конструктор, вызывается автоматически при создании объекта через `Car(...)`
- self - ссылка на сам объект; через неё методы видят свои атрибуты

### Класс

Класс - шаблон, описывающий, какие методы будут у его экземпляров. Экземпляры класса содержат конкретные значения предписанных полей. Из одного класса могут исходить множество экземпляров. 

![1782774642151](image/oop/1782774642151.png)


## Принципы ООП

1. **Инкапсуляция** (объединение данных и методов)- упаковка данных и методов, которые с этими данными работают, в один объект. Внешний код не опускается в детали реализации, а работает через интерфейс класса.
2. **Наследование** (создание новых классов на основе существующих)- создзание нового класса на основе существующего с переиспользованием его атрибутов и методов.
3. **Полиморфизм** (использование единого интерфейса для разных типов) - возможность работать с объектами разных классов через единый интерфейс (одинакого вызывать `.area()` у круга, квадрата, треугольника)
4. **Абстракция**(выделение существенных характеристик**)** - выделение существенных характеристик объекта, скрытие неважных деталей.


#### Практический пример (банковский счёт)

```Python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
      
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Add {amount} rub. New balance is {self.balance} rub."
        return "Deposit sum could be positive"
  
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"withdraw {amount} rub. New balance is {self.balance} rub."
            return "insufficient funds"
        return "Withdraw sum could be positive"
  
    def get_balance(self):
        return f"Current balance of {self.owner} is {self.balance} rub."
  
account = BankAccount("Иван Петров", 1000)

print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))
```

Логика валидации (положительная сумма, недостаточно средств) прописана внутри методов, рядом с данными, к которым относится. Это и есть инкапсуляция.


## Self

Запись `person.greet()` Python превращает в `Person.greet(person)`. То есть объект слева от точки (`person`) автоматически становится первым аргументом метода - тем самым `self`. Через self метод видит собственные данные.

Одинаковый вызов

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    def greet(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет."
  
person = Person("Ann", 25)

print(person.greet())
print(Person.greet(person))
```


self это не keyword и не магия. Это просто имя первого параметра метода по соглашению. Через self можно вызывать другие методы того же объекта:

```Python
class Person:
	def __init__(self, name, age):
      self.name = name 
	  self.age = __package__

	def is_adult(self):
      return self.age >= 18

    def describe(self):
      status = 'adult' if self.is_adult() else 'infant'
	  return f'{self.name}: {status}'

person = Person("Ann", 25)
print(person.describe())
```


Объекты в Python изменяемы. После создания объекта его состояние можно менять: вызывать методы, модифицирующие атрибуты, или присваивать атрибутам новые значения напрямую. 

```Python
class Student:
  def __init__(self, name):
    self.name = name
    self.grades = []

  def add_grade(self, grade):
    self.grades.append(grade)
    return f"Добавлена оценка: {grade}"

  def average_grade(self):
    if not self.grades:
      return "the grades is empty"
    return sum(self.grades) / len(self.grades)

student = Student("Marry")
print(student.add_grade(5))
```

Метод `add_grade` модифицирует `self.grades` - список, хранящийся в объекте. Изменения происходят на месте: следующий вызов `student.average_grade()` видит обновлённое состояние.


### Динамические атрибуты

Можно добавлять любой атрибут в любой момент, даже если он не объявлен в `__init__`. Не рекомендуется, поскольку:

- Состояние объекта становится непредсказуемым. Гляда на класс, нельзя понять, какие атрибуты у него есть в действительности.
- IDE и линтеры не помогут с автодополнением: они знают только то, что объявлено в `__init__`.
- При опечатке создаётся новый атрибут вместо понятной ошибки. При создании `student.aeg = 19` P молча создаст новое поле `aeg`, и баг сложно будет найти.

Правило: все атрибуты объекта объявлять в `__init__`, даже со значением `None`. Так класс описывает поля объекта и опечатки превращаются в AttributeError.

```Python
class Student:
  def __init__(self, name):
    self.name = name

student = Student("Marry")
student.age = 19
student.favorite_color = "blue"

print(student.age)
print(student.favorite_color)
```


### Атрибуты и методы

Атрибуты бывают 2 видов: 

- **Экземпляра** - уникальные для каждого объекта. Это переменные, которые хранят данные конкретного объекта. Обычно создаются в `__init__` через `self.name`. Используются для данных, которые различаются между объектами (имя, возраст, id).
- **Класса** - общие для всех экземпляров. Это переменные, объявленные прямо в теле класса (вне методов). Они общие для всех экземпляров. Атрибуты класса предназначены для констант и значений по умолчанию; общих данных для всех экземпляров (имя школы студентов); счётчиков уровня класса (сколько объектов уже создано).

Разница атрибутов

```Python
class Student:
  # Атрибут класса: общий для всех экземпляров
  school = "Школа №1"

  def __init__(self, name, age):
    # Атрибуты экземпляра
    self.name = name
    self.age = age
```

![1782783755627](image/oop/1782783755627.png)



### Ловушка с изменяемыми значениями по умолчанию

```Python
class Student:
  def __init__(self, name, grades=[]):
    self.name = name
    self.grades = grades

s1 = Student("Ann")
s1.grades.append(5)
print(s1.grades)  # [5]

s2 = Student("Ivan")
print(s2.grades)  # Ожидаем []
> [5]
```

Иван унаследовал оценку Анны, потому что значения по умолчанию вычисляются один раз, в момент определения функции, а не при каждом вызове. Список `[]` создан один раз и переиспользуется всеми вызовами `Student()` без аргумента `grades`. Так, `s1.grades` и `s2.grades` указывают на один и тот же список в памяти.

Правильный паттерн: ставить `None` по умолчанию, а реальный список создавать внутри

```Python
class Student:
  def __init__(self, name, grades=None):
    self.name = name
    self.grades = grades if grades is not None else []

s1 = Student("Анна")
s1.grades.append(5)
print(s1.grades)
> [5]

s2 = Student("Иван")
print(s2.grades)
> []
```


### Методы бывают 4 видов:

- Обычные (методы экземпляра): работают с конкретным объектом через self.
- Классовые. Работают с классом в целом, получают cls.
- Статические. Не получают ни `self`, ни `cls`.
- Специальные. Имеют особое значение для Python (`__init__`, `__str__`).


**Обычные** - функции внутри класса, принимающие self первым параметром. Через self обращаются к атрибутам объекта и вызывают другие методы

```Python
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
	return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

# Создаём прямоугольник и вызываем методы
rect = Rectangle(5, 3)
print('Area: ', rect.area())
print('Perimeter', rect.perimeter())
```


Методы класса получают сам класс первым параметром (обычно называется `cls`), а не экземпляр. Декорируется через `@classmethod`. Часто используется как альтернативные конструкторы.

```Python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    # Метод класса: альтернативный конструктор
    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split("."))
        return cls(day, month, year)


# Стандартное создание объекта
date1 = Date(15, 6, 2023)
print(date1.display())

date2 = Date.from_string("25.12.2005")
print(date2.display())
```


Статические методы - не получают ни self, ни cls. Декорируются через `@staticmethod.` Используются для вспомогательных функций, логически связанных с классом, но не требующих доступа к его состоянию.

```Python
class MathUtils:
    @staticmethod
    def is_prime(number):
        """Проверяет, является ли число простым"""
        if number > 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
  
# Вызов
print(MathUtils.is_prime(7))  # True
```


Специальные методы: методы с двойными подчёркиваниями в имени (`__init__`, `__str__`, `__add__`, `__eq__`). Python вызывает их сам при определённых операциях: создание объекта, печать, сложение, сравнение.

```Python
class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Строковое представление
  def __str__(self):
    return f"Vector({self.x}, {self.y})"

  # Перезагрузка оператора +
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  # Перезагрущка оператора ==
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y)

  v1 = Vector(3, 4)
  v2 = Vector(1, 2)
  v3 = Vector(3, 4)

  print(v1)  # вызов __str__
  print(v1 + v1)  # __add__
  print(v1 == v1)  # __eq__
```

Часто используемые специальные методы: init, str, repr (строковое представление для разработчика), len, getitem, setitem, call (вызов), add, sub (вычитание), eq, lt.



