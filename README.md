# JKH


## Документация
```
http://127.0.0.1:8000/schema/docs/
```

## Краткое описание
Настроены автотесты, проект можно развернуть сразу в контейнерах, в test/fixtures есть factories через них можно создать тестовые данные.
для корректного подсчет надо создать instance Tariff с именем 'rent' - кварплата, 'water_bill' - тариф для счетчиков

PS Немного не понял формулировку про ввод данных по дому, надо ли сделать один post запрос или несколько, решил придерживаться KISS и сделал для каждого отдельный роут на создание.