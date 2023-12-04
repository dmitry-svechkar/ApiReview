![image](https://github.com/KypaH4NK/api_yamdb/assets/138603861/19b60d2f-203f-41aa-a33e-0a9817db2be0)
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
