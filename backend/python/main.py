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
