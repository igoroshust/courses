# Добавить отдельную папку

```bash
# 1. Клонируем репозиторий в sparse-режиме
git clone --depth 1 --filter=blob:none --sparse https://github.com/igoroshust/practice.git practice
cd practice

# 2. Указываем, какие папки хотим разархивировать
git sparse-checkout set js

# 3. Если нужны другие папки, указываем:
git sparse-checkout add другая-папка
```