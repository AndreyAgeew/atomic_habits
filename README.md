# Atomic Habits App


Добро пожаловать в приложение "Atomic Habits"! Это приложение поможет вам управлять вашими привычками и целями,
соблюдать регулярность и отслеживать свой прогресс. В этом README мы предоставим вам информацию о проекте и его
настройках.

## Описание проекта

Atomic Habits - это веб-приложение, разработанное для помощи пользователям создавать, отслеживать и поддерживать
полезные привычки. Приложение предоставляет возможность создавать привычки, устанавливать напоминания и отслеживать
выполнение целей.

## Стек технологий

Проект разработан с использованием следующего технологического стека:

- Python 3.11
- Django: веб-фреймворк для создания веб-приложений
- Django REST framework: библиотека для создания RESTful API
- Celery: для асинхронных задач
- Redis: как брокер сообщений для Celery
- HTML/CSS: для пользовательского интерфейса
- Docker: для контейнеризации приложения


## Инструкция по установке

Чтобы развернуть проект и начать использовать его, выполните следующие шаги:

1. **Склонируйте репозиторий**: Выполните команду Git для клонирования репозитория на свой локальный компьютер.

   ```bash
   git clone https://github.com/AndreyAgeew/atomic_habits.git
2. **Установите зависимости::**

   ```bash
   cd atomic_habits
   pip install -r requirements.txt

3. **Настройте файл .env и .env-non-dev: Создайте файл .env и .env-non-dev в корневой директории проекта и добавьте в
   него переменные среды, например:**

- SECRET_KEY='КЛЮЧ ОТ DJANGO ПРИЛОЖЕНИЯ'
- DOMAIN_NAME='НАПРИМЕР <http://127.0.0.1:8000/>'
- DB_HOST='ХОСТ ДБ НАПРИМЕР <localhost>'
- POSTGRES_DB='<НАЗВАНИЕ БД>'
- POSTGRES_USER='<ИМЯ ПОЛЬЗОВАТЕЛЯ БД>'
- POSTGRES_PASSWORD='<ПАРОЛЬ ОТ БД>'
- EMAIL_HOST_USER='<ВАША GMAIL ПОЧТА>'
- EMAIL_HOST_PASSWORD='<ПАРОЛЬ ПРИЛОЖЕНИЯ ОТ GMAIL ПОЧТЫ>'
- CACHES_LOCATION='НАПРИМЕР <redis://127.0.0.1:6379>'
- ADMIN_PASSWORD='<ПАРОЛЬ АДМИНА>'
- MODERATOR_EMAIL='<ПОЧТА МОДЕРАТОРА>'
- STRIPE_API_KEY='<ВАШ STRIPE КЛЮЧ>'
- CELERY_BROKER_HOST='НАПРИМЕР <redis://127.0.0.1:6379/0>'
- CHAT_ID_ADMIN='<ВАШ ID В ТГ>'
- TELEGRAM_API_TOKEN='<ВАШ API ТОКЕН ДЛЯ ТЕЛЕГРАММ БОТА>'

4. **Выполните миграции для создания базы данных:**

   ```bash
   python manage.py migrate
5. **Запустите приложение:**

   ```bash
   python manage.py runserver
6. **Откройте приложение:** Перейдите в веб-браузере по адресу http://127.0.0.1:8000/ и начните использовать приложение.

## Краткая инструкция по эндпоинтам

В приложении "Atomic Habits" есть несколько важных эндпоинтов:
* /habits/ - список и создание привычек.
* /habits/<int:pk>/ - просмотр, обновление и удаление привычки.
* /habits/public/ - список публичных привычек.

## Важаный момент Celery для Windows


**Запустите Celery для асинхронной обработки задач, таких как отправка уведомлений:**
  
  ```bash
  celery -A atomic_habits worker -l info -P eventlet
  celery -A atomic_habits beat
  ```

## Инструкция по Docker:

#### Установите Docker и Docker Compose:

* Установите Docker, следуя инструкциям для вашей операционной
  системы: [Docker Install](https://docs.docker.com/get-docker/).
* Установите Docker Compose: [Docker Compose Install](https://docs.docker.com/compose/install/).

#### Запустите приложение:

* Откройте терминал в директории с файлом docker-compose.yml.
* Выполните следующую команду:
    ```bash
        docker-compose up

Docker Compose загрузит образы, создаст и запустит контейнеры для ваших сервисов.

#### Проверьте приложение:

После успешного запуска, ваше приложение Atomic Habits должно быть доступно по адресу http://localhost:7777.

#### Остановите приложение:

* В терминале, где была запущена команда docker-compose up, нажмите Ctrl+C для остановки контейнеров.

## Автор проекта
Этот проект создан и поддерживается Агеевым Андреем.

Если у вас есть вопросы или предложения по улучшению проекта, свяжитесь со мной по адресу mr1993@bk.ru.

<em>Спасибо, что выбрали "Atomic Habits" для управления вашими привычками!</em>

