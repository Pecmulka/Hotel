# Гостиница (Hotel)

Django-приложение для управления гостиничным бизнесом. Включает модели для номеров, бронирований, клиентов и других сущностей.

## Начало работы

Эти инструкции помогут вам запустить копию проекта на локальном компьютере для разработки и тестирования.

### Необходимые условия

Убедитесь, что у вас установлены:

- Python 3.9+
- Django 4.x
- База данных PostgreSQL
- Git

Пример установки Python:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Pecmulka/Hotel.git
```

2. Перейдите в папку проекта

```bash
cd hotel_business
```

3. Установите зависимости
```bash
pip install django psycopg2-binary 
```

4. Примените миграции

```bash
python manage.py migrate
```

5. Запустите сервер

```bash
python manage.py runserver
```

Теперь приложение досутпно по адресу http://127.0.0.1:8000