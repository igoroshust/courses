# Конкурентность, параллелизм, асинхронность

Программе необходимо скачать 100 страниц с разных сайтов. Отправлять запросы по очереди – означает ждать ответ от сервера в течении 1-2 секунд, что увеличивает общее время (сумма всех ожиданий). Большую часть этого времени процессор простаивает, пока один запрос ждёт ответа – могут быть отправлены другие. Это и есть конкурентное выполнение.

Python has three tools for this: threading, multiprocessing, asyncio.

- Concurrency (конкурентность): tasks can be switched between each other, creating the illusion of simultaneous work. One barista at the counter takes an order, puts the milk on to heat, moves on to the next customer, and returns to the milk. One performer, several tasks "in the air" at the same time.
- Parallelism: tasks are executed physically simultaneously on different processor cores. Several baristas, each making their own coffee. Requires multi-core processing.
- Asynchronicity: a way of organizing code in which a task can be "delayed" while waiting (for example, for a server response) without blocking the entire thread. This is a way to achieve concurrency on a single thread without switching OS.

Concurrency is the goal, parallelism and asynchrony are to ways to achieve it.

![1783130778946](image/async/1783130778946.png)

## I/O-bound vs CPU-bound: key dichotomy

The choice of tool depends only on what your task is:

- I/O-bound: the processor is idle waiting for an external resource. Network request, read from disk, database response. Here, asynchronous processing wins: while one request is waiting, we send the next ones.
- CPU-bound: the processor is working hard on calculations. Image compression, encryption, scientific computing. This requires real parallelism across multiple cores.

The most common beginner mistake is using multiprocessing for page downloads or asyncio for matrix multiplication. This will result in slowdowns, not speedups.

I/O-bound и CPU-bound - это категории задач по тому, что становится узким местом при их выполнении: ввод-вывод или вычисления на процессоре.

### IO (ограничено вводом-выводом)

Задача большую часть времени ждёт ответа от внешнего ресурса, а процессор почти не нагружен.

**Примеры**

- HTTP-запросы к API и ожидание ответа (сеть)
- Чтение файла с диска
- Запрос к БД и ожидание результата (сеть + диск)
- Ожидание ввода пользователя

Допустим, запрос к серверу идёт 1 секунду, а обработка ответа - 10 мс. Из этих 1010 мс процессор реально занят только 10 мс, остальное время поток висит в ожидании.

**Использование в Python**

- asyncio - запуск других запросов в момент, когда один запрос "ждёт"
- threading - В CPython для I/O-задач потоки полезны, потому что во время ожидания GIL освобождаются.
- concurrent.futures.ThreadPoolExecutor - удобная обёртка над потоками.

**I/O-bound-задача** - скачивание 100 страниц сайта. Основное время тратится на ожидание сети, а не на вычисления.


### CPU-bound (ограничено процессором)

Задача активно нагружает CPU вычислениями, почти не обращаясь к внешним ресурсам.

**Примеры**

- Сжатие, кодирование, шифрование данных
- Обработка изображений (фильтры, ресайз)
- Расчёт математических моделей, симуляции
- Парсинг и тяжёлые преобразования больших объемов текста

Почти 100% времени процессор занят выполнением инструкций.

**Использование в Python**

- Процессы (multiprocessing) - чтобы обойти GIL и задействовать несколько ядер.
- concurrent.futures.ProcessPoolExecutor - простой способ запустить задачи на нескольких ядрах
- Вызовы на C/C++/Rust (NumPy) - чтобы тяжёлые вычисления шли вне интерпретатора Python.

**CPU-bound-задача** - перемножение больших матриц или перебор вариантов в задаче оптимизации.

**The difference is clear**

```Python
import time
import requests

# I/O-bound: waiting for network
def fetch_url(url):
    r = requests.get(url)
    return r.text


# CPU-bound: a lot of calculations
def heavy_compute(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

start = time.time()
fetch_url("https://jsonplaceholder.typicode.com/users/1/")  # We wait for an answer most of the time.
print("I/O time:", time.time() - start)

start = time.time()
heavy_compute(10_000_000)  # The CPU is running almost all the time.
print("CPU time:", time.time() - start)
```


## GIL

В стандартной реализации Python (CPython) есть Global Interpreter Lock (GIL) – глобальный замок, разрешающий выполнять Python-код только одному потоку за раз внутри процесса. Даже если у вас 8 ядер, потоки выполняются по очереди.

- Для CPU-bound задач threading бесполезен - потоки делят одно ядро через GIL. Нужны процессы (multiprocessing), у каждого свой GIL и своё ядро.
- Для I/O-bound задач GIL отпускается при ожидании сети/диска. Поэтому threading отлично подходит для I/O, как и asyncio (но без накладных расходов на потоки).

**Tools for a specific situation**

1. Множество сетевых запросов, тысячи соединений – asyncio
2. I/O в legacy-коде без async-библиотек – threading
3. Тяжёлые вычисления на нескольких ядрах – multiprocessing
4. Простое распараллеливание без погружения в детали – concurrent.futures (ThreadPoolExecutor, ProcessPoolExecutor)

Поток - легковесный исполнитель внутри одного процесса (для I/O), процесс - это отдельная программа с собственной памятью (для CPU-bound).
