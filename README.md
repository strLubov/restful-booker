# Проект автотестирования для платформы RestfulBooker

[RestfulBooker](https://automationintesting.online/) - тестовая платформа, реализующая функционал для онлайн бронирования гостиницы

## Проверяется функционал

API:

* Создание бронирования (метод POST)
* Редактирование бронирования (метод PUT)
* Частичное обновление бронирования (метод PATCH)
* Удаление бронирования (метод DELETE)
* Получение бронирования по различным фильтрам (метод GET)

UI:

* Создание комнаты
* Редактирование комнаты
* Редактирование контактной информации

## Особенности тестов

В UI тестах реализована авторизации через API с помощью фистуры open_browser_with_cookie.

Тест test_create_room параметризован для проверки создания всех видов комнат.

## Запуск тестов

Локально 

```bash
pytest
```

С помощью [JOB](https://jenkins.autotests.cloud/job/StrelnikovaL_restful-booker/) в Jenkins

![Нажать "Собрать с параметрами"](https://github.com/strLubov/restful-booker/blob/main/src/img/setting.png)

![Указать значение версии браузера при необходимости](https://github.com/strLubov/restful-booker/blob/main/src/img/param.png)

![Посмотреть выполнение прогона](https://github.com/strLubov/restful-booker/blob/main/src/img/status.png)

![Посмотреть подробный отчет](https://github.com/strLubov/restful-booker/blob/main/src/img/allure-report.png)

[Ссылка](https://jenkins.autotests.cloud/job/StrelnikovaL_restful-booker/allure/) на allure отчет. Allure отчет содержит два suites: API и UI. Для UI тестов приложены логи, скриншот и видео о прохождении теста




