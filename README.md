# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.  

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить
Создать файл `.env`, содержащий переменные окружения:

- `ENGINE` - драйвер базы данных для django
- `HOST` - адрес размещения базы данных
- `PORT` - порт на котором работает база данных
- `NAME` - имя базы данных
- `USER` - логин пользователя
- `PASSWORD` - пароль пользователя
- `DEBUG` - режим дебага (`True`|`False`)

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).