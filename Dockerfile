FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт Django
EXPOSE 8000

# Команда запуска Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
