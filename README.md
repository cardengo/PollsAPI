## API опросов пользователей

### Функционал для администратора системы:
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: 
    * название
    * дата старта (после создания поля, менять его нельзя)
    * дата окончания
    * описаниe
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов:
    * текст вопроса
    * тип вопроса (
        ответ текстом
        ответ с выбором одного варианта
        ответ с выбором нескольких вариантов
    )

### Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса:
    * опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы;
    * один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

### Стек
* `Django`
* `Django REST Framework`
* `PostgreSQL`


### Точки входа
1. POST, PATCH, DELETE:
* `poll/`
* `poll/<int:poll_id>/`

POST, PATCH, DELETE:
* `question/`
* `question/<int:question_id>/`


### Разворачивание (локально)
```
python3 -m pip venv env
source env/bin/activate

python3 -m pip install -r requirements.txt
```
#### настройка БД
```
export DB_NAME='db_name'

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
#### Запуск сервера
```
python3 manage.py runserver
```

### Параментры БД
* `$DB_NAME` - имя базы данных

Дополнительные настройки:
* `DB_USER` - имя пользователя
* `DB_PASSWORD` - пароль БД
* `DB_HOST` - хост ДБ (по умолчанию `localhost`)
* `DB_PORT` - порт ДБ
   