### Rest API сервис.
В рамках данного проекта любой пользователь может оставить рецензию на опубликованные произведения (фильмы, музыка, литература и другое), а так же принять участие в обсуждениях и комментировании.

Пользователи могут оставлять отзывы и комментарии к опубликованным на сервире произведениям.

Проект реализовывался в команде из 3 backend-разработчиков.

В проекте реализованы:
- Кастомные роли пользователей.
- Аутентификация  по JWT-токену.
- Полностью настроен REST API для добавления произведений, отзывов и комментариев. 
- Импорт/Экспорт данных в БД.
- Настроена админ-панель.


### Стек технологий
<div>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-line-wordmark.svg" width="50" height="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" width="50" height="50">
</div>

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dmitry-svechkar/ApiReview.git
```
###### Cоздать и активировать виртуальное окружение:
- Windows
```
python -m venv venv
source venv/Scripts/activate
```
- Linux
```
python3 -m venv venv
source venv/bin/activate
```
###### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```


###### Для подлючения  к БД необходимо указать данные для подключения к БД и данные проекта.
```
POSTGRES_USER=username
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=db_name
DB_HOST=db
DB_PORT=5432
SECRET_KEY=any_secret_key_of_django_project
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
```
###### Выполнить миграции:
```
python manage.py migrate
```


###### К проекту имеются заготовки для БД. Для импорта необходимо ввести команду:
```
python manage.py import_csv
```

###### Запустить проект:

```
python manage.py runserver
```
Когда Вы запустите проект, по адресу  `http://127.0.0.1:8000/redoc/` будет доступна документация для API. В документации описано, как должен работать  API.



