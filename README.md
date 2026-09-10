# 📝 Task Manager — Django + PostgreSQL + Docker

Небольшой backend‑проект на Django, демонстрирующий работу с PostgreSQL, ORM, миграциями, SQL‑запросами, management‑командами и контейнеризацией через Docker / Docker Compose.
Проект включает CRUD‑логику задач, примеры ORM, импорт данных, SQL‑файл с JOIN‑запросами и полноценный Docker‑стек для локального запуска.

## 🚀 Стек технологий
- Python 3.12
- Django 5
- PostgreSQL 15/18
- Docker / Docker Compose
- Django ORM
- SQL (JOIN, GROUP BY, SELECT)
- pgAdmin 4

## 📦 Установка и запуск (через Docker)
1. Клонировать проект
```
git clone https://github.com/Icestorm203/django-task-manager.git
cd django-task-manager
```
2. Собрать и запустить контейнеры
```
docker compose up --build
```
После запуска проект будет доступен по адресу:
http://localhost:8000

3. Войти в контейнер Django
```
docker compose exec web bash
```
4. Выполнить миграции
```
python manage.py migrate
```
5. Создать суперпользователя
```
python manage.py createsuperuser
```

## 🐘 Подключение к PostgreSQL (Docker).
PostgreSQL работает в контейнере db.

Настройки подключения внутри Django в файле settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taskmanager',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

## 📂 Структура проекта
```
django-task-manager/
│
├── Dockerfile
├── docker-compose.yml
│
├── tasks/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── close_tasks.py
│   ├── templates/
│   │   └── admin/
│   │       ├── task_import_form.html
│   │       └── tasks/task/change_list.html
│   ├── models.py
│   ├── admin.py
│   ├── orm_examples.py
│   └── views.py
│
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── sql/
│   └── sql_examples.sql
│
├── requirements.txt
├── manage.py
└── README.md
```

## 🗄️ Модель Task
```
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

## 🧪 Примеры работы через Django ORM

- Создание задачи:
```
from tasks.models import Task
Task.objects.create(title="Test PG", description="From PostgreSQL")
```
- Получение всех задач:
```
Task.objects.all()
```
- Фильтрация:
```
Task.objects.filter(is_closed=False)
```
- Обновление:
```
Task.objects.filter(id=1).update(is_closed=True)
```
- Удаление:
```
Task.objects.filter(id=1).delete()
```

## 🧩 Management‑команда
Файл: tasks/management/commands/close_tasks.py

Запуск: 
```
python manage.py close_tasks
```

## 🧩 SQL‑примеры (JOIN, GROUP BY, SELECT)
Файл: sql/sql_examples.sql

Содержит:
- BASIC SELECT
- INNER JOIN
- LEFT JOIN
- MULTI JOIN
- FULL OUTER JOIN
- GROUP BY
- CROSS JOIN

## 📊 Пример SQL JOIN
```
SELECT t.id, t.title, ct.model
FROM tasks_task AS t
INNER JOIN django_content_type AS ct
    ON ct.id = t.id;
```

## 🎯 Цели проекта
- Демонстрация навыков Django ORM
- Работа с PostgreSQL и SQL
- Примеры миграций, management‑команд и импорта данных
- Полноценный Docker‑стек для локального запуска
- Учебный backend‑проект для портфолио и собеседований

## ✔️ Статус проекта
Проект полностью рабочий:
Django подключён к PostgreSQL, миграции выполнены, таблицы созданы, ORM и SQL работают, Docker‑контейнеры запускаются корректно.