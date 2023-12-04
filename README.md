# Описание
Учебный прект ЯП. Работа в группе. Спринт 12.
![image](https://github.com/KypaH4NK/api_yamdb/assets/138603861/5ef7319a-1bc0-4cbf-a202-d733138b428a)


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
