# Dordoi Association Backend

Django REST API для приложения Dordoi Association.

## Локальная разработка

### Требования
- Python 3.12.7
- pip
- virtualenv (рекомендуется)

### Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd dordoi-association-back
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` на основе `.env.example`:
```bash
cp .env.example .env
```

5. Выполните миграции:
```bash
python manage.py migrate
```

6. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

7. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Деплой на Heroku

### Предварительные требования
- Аккаунт Heroku
- Heroku CLI

### Шаги деплоя

1. **Создайте приложение Heroku:**
```bash
heroku create your-app-name
```

2. **Настройте переменные окружения:**
```bash
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
heroku config:set CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

3. **Добавьте PostgreSQL addon:**
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. **Задеплойте приложение:**
```bash
git push heroku master
```

5. **Выполните миграции на Heroku:**
```bash
heroku run python manage.py migrate
```

6. **Создайте суперпользователя:**
```bash
heroku run python manage.py createsuperuser
```

### Проверка деплоя

- **Health Check:** `https://your-app-name.herokuapp.com/health/`
- **API Docs:** `https://your-app-name.herokuapp.com/swagger/`
- **Admin Panel:** `https://your-app-name.herokuapp.com/admin/`

## Структура проекта

```
dordoi-association-back/
├── core/                    # Основные настройки Django
│   ├── settings.py         # Настройки проекта
│   ├── urls.py            # URL конфигурация
│   ├── views.py           # Общие views
│   └── wsgi.py            # WSGI конфигурация
├── about_us/              # Приложение "О нас"
├── presscentre/           # Приложение пресс-центра
├── partners/              # Приложение партнеров
├── requirements.txt       # Зависимости Python
├── Procfile              # Конфигурация Heroku
├── runtime.txt           # Версия Python для Heroku
├── release.py            # Скрипт релиза
└── .env.example          # Пример переменных окружения
```

## API Endpoints

### About Us
- `GET /api/about-us/facts/?language=ru|en|kg` - Факты
- `GET /api/about-us/details/?language=ru|en|kg` - Детали фактов

### Press Centre
- `GET /api/presscentre/news/` - Новости
- `GET /api/presscentre/news/{id}/` - Детали новости

### Partners
- `GET /api/partners/` - Партнеры

### Documentation
- `GET /api/schema/` - OpenAPI схема
- `GET /swagger/` - Swagger UI
- `GET /redoc/` - ReDoc

## Переменные окружения

| Переменная | Описание | Значение по умолчанию |
|------------|----------|----------------------|
| `SECRET_KEY` | Секретный ключ Django | - |
| `DEBUG` | Режим отладки | `False` |
| `ALLOWED_HOSTS` | Разрешенные хосты | `localhost,127.0.0.1` |
| `DATABASE_URL` | URL базы данных | SQLite локально, PostgreSQL на Heroku |
| `CORS_ALLOWED_ORIGINS` | Разрешенные origins для CORS | `http://localhost:3000,http://localhost:5173` |
| `BUCKETEER_AWS_ACCESS_KEY_ID` | AWS Access Key ID для S3 | - |
| `BUCKETEER_AWS_REGION` | AWS регион для S3 | - |
| `BUCKETEER_AWS_SECRET_ACCESS_KEY` | AWS Secret Access Key для S3 | - |
| `BUCKETEER_BUCKET_NAME` | Имя S3 бакета | - |

## Разработка

### Создание новой миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

### Создание нового приложения
```bash
python manage.py startapp app_name
```

### Запуск тестов
```bash
python manage.py test
```

## Хранение файлов

Проект поддерживает два режима хранения медиа файлов:

### 1. Локальное хранение (разработка)
По умолчанию файлы хранятся локально в папке `mediafiles/`.

### 2. AWS S3 (продакшн)
При наличии переменных окружения для AWS S3, все медиа файлы автоматически сохраняются в облаке.

**Настройка S3:**
1. Добавьте Bucketeer addon: `heroku addons:create bucketeer`
2. Или установите переменные вручную:
   ```bash
   heroku config:set BUCKETEER_AWS_ACCESS_KEY_ID=...
   heroku config:set BUCKETEER_AWS_REGION=...
   heroku config:set BUCKETEER_AWS_SECRET_ACCESS_KEY=...
   heroku config:set BUCKETEER_BUCKET_NAME=...
   ```

**Преимущества S3:**
- ✅ Надежное хранение
- ✅ Автоматическое масштабирование
- ✅ Доступность файлов через CDN
- ✅ Резервное копирование