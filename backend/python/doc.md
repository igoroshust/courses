












# JSON

JSON (JavaScript Object Notation) – текстовый формат обмена данными. Он простой, человекочитаемый и поддерживается почти всеми языками.

### Главные правила

1. Ключи всегда в двойных кавычках
2. Значения: строка, число, булево (true/false), null, объект, массив
3. Внутри объектов пары "ключ: значение" разделяются запятыми; после последнего элемента запятой быть не должно.
4. Объекты - в `{ }`, массивы - в `[ ]`

Пример простого объекта

```JSON
{
  "name": "Мария",
  "age": 25,
  "isMember": true,
  "balance": null
}
```

Массив

```JSON
[
  "яблоко",
  "банан",
  "апельсин"
]
```

Вложенные структуры

```JSON
{
  "user": {
    "name": "Мария",
    "address": {
      "city": "Чита",
      "zip": "1900000"
    },
    "phones": ["+79...", "+79..."]
  }
}
```

Массив объектов

```JSON
[
  {
  "id": 1,
  "name": "Иван",
  "role": "developer"
}, {
  "id": 2,
  "name": "Ольга",
  "role": "designer"
}
]
```

### Частые ошибки

1. Одинарные кавычки - нельзя
2. Запятая после последнего элемента
3. Ключи без кавычек
4. Комментарии - в стандартном JSON их нет

## Примеры

1. Ответ сервера

```Python
from django.http import JsonResponse

def user_view(request):
    data = {
        "id": 42,
        "username": "maria_dev",
        "roles": ["editor", "viewer"],
        "active": True,
        "profile": {
            "bio": "Люблю Python",
            "skills": ["Django", "SQL"]
        }
    }
  
    return JsonResponse(data)  # сам делает ensure_ascii=False и правильный Content-Type
```

2. Подготовка данных для PostgreSQL. Подготовка JSON для вставки в колонку `jsonb`:

```Python
import json

payload = {
    "user_id": 123,
    "actions": ["login", "view_page"],
    "meta": {"ip": "192.168.0.1", "ua": "Chrome"}
}

# Для БД лучше компактный JSON без indent
json_text = json.dumps(payload, ensure_ascii=False)
# Дальше передавать json_text в INSERT/UPDATE для jsonb-колонки
```

3. Конфигурационный JSON (настройка тестов)

config.json

```JSON
{
  "db": {
    "host": "localhost",
    "port": 5432,
    "name": "test_db"
  },
  "features": {
    "enable_cache": true,
    "max_workers": 4
  }
}
```

main.py

```Python
import json

with open("config.json", "r", encoding="utf-8") as f:
  cfg = json.load(f)

host = cfg["db"]["host"]
```

# JsonResponse (Django)

JsonResponse - удобный класс джанго для возврата HTTP-ответа с JSON, наследуемый от HttpResponse и берущий на себя всю грязную работу `from django.http import JsonResponse`

```Python
from django.http import JsonResponse

def user_view(request):
  data = {
    "id": 42,
    "username": "maria_dev",
    "roles": ["editor", "viewer"],
    "active": True
  }

  return JsonResponse(data)
```

Под капотом:

1. Сериализация в JSON. Джанго превращает пайтон объект в джсон через `json.dumps`
2. Установка заголовка `Content-Type` в `application/json; charset=utf-8`. Без этого браузер не поймёт, что это json.
3. Кодировка и экранирование. Делает всё безопасно и в UTF-8, чтобы кириллица и спецсимволы не ломались.
4. Обработка ошибок. Если данные нельзя превратить в JSON (например, есть datetime без конвертации), Django выбросит понятную ошибку.

Для разрешения списка при передаче данных нужно использовать `safe=False`, так как JsonResponse(data) по умолчанию ожидает, что data - словарь.

```Python
# Список объектов
users = [
    {"id": 1, "name": "Иван"},
    {"id": 2, "name": "Ольга"}
]
return JsonResponse(users, safe=False)
```

Передача HTTP-статуса_

```Python
return JsonResponse({"error": "Not found"}, status=404)
```

### Работа со сложными типами

Стандартный JSON не умеет в datetime. Если в словаре есть дата, будет ошибка. Решения:

1. Заранее превратить даты в строки

```Python
data["created_at"] = obj.created_at.isoformat()
return JsonResponse(data)
```

2. Использовать кастомный энкодер (продвинутый). DjangoJSONEncoder знает, как превращать datetime, date, Decimal и т.п. в JSON-совместимые типы.

```Python
from django.core.serializers.json import DjangoJSONEncoder

return JsonResponse(data, encoder=DjangoJSONEncoder)
```

### Создание вручную (не рекомендуется)

```Python
import json
from django.http import HttpResponse

def view(request):
  data = {"name": "Мария"}
  body = json.dumps(data, ensure_ascii=False
  return HttpResponse(body, content_type="application/json; charset=utf-8")
```

Но лучше JsonResponse. Меньше кода, меньше шансов забыть про content-type и всё уже настроено под utf-8.

```Python
from django.http import JsonResponse

def view(request):
  data = {"name": "Мария"}
  return JsonResponse(data)_
```

# Стили обработки ситуаций

LBYL - look before you leap (сначала посмотри, потом прыгай) - стиль обработки ситуаций, когда условия явно проверяются до операции, чтобы убедиться, что всё безопасно

```Python
def check_age(age):
  age = int(age)  # Сразу нормализуем
  return age + 1
```

EAFP (Easier to Ask Forgiveness than Permission) - проще попросить прощения, чем разрешения (делаем смело, ловим ошибку). Просто выполняем операцию, а если что-то пойдёт не так – обрабатываем исключение.

```Python
try:
  value = data['key']
except KeyError:
  value = None
```



