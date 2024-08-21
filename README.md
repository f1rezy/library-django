# library-django

## Конфигурация .env

Скопируйте файл `.env.dist` в `.env` и, если нужно, отредактируйте значения переменных

```bash
cp .env.dist .env
```

## Создание билда nginx

```bash
cd nginx
mkdir build
```

## Создание профиля администратора
```bash
docker compose run app python app/manage.py migrate
docker compose run app python app/manage.py createsuperuser --username admin --email admin@example.com
```

## Запуск бота

```bash
docker compose up --build
```