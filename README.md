# Auto Mailing

**Тестовое задание от Фабрики Решений**

Сервис уведомлений - создание автоматических рассылок для пользователей.

# Руководство по работе с проектом для разработчиков

## Требования

- python=3.8.10

## Настройка и установка проекта

1. Склонировать репозиторий с помощью команды:
   ```
   git clone https://github.com/alinocco/auto-mailing.git
   ```
2. Перейти в папку с проектом:
   ```
   cd auto-mailing
   ```
3. Установить **poetry**:
   ```
   pip3 install poetry
   ```
4. Активировать виртуальное окружение:
   ```
   poetry shell
   ```
5. Установить зависимости:
   ```
   poetry install
   ```
6. Установить Docker и docker-compose с [официального сайта](https://www.docker.com/products/docker-desktop)
7. Запустить сервисы в Docker (PostgreSQL, Redis):
   ```
   docker-compose -f basic-compose.yml up -d --build --remove-orphans
   ```
8. Получить креды от внешних сервисов и положить их в папку conf. _Для проверки оставляю открытым файл .env._

9. Применить миграции:
   ```
   python3 src/manage.py migrate
   ```
10. Запустить сервер приложения:
    ```
    python3 src/manage.py runserver
    ```
11. При необходимости запустить Celery:
    ```
    cd src && celery -A automailing worker -B -l INFO
    ```
