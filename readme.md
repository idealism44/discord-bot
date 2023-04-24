# Введение
Бот разработан в рамках проекта "[Virtual Company Systems](https://vk.com/vcsys)" и предназначен для автоматизации процессов виртуальных транспортных компаний ETS 2/ATS. 

# Подготовка к запуску

## База данных
В проекте используется PostgreSQL.

Создайте файл `db_secret.sec` в корне репозитория со следующим содержанием:
```
<имя базы данных>
<имя пользователя базы данных>
```

Запустите `./scripts/setupdb.sh` для создания таблиц из `schema.sql`, указав в качестве базы данных указанную в `db_secret.sec`, а в качестве имени пользователя — уполномоченного создавать таблицы.

## Среда
В качестве виртуального окружения используется poetry. Для его инициализации в корне проекта необходимо запустить:
```
poetry init
```

## VSCode
В .vscode содержатся верные конфигурации для запуска дебага и тестов. Дополнительных настроек не требуется.

# Запуск
Запуск осуществляется исключительно через poetry:
```
poetry run bot
```
Поскольку в проекте используется относительное
импортирование, при запуске другим способом это приведёт к ошибкам импортирования.

# Совместная разработка
TODO

# Ресурсы проекта
TODO