<p align="center">
  <img src="https://top-fon.com/uploads/posts/2023-01/1674926151_top-fon-com-p-chelovechki-dlya-prezentatsii-bez-fona-bes-18.jpg" />
</p>
# Описание
Учебный прект ЯП. Работа в группе. Спринт 12.


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
