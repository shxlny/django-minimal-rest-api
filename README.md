# django-minimal-rest-api

Минимальный пример REST API на Django с использованием Django Rest Framework.

## Структура проекта

```plaintext
django-minimal-rest-api/
├── api/                      # Приложение (app) с моделями, сериализаторами, представлениями и URL
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── myapi/                    # Папка проекта с настройками Django (settings, urls, wsgi, asgi)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/                # Папка с шаблонами (если требуется)
├── manage.py                 # Основной управляющий скрипт Django
└── .gitignore                # Файл игнорирования для Git
```plaintext


## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/shxlny/django-minimal-rest-api.git
   cd django-minimal-rest-api

2. **Создайте и активируйте виртуальное окружение:**
   
  *Для Unix/macOS:*
   
       ```bash
       python -m venv .venv
       source .venv/bin/activate
   
  *Для Windows:*
  
       ```bash
       python -m venv .venv
       .venv\Scripts\activate

3. **Установите зависимости:**
   
   ```bash
   pip install django djangorestframework

4. **Примените миграции:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Запустите сервер разработки:**

   ```bash
   python manage.py runserver

6. **Проверьте работу API:**

   `Откройте браузер и перейдите по адресу: http://127.0.0.1:8000/api/items/.
    Здесь вы увидите Browsable API интерфейс, где можно:

    Отправлять GET-запросы для получения списка объектов (на старте список будет пустым).
    Отправлять POST-запросы для создания нового объекта.
   

   
