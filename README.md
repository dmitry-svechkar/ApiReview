<p align="center">
  <img src="https://top-fon.com/uploads/posts/2023-01/1674926151_top-fon-com-p-chelovechki-dlya-prezentatsii-bez-fona-bes-18.jpg" />
</p>

### Описание
Учебный проект ЯП. Работа в группе. Спринт 12.

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. 

Пользователи могут оставлять отзывы и комментарии к опубликованным на сервире произведениям.

В проекте реализованы:
- Аутентификация  по JWT-токену.
- Полностью настроен REST API для добавления произведений, отзывов и комментариев. 
- Импорт данных в БД.
### Участники проекта

- [ Кирилл](https://github.com/KypaH4NK)
- [Дмитрий](https://github.com/dmitry-svechkar)
- [Максим](https://github.com/swapper1983)


### Стек технологий

- Python 3.9
- Django 3.2
- DRF 3.12
- JWT


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:KypaH4NK/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Когда вы запустите проект, по адресу  `http://127.0.0.1:8000/redoc/` будет доступна документация для API Yatube. В документации описано, как должен работать  API. Документация представлена в формате Redoc.

### Примеры запросов
![image](https://github.com/KypaH4NK/api_yamdb/assets/138603861/a5cbcd36-5bab-4cf6-bfda-51a47f9fca62)
![image](https://github.com/KypaH4NK/api_yamdb/assets/138603861/6ede1d3f-2ce7-4012-aec7-183c7b68c109)
![image](https://github.com/KypaH4NK/api_yamdb/assets/138603861/2e0e1ca7-2665-4223-9073-bcce90670767)


