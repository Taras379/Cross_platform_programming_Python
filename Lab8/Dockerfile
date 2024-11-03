FROM python:3.10-slim

# Встановлення залежностей для Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc

# Налаштування робочого каталогу
WORKDIR /app

# Копіювання файлу вимог (requirements.txt)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання всіх файлів проєкту в контейнер
COPY . .

# Запуск Django-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
