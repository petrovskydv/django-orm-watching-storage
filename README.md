# Пульт охраны банка

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников банка. Вы не сможете запустить репозиторий без доступа к БД, но можете использовать код верстки или посмотреть как реализованы запросы к БД.

## Как установить
Скачайте проект на свой компьютер.
В папке проекта необходимо создать файл `.env`. В этом файле нужно создать переменные, указанные в образце.

Образец файла:
```
ENGINE='тип БД'
HOST='адрес БД'
PORT='порт БД'
NAME='имя БД'
USER='логин БД'
PASSWORD='пароль БД'
SECRET_KEY='ключ приложения'
DEBUG=false
```
Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как запустить

Для запуска на компьютере необходимо ввести в командной строке:
```
python manage.py runserver
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Лицензия

Этот проект находится под лицензией MIT License - подробности см. в файле LICENSE.