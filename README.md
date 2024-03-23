
Запуск redis (для мак)
```
 brew services start redis
```

Запуск приложения
```
 python manage.py runserver
```

Запуск celery
```
 celery -A core worker -l info
```

Зпуска теста нагрузки (см. скриншот теста test.png)
```
locust
```

Серивис ожидает что в теле запроса есть идентификатор запроса. Наприме:
```
{
    "request_id": 123
}
```
