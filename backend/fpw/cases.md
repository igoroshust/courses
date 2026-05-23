# Вывести пары ключ-значение

**Моё решение**
```python
import pprint
user_dict = {input('Введите ключ: '): input('Введите значение: ') for i in range(3)}

pprint.pprint(user_dict)
```

**Генератор**
```python
import pprint
user_dict = {line.split()[0]: line.split()[1] for line in (input(': ') for _ in range(3))}
pprint.pprint(user_dict)
```

**Преобразование списка в словарь**
```python
lst = [1, 2, 3, 4, 5, 6, 7, 8]
d = dict(zip(lst[::2], lst[1::2]))

print(d)
```